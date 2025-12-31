// API IMPORT
import { apiFetch } from "./api.js";

// AUTH GUARD

const token = sessionStorage.getItem("access_token");
const role = sessionStorage.getItem("role");

if (!token || role !== "student") {
  window.location.href = "login.html";
}

// LOAD PERFORMANCE

async function loadStudentPerformance() {
  try {
    const data = await apiFetch("/student/performance");

    const scores = Object.values(data.subjects);
    const total = scores.reduce((a, b) => a + b, 0);
    const average = (total / scores.length).toFixed(1);

    let grade = "C";
    if (average >= 85) grade = "A";
    else if (average >= 70) grade = "B";

    // Populate KPIs
    document.getElementById("totalScore").innerText = total;
    document.getElementById("averageScore").innerText = average;
    document.getElementById("attendance").innerText = data.attendance + "%";
    document.getElementById("grade").innerText = grade;

    renderMarksChart(data.subjects);
    renderTrendChart(data.monthly_trend);

  } catch (error) {
    console.error("Performance load failed:", error);
    alert("Unable to load performance data");
  }
}

// CHARTS

function renderMarksChart(subjects) {
  new Chart(document.getElementById("marksChart"), {
    type: "bar",
    data: {
      labels: Object.keys(subjects),
      datasets: [{
        label: "Marks",
        data: Object.values(subjects),
        borderWidth: 1
      }]
    },
    options: {
      scales: {
        y: { beginAtZero: true, max: 100 }
      }
    }
  });
}

function renderTrendChart(trendData) {
  new Chart(document.getElementById("trendChart"), {
    type: "line",
    data: {
      labels: ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
      datasets: [{
        label: "Average Score",
        data: trendData,
        tension: 0.4,
        fill: false
      }]
    },
    options: {
      scales: {
        y: { beginAtZero: true, max: 100 }
      }
    }
  });
}

// INIT
loadStudentPerformance();
