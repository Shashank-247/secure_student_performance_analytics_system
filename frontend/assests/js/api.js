const BASE_URL = "http://127.0.0.1:8000";

export async function apiFetch(endpoint, options = {}) {
  const token = sessionStorage.getItem("access_token");

  const res = await fetch(BASE_URL + endpoint, {
    headers: {
      "Content-Type": "application/json",
      ...(token && { Authorization: `Bearer ${token}` })
    },
    ...options
  });

  if (!res.ok) {
    if (res.status === 401) {
      sessionStorage.clear();
      window.location.href = "login.html";
    }
    throw new Error("API Error");
  }

  return res.json();
}
