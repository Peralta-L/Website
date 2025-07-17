# Flask Login & Registration App

This is a simple Flask web application that allows users to register and log in with secure password hashing. The app demonstrates basic user authentication, password complexity checks, and the use of static and template files.

## Features

- User registration with password complexity requirements
- Secure password storage using `passlib` (SHA-256 hashing)
- User login with credential verification
- Simple navigation between login, registration, and main pages
- Custom CSS styling and support for static images

## Folder Structure

```
lab7_peralta_luis/
│
├── app.py                # Main Flask application
├── requirements.txt      # Python dependencies
├── info.txt              # Stores user credentials (hashed)
├── static/
│   ├── main.css          # CSS styles
│   └── image/            # (Optional) Images used by the app
└── templates/
    ├── question.html     # Password question page
    ├── login.html        # Login page
    ├── register.html     # Registration page
    └── lab6.html         # Main user page after login
```

## Setup & Installation

1. **Clone the repository:**
   ```sh
   git clone https://github.com/yourusername/your-repo-name.git
   cd your-repo-name
   ```

2. **Create and activate a virtual environment (recommended):**
   ```sh
   python -m venv .venv
   .\.venv\Scripts\activate   # On Windows
   # source .venv/bin/activate  # On Mac/Linux
   ```

3. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
   ```

4. **Run the application:**
   ```sh
   python app.py
   ```

5. **Open your browser and go to:**
   ```
   http://127.0.0.1:5000
   ```
## Dependencies

- Flask
- passlib

(See `requirements.txt` for exact versions.)

## License

This project is
