async function login(event) {
    event.preventDefault();
    const username = document.getElementById("username").value;
    const password = document.getElementById("password").value;
    const response = await fetch('/login', {
        method: 'POST',
        body: new URLSearchParams({ username, password }),
        headers: { 'Content-Type': 'application/x-www-form-urlencoded' }
    });
    if (response.ok) {
        window.location.href = '/main';
    } else {
        alert("Invalid credentials. Please try again.");
    }
}

async function logout() {
    await fetch('/logout');
    window.location.href = '/login';
}

async function searchWord() {
    const word = document.getElementById("searchWord").value;
    const response = await fetch('/main', {
        method: 'POST',
        body: JSON.stringify({ word }),
        headers: { 'Content-Type': 'application/json' }
    });

    const resultDiv = document.getElementById("result");
    if (response.ok) {
        const data = await response.json();
        if (data.match) {
            resultDiv.innerHTML = `Exact match found: <strong>${data.match}</strong> - ${data.meaning}`;
        } else if (data.suggestions) {
            resultDiv.innerHTML = `Did you mean: <strong>${data.suggestions.join(', ')}</strong>?`;
        }
    } else {
        resultDiv.innerHTML = "Error: Unable to search.";
    }
}

document.getElementById("loginForm")?.addEventListener('submit', login);
