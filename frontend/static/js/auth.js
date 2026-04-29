// auth.js — paste this in every page via <script src="auth.js">

// Get saved token
function getToken() {
  return localStorage.getItem('access_token');
}

// Get saved role
function getRole() {
  return localStorage.getItem('user_role');
}

// Check if logged in — redirect to login if not
function requireAuth() {
  if (!getToken()) {
    window.location.href = '/auth/login/';
  }
}

// Logout function
function doLogout() {
  const refresh = localStorage.getItem('refresh_token');
  fetch('http://localhost:8001/api/auth/logout/', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ refresh: refresh })
  });
  localStorage.removeItem('access_token');
  localStorage.removeItem('refresh_token');
  localStorage.removeItem('user_role');
  window.location.href = '/auth/login/';
}

// Make authenticated API call
async function apiCall(url, method = 'GET', body = null) {
  const headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer ' + getToken()
  };
  const options = { method, headers };
  if (body) options.body = JSON.stringify(body);
  const response = await fetch(url, options);
  if (response.status === 401) {
    window.location.href = '/auth/login/'; // token expired
  }
  return response.json();
}