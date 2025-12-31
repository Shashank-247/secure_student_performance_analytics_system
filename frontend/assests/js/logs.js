import { apiFetch } from "./api.js";

const token = sessionStorage.getItem("access_token");
const role = sessionStorage.getItem("role");

if (!token || role !== "admin") {
  window.location.href = "login.html";
}

const table = document.getElementById("logTable");
let logs = [];

async function loadLogs() {
  try {
    logs = await apiFetch("/admin/logs");
    renderLogs(logs);
  } catch (err) {
    console.error(err);
    alert("Failed to load system logs");
  }
}

function renderLogs(list) {
  table.innerHTML = "";

  if (!list.length) {
    table.innerHTML =
      "<tr><td colspan='6'>No logs available</td></tr>";
    return;
  }

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
  const selectedEvent =
    document.getElementById("eventFilter").value;

  if (selectedEvent === "all") {
    renderLogs(logs);
  } else {
    renderLogs(logs.filter(l => l.event === selectedEvent));
  }
}

loadLogs();
