// Mock student list (CSV / DB later)
const students = [
  { roll: "BCA101", name: "Amit Sharma", avg: 85, attendance: 88 },
  { roll: "BCA102", name: "Riya Singh", avg: 72, attendance: 75 },
  { roll: "BCA103", name: "Kunal Verma", avg: 64, attendance: 68 },
  { roll: "BCA104", name: "Neha Patel", avg: 91, attendance: 92 }
];

// Render table
function renderTable(data) {
  const table = document.getElementById("studentsTable");
  table.innerHTML = "";

  data.forEach(s => {
    const status = s.avg < 65 || s.attendance < 75 ? "At Risk" : "Good";

    table.innerHTML += `
      <tr>
        <td>${s.roll}</td>
        <td>${s.name}</td>
        <td>${s.avg}</td>
        <td>${s.attendance}%</td>
        <td>${status}</td>
        <td>
          <button onclick="viewStudent('${s.roll}')">View</button>
        </td>
      </tr>
    `;
  });
}

// Search logic
document.getElementById("searchInput").addEventListener("input", e => {
  const value = e.target.value.toLowerCase();
  const filtered = students.filter(s =>
    s.name.toLowerCase().includes(value) ||
    s.roll.toLowerCase().includes(value)
  );
  renderTable(filtered);
});

// View student detail
function viewStudent(roll) {
  // Later: pass roll via URL or session
  window.location.href = "student-detail.html?roll=" + roll;
}

// Initial render
renderTable(students);
