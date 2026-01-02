import { apiFetch } from "./api.js";

const token = sessionStorage.getItem("access_token");
const role = sessionStorage.getItem("role");

if (!token || role !== "teacher") {
  window.location.href = "login.html";
}

let classData = [];

async function loadTeacherAnalytics() {
  try {
    classData = await apiFetch("/teacher/analytics");

    const totalStudents = classData.length;

    const avgScore = (
      classData.reduce((sum, s) => sum + s.avg_score, 0) / totalStudents
    ).toFixed(1);

    const avgAttendance = (
      classData.reduce((sum, s) => sum + s.attendance, 0) / totalStudents
    ).toFixed(1);

    const atRisk = classData.filter(
      s => s.avg_score < 65 || s.attendance < 75
    ).length;

    document.getElementById("classAvg").innerText = avgScore;
    document.getElementById("classAttendance").innerText =
      avgAttendance + "%";
    document.getElementById("atRiskCount").innerText = atRisk;
    document.getElementById("totalStudents").innerText = totalStudents;

    renderCharts(classData);
  } catch (err) {
    console.error(err);
    alert("Failed to load analytics");
  }
}

function renderCharts(data) {
  new Chart(document.getElementById("scoreChart"), {
    type: "bar",
    data: {
      labels: data.map(s => s.name),
      datasets: [
        {
          label: "Average Score",
          data: data.map(s => s.avg_score),
          borderWidth: 1
        }
      ]
    },
    options: {
      scales: {
        y: { beginAtZero: true, max: 100 }
      }
    }
  });

  new Chart(document.getElementById("attendanceChart"), {
    type: "line",
    data: {
      labels: data.map(s => s.name),
      datasets: [
        {
          label: "Attendance %",
          data: data.map(s => s.attendance),
          tension: 0.4
        }
      ]
    },
    options: {
      scales: {
        y: { beginAtZero: true, max: 100 }
      }
    }
  });
}

loadTeacherAnalytics();
