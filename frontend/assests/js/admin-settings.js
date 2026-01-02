import { apiFetch } from "./api.js";

const token = sessionStorage.getItem("access_token");
const role = sessionStorage.getItem("role");

if (!token || role !== "admin") {
  window.location.href = "login.html";
}

async function loadSettings() {
  try {
    const settings = await apiFetch("/admin/settings");

    document.getElementById("registrationToggle").checked =
      settings.registration_enabled;

    document.getElementById("twoFactor").checked =
      settings.two_factor_enabled;

    document.getElementById("sessionTimeout").value =
      settings.session_timeout;

    document.getElementById("minLength").value =
      settings.password_policy.min_length;

    document.getElementById("uppercase").checked =
      settings.password_policy.uppercase;

    document.getElementById("numbers").checked =
      settings.password_policy.numbers;

    document.getElementById("special").checked =
      settings.password_policy.special;
  } catch (err) {
    console.error(err);
    alert("Failed to load settings");
  }
}

async function saveSettings() {
  const payload = {
    registration_enabled:
      document.getElementById("registrationToggle").checked,

    two_factor_enabled:
      document.getElementById("twoFactor").checked,

    session_timeout:
      Number(document.getElementById("sessionTimeout").value),

    password_policy: {
      min_length:
        Number(document.getElementById("minLength").value),
      uppercase:
        document.getElementById("uppercase").checked,
      numbers:
        document.getElementById("numbers").checked,
      special:
        document.getElementById("special").checked
    }
  };

  try {
    await apiFetch("/admin/settings", {
      method: "PUT",
      body: JSON.stringify(payload)
    });

    alert("Settings saved successfully");
  } catch (err) {
    console.error(err);
    alert("Failed to save settings");
  }
}

loadSettings();
