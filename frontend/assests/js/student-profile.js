// API IMPORT
import { apiFetch } from "./api.js";

// AUTH GUARD

const token = sessionStorage.getItem("access_token");
const role = sessionStorage.getItem("role");

if (!token || role !== "student") {
  window.location.href = "login.html";
}

// LOAD PROFILE

async function loadStudentProfile() {
  try {
    const profile = await apiFetch("/student/profile");

    document.getElementById("name").innerText = profile.name;
    document.getElementById("roll").innerText = profile.roll;
    document.getElementById("email").innerText = profile.email;
    document.getElementById("age").innerText = profile.age;
    document.getElementById("course").innerText = profile.course;
    document.getElementById("semester").innerText = profile.semester;
    document.getElementById("batch").innerText = profile.batch;
    document.getElementById("status").innerText = profile.status;

  } catch (error) {
    console.error("Profile load failed:", error);
    alert("Unable to load student profile");
  }
}

// INIT
loadStudentProfile();
