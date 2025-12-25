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

/* Placeholder login logic */
document.getElementById("loginForm").addEventListener("submit", function (e) {
  e.preventDefault();

  const username = document.getElementById("loginUsername").value;
  const password = document.getElementById("loginPassword").value;

  // Later: replace with fetch() to Python backend
  console.log("Login:", username, password);

  // Example redirect
  window.location.href = "dashboard.html";
});

/* Placeholder register logic */
document.getElementById("registerForm").addEventListener("submit", function (e) {
  e.preventDefault();
  alert("Registration submitted. Await admin approval.");
});
