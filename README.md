# Secure Login & Fuzzy Search Dictionary

This is a simple web application built using Flask that provides a secure login system and a fuzzy search dictionary.

## Features
- Secure login and logout functionality.
- Dictionary search with fuzzy matching using difflib.
- Suggestions for similar words if no exact match is found.

## Installation

1. Clone the repository:
```bash
git clone https://github.com/poojatalele/fuzzy-dictionary.git
cd fuzzy-dictionary
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

3. Install the required packages:
```bash
pip install -r requirements.txt
```

4. Ensure `dictionary.json` exists and contains valid word-meaning pairs in JSON format.

## Running the Application

1. Start the Flask application:
```bash
python backend/app.py
```

2. Open your browser and go to:
```
http://127.0.0.1:5000
```

## API Endpoints

### 1. **Login**
- **Endpoint:** `/login`
- **Method:** `GET | POST`
- **Description:** Allows users to log in using username and password.
- **Example Request:**
```bash
POST /login
{
  "username": "admin",
  "password": "password123"
}
```
- **Response:**
```
Redirect to /main on success.
Shows error message on failure.
```

### 2. **Main Page**
- **Endpoint:** `/main`
- **Method:** `GET | POST`
- **Description:** Provides the search functionality for the dictionary. Requires authentication.
- **Example Request:**
```bash
POST /main
{
  "word": "example"
}
```
- **Responses:**
- Exact Match: `Exact match found: example - Definition`
- Suggestions: `Did you mean: word1, word2, word3?`
- No Match: `No match found.`

### 3. **Logout**
- **Endpoint:** `/logout`
- **Method:** `GET`
- **Description:** Logs the user out and redirects to the login page.

## Notes
- Default credentials: 
  - **Username:** `admin`
  - **Password:** `password123`
- The dictionary is loaded from `dictionary.json`. Ensure it follows the correct format.