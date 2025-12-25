// Mock class data (from CSV logic)
const classData = {
  avgScore: 398,
  avgAttendance: 84,
  totalStudents: 4,
  atRisk: 1,

  students: [
    { id: 1, name: "Amit Sharma", score: 412, grade: "A", attendance: 88 },
    { id: 2, name: "Riya Singh", score: 365, grade: "B", attendance: 72 },
    { id: 3, name: "Kunal Verma", score: 340, grade: "C", attendance: 65 },
    { id: 4, name: "Neha Patel", score: 430, grade: "A", attendance: 91 }
  ]
};

// Populate KPIs
document.getElementById("avgScore").innerText = classData.avgScore;
document.getElementById("avgAttendance").innerText = classData.avgAttendance + "%";
document.getElementById("totalStudents").innerText = classData.totalStudents;
document.getElementById("atRisk").innerText = classData.atRisk;

// Populate table
const table = document.getElementById("studentTable");

classData.students.forEach((s, index) => {
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

// Attendance control
function changeAttendance(index, delta) {
  const student = classData.students[index];
  student.attendance = Math.min(100, Math.max(0, student.attendance + delta));
  document.getElementById(`att-${index}`).innerText = student.attendance + "%";
}

// Save changes (mock backend call)
function saveStudent(index) {
  const row = document.querySelector(`tr[data-index="${index}"]`);
  const newScore = row.querySelector(".mark-input").value;

  if (newScore < 0 || newScore > 500) {
    alert("Invalid marks entered");
    return;
  }

  classData.students[index].score = parseInt(newScore);

  console.log("Saved changes:", classData.students[index]);

  alert("Changes saved successfully (mock)");
}
