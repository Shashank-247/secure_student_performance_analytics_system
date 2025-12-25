// Mock student data (from CSV structure)
const student = {
  name: "Amit Sharma",
  total_score: 412,
  grade: "A",
  attendance: 86,
  weekly_study_hours: 12,
  fees_status: "Paid",
  subjects: {
    English: 78,
    Hindi: 82,
    Maths: 90,
    Science: 85,
    SST: 77
  }
};

// Populate text fields
document.getElementById("studentName").innerText = student.name;
document.getElementById("totalScore").innerText = student.total_score;
document.getElementById("grade").innerText = student.grade;
document.getElementById("attendance").innerText = student.attendance + "%";
document.getElementById("studyHours").innerText = student.weekly_study_hours + " hrs";
document.getElementById("feesStatus").innerText = student.fees_status;

// Populate table
const tableBody = document.getElementById("marksTable");
Object.entries(student.subjects).forEach(([subject, marks]) => {
  const row = `<tr><td>${subject}</td><td>${marks}</td></tr>`;
  tableBody.innerHTML += row;
});

// Chart
const ctx = document.getElementById("marksChart").getContext("2d");

new Chart(ctx, {
  type: "bar",
  data: {
    labels: Object.keys(student.subjects),
    datasets: [{
      label: "Marks",
      data: Object.values(student.subjects),
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
