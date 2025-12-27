// Mock student data (CSV-backed later)
const studentData = {
  name: "Amit Sharma",
  attendance: 86,
  subjects: {
    Math: 78,
    Science: 85,
    English: 74,
    Computer: 92,
    DBMS: 88
  },
  monthlyTrend: [72, 75, 78, 80, 83, 85]
};

// Calculations
const scores = Object.values(studentData.subjects);
const total = scores.reduce((a, b) => a + b, 0);
const average = (total / scores.length).toFixed(1);

let grade = "C";
if (average >= 85) grade = "A";
else if (average >= 70) grade = "B";

// Populate KPIs
document.getElementById("totalScore").innerText = total;
document.getElementById("averageScore").innerText = average;
document.getElementById("attendance").innerText = studentData.attendance + "%";
document.getElementById("grade").innerText = grade;

// Subject-wise bar chart
new Chart(document.getElementById("marksChart"), {
  type: "bar",
  data: {
    labels: Object.keys(studentData.subjects),
    datasets: [{
      label: "Marks",
      data: scores,
      borderWidth: 1
    }]
  },
  options: {
    scales: {
      y: { beginAtZero: true, max: 100 }
    }
  }
});

// Performance trend line chart
new Chart(document.getElementById("trendChart"), {
  type: "line",
  data: {
    labels: ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
    datasets: [{
      label: "Average Score",
      data: studentData.monthlyTrend,
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
