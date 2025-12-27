// Mock student profile (DB later)
const studentProfile = {
  name: "Amit Sharma",
  roll: "BCA101",
  email: "amit.sharma@example.com",
  age: 20,
  course: "BCA",
  semester: "5",
  batch: "2022-2025",
  status: "Active"
};

// Populate profile
document.getElementById("name").innerText = studentProfile.name;
document.getElementById("roll").innerText = studentProfile.roll;
document.getElementById("email").innerText = studentProfile.email;
document.getElementById("age").innerText = studentProfile.age;
document.getElementById("course").innerText = studentProfile.course;
document.getElementById("semester").innerText = studentProfile.semester;
document.getElementById("batch").innerText = studentProfile.batch;
document.getElementById("status").innerText = studentProfile.status;
