const logs = [
  {
    time: "2025-01-02 10:15:22",
    user: "admin",
    role: "Admin",
    event: "LOGIN",
    description: "Admin logged in successfully",
    ip: "192.168.1.10"
  },
  {
    time: "2025-01-02 10:20:01",
    user: "amit01",
    role: "Student",
    event: "LOGIN",
    description: "Student logged in",
    ip: "192.168.1.15"
  },
  {
    time: "2025-01-02 10:30:45",
    user: "admin",
    role: "Admin",
    event: "APPROVAL",
    description: "Approved student amit01",
    ip: "192.168.1.10"
  },
  {
    time: "2025-01-02 11:00:12",
    user: "neha_t",
    role: "Teacher",
    event: "UPDATE",
    description: "Updated marks for CS101",
    ip: "192.168.1.22"
  }
];

const table = document.getElementById("logTable");

function renderLogs(list) {
  table.innerHTML = "";

  list.forEach(log => {
    const row = document.createElement("tr");
    row.innerHTML = `
      <td>${log.time}</td>
      <td>${log.user}</td>
      <td>${log.role}</td>
      <td>${log.event}</td>
      <td>${log.description}</td>
      <td>${log.ip}</td>
    `;
    table.appendChild(row);
  });
}

function filterLogs() {
  const event = document.getElementById("eventFilter").value;

  if (event === "all") {
    renderLogs(logs);
  } else {
    const filtered = logs.filter(log => log.event === event);
    renderLogs(filtered);
  }
}

renderLogs(logs);
