import { apiFetch } from "./api.js";

const token = sessionStorage.getItem("access_token");
const role = sessionStorage.getItem("role");

if (!token || role !== "admin") {
  window.location.href = "login.html";
}

const table = document.getElementById("userTable");
let users = [];

async function loadUsers() {
  try {
    users = await apiFetch("/admin/users");
    renderUsers(users);
  } catch (err) {
    console.error(err);
    alert("Failed to load users");
  }
}

function renderUsers(list) {
  table.innerHTML = "";

  if (!list.length) {
    table.innerHTML =
      "<tr><td colspan='5'>No users found</td></tr>";
    return;
  }

  list.forEach(user => {
    let actions = "";

    if (user.status === "Pending") {
      actions = `
        <button onclick="approveUser(${user.id})">Approve</button>
        <button class="danger" onclick="rejectUser(${user.id})">Reject</button>
      `;
    }

    if (user.status === "Active") {
      actions = `
        <button class="warning" onclick="suspendUser(${user.id})">Suspend</button>
      `;
    }

    if (user.status === "Suspended") {
      actions = `
        <button onclick="activateUser(${user.id})">Reactivate</button>
      `;
    }

    if (user.status === "Rejected") {
      actions = `<span class="muted">Rejected</span>`;
    }

    const row = document.createElement("tr");
    row.innerHTML = `
      <td>${user.name}</td>
      <td>${user.username}</td>
      <td>${user.role}</td>
      <td>${user.status}</td>
      <td>${actions}</td>
    `;

    table.appendChild(row);
  });
}

async function approveUser(userId) {
  await updateUser(`/admin/users/${userId}/approve`);
}

async function rejectUser(userId) {
  await updateUser(`/admin/users/${userId}/reject`);
}

async function suspendUser(userId) {
  await updateUser(`/admin/users/${userId}/suspend`);
}

async function activateUser(userId) {
  await updateUser(`/admin/users/${userId}/activate`);
}

async function updateUser(endpoint) {
  try {
    await apiFetch(endpoint, { method: "PUT" });
    loadUsers();
  } catch (err) {
    console.error(err);
    alert("Action failed");
  }
}

function filterUsers() {
  const selectedRole = document.getElementById("roleFilter").value;

  if (selectedRole === "all") {
    renderUsers(users);
  } else {
    renderUsers(users.filter(u => u.role === selectedRole));
  }
}

loadUsers();
