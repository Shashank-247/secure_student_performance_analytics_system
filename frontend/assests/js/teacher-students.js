import { apiFetch } from "./api.js";

const token = sessionStorage.getItem("access_token");
const role = sessionStorage.getItem("role");

if (!token || role !== "teacher") {
  window.location.href = "login.html";
}

let students = [];

async function loadStudents() {
  try {
    students = await apiFetch("/teacher/students");
    renderTable(students);
  } catch (err) {
    console.error(err);
    alert("Failed to load students");
  }
}

function renderTable(data) {
  const table = document.getElementById("studentsTable");
  table.innerHTML = "";

  if (!data.length) {
    table.innerHTML =
      "<tr><td colspan='6'>No students found</td></tr>";
    return;
  }

  data.forEach(s => {
    const status =
      s.avg_score < 65 || s.attendance < 75 ? "At Risk" : "Good";

    table.innerHTML += `
      <tr>
        <td>${s.roll}</td>
        <td>${s.name}</td>
        <td>${s.avg_score}</td>
        <td>${s.attendance}%</td>
        <td>${status}</td>
        <td>
          <button onclick="viewStudent('${s.id}')">View</button>
        </td>
      </tr>
    `;
  });
}

document.getElementById("searchInput").addEventListener("input", e => {
  const value = e.target.value.toLowerCase();

  const filtered = students.filter(s =>
    s.name.toLowerCase().includes(value) ||
    s.roll.toLowerCase().includes(value)
  );

  renderTable(filtered);
});

function viewStudent(studentId) {
  window.location.href =
    "student-detail.html?id=" + studentId;
}

loadStudents();
