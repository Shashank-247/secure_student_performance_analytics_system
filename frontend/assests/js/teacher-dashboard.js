import { apiFetch } from "./api.js";

const token = sessionStorage.getItem("access_token");
const role = sessionStorage.getItem("role");

if (!token || role !== "teacher") {
  window.location.href = "login.html";
}

let classData = null;

async function loadTeacherDashboard() {
  try {
    classData = await apiFetch("/teacher/dashboard");

    document.getElementById("avgScore").innerText = classData.avgScore;
    document.getElementById("avgAttendance").innerText =
      classData.avgAttendance + "%";
    document.getElementById("totalStudents").innerText =
      classData.totalStudents;
    document.getElementById("atRisk").innerText = classData.atRisk;

    renderStudentTable(classData.students);
  } catch (err) {
    console.error(err);
    alert("Failed to load teacher dashboard");
  }
}

function renderStudentTable(students) {
  const table = document.getElementById("studentTable");
  table.innerHTML = "";

  students.forEach((s, index) => {
    table.innerHTML += `
      <tr data-index="${index}">
        <td>${s.name}</td>

        <td>
          <input
            type="number"
            class="mark-input"
            value="${s.score}"
            min="0"
            max="500"
          >
        </td>

        <td>${s.grade}</td>

        <td class="attendance-controls">
          <button onclick="changeAttendance(${index}, -1)">-</button>
          <span id="att-${index}">${s.attendance}%</span>
          <button onclick="changeAttendance(${index}, 1)">+</button>
        </td>

        <td>
          <button onclick="saveStudent(${index})">Save</button>
        </td>
      </tr>
    `;
  });
}

function changeAttendance(index, delta) {
  const student = classData.students[index];
  student.attendance = Math.min(100, Math.max(0, student.attendance + delta));
  document.getElementById(`att-${index}`).innerText =
    student.attendance + "%";
}

async function saveStudent(index) {
  const student = classData.students[index];
  const row = document.querySelector(`tr[data-index="${index}"]`);
  const newScore = Number(row.querySelector(".mark-input").value);

  if (newScore < 0 || newScore > 500) {
    alert("Invalid marks entered");
    return;
  }

  try {
    await apiFetch(`/teacher/student/${student.id}`, {
      method: "PUT",
      body: JSON.stringify({
        score: newScore,
        attendance: student.attendance
      })
    });

    alert("Student data updated successfully");
  } catch (err) {
    console.error(err);
    alert("Failed to save student data");
  }
}

loadTeacherDashboard();
