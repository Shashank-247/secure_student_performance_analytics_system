import { apiFetch } from "./api.js";

document.addEventListener("DOMContentLoaded", () => {

  const loginTab = document.getElementById("loginTab");
  const registerTab = document.getElementById("registerTab");
  const loginForm = document.getElementById("loginForm");
  const registerForm = document.getElementById("registerForm");

  if (!loginTab || !registerTab || !loginForm || !registerForm) {
    console.error("Tab elements not found");
    return;
  }

  function showLogin() {
    loginForm.classList.add("active");
    registerForm.classList.remove("active");

    loginTab.classList.add("active");
    registerTab.classList.remove("active");
  }

  function showRegister() {
    registerForm.classList.add("active");
    loginForm.classList.remove("active");

    registerTab.classList.add("active");
    loginTab.classList.remove("active");
  }

  loginTab.addEventListener("click", showLogin);
  registerTab.addEventListener("click", showRegister);

  // LOGIN
  loginForm.addEventListener("submit", async (e) => {
    e.preventDefault();

    const username = document.getElementById("loginUsername").value.trim();
    const password = document.getElementById("loginPassword").value.trim();

    if (!username || !password) {
      alert("Please enter username and password");
      return;
    }

    try {
      const response = await fetch("http://127.0.0.1:8000/auth/login", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ username, password })
      });

      const data = await response.json();

      if (!response.ok) {
        alert(data.detail || "Login failed");
        return;
      }

      sessionStorage.setItem("access_token", data.access_token);
      sessionStorage.setItem("role", data.role);

      if (data.role === "student") {
        window.location.href = "dashboard-student.html";
      } else if (data.role === "teacher") {
        window.location.href = "dashboard-teacher.html";
      } else if (data.role === "admin") {
        window.location.href = "dashboard-admin.html";
      }

    } catch (err) {
      alert("Backend not reachable");
      console.error(err);
    }
  });

  // REGISTER (placeholder)
  registerForm.addEventListener("submit", (e) => {
    e.preventDefault();
    alert("Registration submitted. Await admin approval.");
  });

});
