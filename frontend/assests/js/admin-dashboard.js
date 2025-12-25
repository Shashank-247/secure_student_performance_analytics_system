// Mock admin data
const adminData = {
  totalUsers: 12,
  students: 8,
  teachers: 3,
  pending: 1,

  users: [
    { id: 1, name: "Amit Sharma", role: "Student", status: "Active" },
    { id: 2, name: "Riya Singh", role: "Student", status: "Pending" },
    { id: 3, name: "Kunal Verma", role: "Teacher", status: "Active" },
    { id: 4, name: "Admin", role: "Admin", status: "Active" }
  ]
};

// Populate KPIs
document.getElementById("totalUsers").innerText = adminData.totalUsers;
document.getElementById("totalStudents").innerText = adminData.students;
document.getElementById("totalTeachers").innerText = adminData.teachers;
document.getElementById("pendingCount").innerText = adminData.pending;

// Populate table
const table = document.getElementById("userTable");

adminData.users.forEach((u, index) => {
  table.innerHTML += `
    <tr>
      <td>${u.name}</td>
      <td>${u.role}</td>
      <td>${u.status}</td>
      <td>
        <select onchange="changeRole(${index}, this.value)">
          <option value="">-- Select --</option>
          <option value="Student">Student</option>
          <option value="Teacher">Teacher</option>
          <option value="Admin">Admin</option>
        </select>
      </td>
      <td>
        ${u.status === "Pending" 
          ? `<button onclick="approveUser(${index})">Approve</button>` 
          : `<button onclick="disableUser(${index})">Disable</button>`}
      </td>
    </tr>
  `;
});

// Approve user
function approveUser(index) {
  adminData.users[index].status = "Active";
  alert("User approved (mock)");
  console.log("Approved:", adminData.users[index]);
  location.reload();
}

// Disable user
function disableUser(index) {
  alert("User disabled (mock)");
  console.log("Disabled:", adminData.users[index]);
}

// Change role
function changeRole(index, newRole) {
  if (!newRole) return;
  adminData.users[index].role = newRole;
  alert("Role updated (mock)");
  console.log("Role changed:", adminData.users[index]);
}
