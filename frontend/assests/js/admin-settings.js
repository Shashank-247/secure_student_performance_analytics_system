function saveSettings() {
  const settings = {
    registrationEnabled: document.getElementById("registrationToggle").checked,
    twoFactor: document.getElementById("twoFactor").checked,
    sessionTimeout: document.getElementById("sessionTimeout").value,
    passwordPolicy: {
      minLength: document.getElementById("minLength").value,
      uppercase: document.getElementById("uppercase").checked,
      numbers: document.getElementById("numbers").checked,
      special: document.getElementById("special").checked
    }
  };

  console.log("Saved Settings:", settings);
  alert("Settings saved successfully!");
}
