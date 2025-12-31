import { apiFetch } from "./api.js";

const token = sessionStorage.getItem("access_token");
const role = sessionStorage.getItem("role");

if (!token || role !== "admin") {
  window.location.href = "login.html";
}

let users = [];

async function loadAdminDashboard() {
  try {
    const stats = await apiFetch("/admin/dashboard");
    users = await apiFetch("/admin/users");

    document.getElementById("totalUsers").innerText = stats.total_users;
    document.getElementById("totalStudents").innerText = stats.students;
    document.getElementById("totalTeachers").innerText = stats.teachers;
    document.getElementById("pendingCount").innerText = stats.pending;

    renderUserTable(users);
  } catch (err) {
    console.error(err);
    alert("Failed to load admin dashboard");
  }
}

function renderUserTable(data) {
  const table = document.getElementById("userTable");
  table.innerHTML = "";

  if (!data.length) {
    table.innerHTML =
      "<tr><td colspan='5'>No users found</td></tr>";
    return;
  }

  data.forEach(u => {
    table.innerHTML += `
      <tr>
        <td>${u.name}</td>
        <td>${u.role}</td>
        <td>${u.status}</td>
        <td>
          <select onchange="changeRole(${u.id}, this.value)">
            <option value="">-- Select --</option>
            <option value="student">Student</option>
            <option value="teacher">Teacher</option>
            <option value="admin">Admin</option>
          </select>
        </td>
        <td>
          ${
            u.status === "Pending"
              ? `<button onclick="approveUser(${u.id})">Approve</button>
                 <button onclick="rejectUser(${u.id})">Reject</button>`
              : `<button onclick="disableUser(${u.id})">Disable</button>`
          }
        </td>
      </tr>
    `;
  });
}

async function approveUser(userId) {
  try {
    await apiFetch(`/admin/users/${userId}/approve`, {
      method: "PUT"
    });
    loadAdminDashboard();
  } catch (err) {
    console.error(err);
    alert("Failed to approve user");
  }
}

async function rejectUser(userId) {
  try {
    await apiFetch(`/admin/users/${userId}/reject`, {
      method: "PUT"
    });
    loadAdminDashboard();
  } catch (err) {
    console.error(err);
    alert("Failed to reject user");
  }
}

async function disableUser(userId) {
  try {
    await apiFetch(`/admin/users/${userId}/disable`, {
      method: "PUT"
    });
    loadAdminDashboard();
  } catch (err) {
    console.error(err);
    alert("Failed to disable user");
  }
}

async function changeRole(userId, newRole) {
  if (!newRole) return;

  try {
    await apiFetch(`/admin/users/${userId}/role`, {
      method: "PUT",
      body: JSON.stringify({ role: newRole })
    });
    loadAdminDashboard();
  } catch (err) {
    console.error(err);
    alert("Failed to update role");
  }
}

loadAdminDashboard();
