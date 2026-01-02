// API IMPORT
import { apiFetch } from "./api.js";

// AUTH GUARD

const token = sessionStorage.getItem("access_token");
const role = sessionStorage.getItem("role");

if (!token || role !== "student") {
  window.location.href = "login.html";
}

// LOAD DASHBOARD DATA

async function loadStudentDashboard() {
  try {
    const student = await apiFetch("/student/dashboard");

    // Populate text fields
    document.getElementById("studentName").innerText = student.name;
    document.getElementById("totalScore").innerText = student.total_score;
    document.getElementById("grade").innerText = student.grade;
    document.getElementById("attendance").innerText = student.attendance + "%";
    document.getElementById("studyHours").innerText = student.weekly_study_hours + " hrs";
    document.getElementById("feesStatus").innerText = student.fees_status;

    // Populate marks table
    const tableBody = document.getElementById("marksTable");
    tableBody.innerHTML = "";

    Object.entries(student.subjects).forEach(([subject, marks]) => {
      const row = document.createElement("tr");
      row.innerHTML = `<td>${subject}</td><td>${marks}</td>`;
      tableBody.appendChild(row);
    });

    // Render chart
    renderMarksChart(student.subjects);

  } catch (error) {
    console.error("Dashboard load failed:", error);
    alert("Failed to load student dashboard data");
  }
}

// CHART FUNCTION

function renderMarksChart(subjects) {
  const ctx = document.getElementById("marksChart").getContext("2d");

  new Chart(ctx, {
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
      responsive: true,
      scales: {
        y: {
          beginAtZero: true,
          max: 100
        }
      }
    }
  });
}

// INIT

loadStudentDashboard();
