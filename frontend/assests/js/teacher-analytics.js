// Mock class data (from CSV / DB later)
const classData = [
  { name: "Amit", avg: 85, attendance: 88 },
  { name: "Riya", avg: 72, attendance: 75 },
  { name: "Kunal", avg: 64, attendance: 68 },
  { name: "Neha", avg: 91, attendance: 92 }
];

// Calculations
const totalStudents = classData.length;

const avgScore =
  (classData.reduce((sum, s) => sum + s.avg, 0) / totalStudents).toFixed(1);

const avgAttendance =
  (classData.reduce((sum, s) => sum + s.attendance, 0) / totalStudents).toFixed(1);

const atRisk = classData.filter(
  s => s.avg < 65 || s.attendance < 75
).length;

// Populate KPIs
document.getElementById("classAvg").innerText = avgScore;
document.getElementById("classAttendance").innerText = avgAttendance + "%";
document.getElementById("atRiskCount").innerText = atRisk;
document.getElementById("totalStudents").innerText = totalStudents;

// Score distribution chart
new Chart(document.getElementById("scoreChart"), {
  type: "bar",
  data: {
    labels: classData.map(s => s.name),
    datasets: [{
      label: "Average Score",
      data: classData.map(s => s.avg),
      borderWidth: 1
    }]
  },
  options: {
    scales: {
      y: { beginAtZero: true, max: 100 }
    }
  }
});

// Attendance distribution chart
new Chart(document.getElementById("attendanceChart"), {
  type: "line",
  data: {
    labels: classData.map(s => s.name),
    datasets: [{
      label: "Attendance %",
      data: classData.map(s => s.attendance),
      tension: 0.4
    }]
  },
  options: {
    scales: {
      y: { beginAtZero: true, max: 100 }
    }
  }
});
