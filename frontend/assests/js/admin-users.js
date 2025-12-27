const users = [
  {
    name: "Amit Sharma",
    username: "amit01",
    role: "student",
    status: "Pending"
  },
  {
    name: "Neha Verma",
    username: "neha_t",
    role: "teacher",
    status: "Active"
  },
  {
    name: "Rohit Kumar",
    username: "rohit22",
    role: "student",
    status: "Suspended"
  }
];

const table = document.getElementById("userTable");

/* Render Users */
function renderUsers(list) {
  table.innerHTML = "";

  list.forEach((user, index) => {
    const row = document.createElement("tr");

    let actions = "";

    if (user.status === "Pending") {
      actions = `
        <button onclick="approveUser(${index})">Approve</button>
        <button class="danger" onclick="rejectUser(${index})">Reject</button>
      `;
    }

    if (user.status === "Active") {
      actions = `
        <button class="warning" onclick="suspendUser(${index})">Suspend</button>
      `;
    }

    if (user.status === "Suspended") {
      actions = `
        <button onclick="activateUser(${index})">Reactivate</button>
      `;
    }

    if (user.status === "Rejected") {
      actions = `<span class="muted">Rejected</span>`;
    }

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

/* User Actions */
function approveUser(index) {
  users[index].status = "Active";
  renderUsers(users);
}

function rejectUser(index) {
  users[index].status = "Rejected";
  renderUsers(users);
}

function suspendUser(index) {
  users[index].status = "Suspended";
  renderUsers(users);
}

function activateUser(index) {
  users[index].status = "Active";
  renderUsers(users);
}

/* Filter by Role */
function filterUsers() {
  const role = document.getElementById("roleFilter").value;

  if (role === "all") {
    renderUsers(users);
  } else {
    const filtered = users.filter(user => user.role === role);
    renderUsers(filtered);
  }
}

/* Initial Load */
renderUsers(users);
