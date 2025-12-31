// TAB SWITCHING

function showLogin() {
  document.getElementById("loginForm").classList.add("active");
  document.getElementById("registerForm").classList.remove("active");

  document.getElementById("loginTab").classList.add("active");
  document.getElementById("registerTab").classList.remove("active");
}

function showRegister() {
  document.getElementById("registerForm").classList.add("active");
  document.getElementById("loginForm").classList.remove("active");

  document.getElementById("registerTab").classList.add("active");
  document.getElementById("loginTab").classList.remove("active");
}

// LOGIN (FASTAPI INTEGRATION) 

document.getElementById("loginForm").addEventListener("submit", async function (e) {
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
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({
        username: username,
        password: password
      })
    });

    const data = await response.json();

    if (!response.ok) {
      alert(data.detail || "Login failed");
      return;
    }

    // Store JWT token & role
    sessionStorage.setItem("access_token", data.access_token);
    sessionStorage.setItem("role", data.role);

    // Redirect based on role
    if (data.role === "student") {
      window.location.href = "dashboard-student.html";
    } else if (data.role === "teacher") {
      window.location.href = "dashboard-teacher.html";
    } else if (data.role === "admin") {
      window.location.href = "dashboard-admin.html";
    } else {
      alert("Unknown user role");
    }

  } catch (error) {
    console.error("Login error:", error);
    alert("Unable to connect to backend server");
  }
});

// REGISTER (PLACEHOLDER)

document.getElementById("registerForm").addEventListener("submit", function (e) {
  e.preventDefault();
  alert("Registration submitted. Await admin approval.");
});
