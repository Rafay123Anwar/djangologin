 <h1 align="center">
    <img src="https://readme-typing-svg.herokuapp.com/?font=Righteous&size=35&center=true&vCenter=true&width=600&height=70&duration=6000&lines=Django+Authentication+System+🛡️" />
  </h1>
  <h3 align="center">A simple, secure Django authentication solution.</h3>

  <div class="section">
    <h2>✨ Features</h2>
    <ul>
      <li><strong>User Registration</strong>: Validate unique usernames and phone numbers. Password confirmation included.</li>
      <li><strong>User Login</strong>: Authenticate users with valid credentials, display errors for invalid attempts.</li>
      <li><strong>Forgot Password</strong>: Recover credentials using the registered phone number.</li>
    </ul>
  </div>
   <br>  
     
<div align="center"> 
  <!-- 동적 뱃지 --> 
  <div style="display: flex; justify-content: center; align-items: flex-end;">
    <img src="https://techstack-generator.vercel.app/python-icon.svg" alt="icon" width="65" height="65" />
    <img src="https://techstack-generator.vercel.app/django-icon.svg" alt="icon" width="65" height="65" />
    <img src="https://techstack-generator.vercel.app/mysql-icon.svg" alt="icon" width="65" height="65">
    <img src="https://techstack-generator.vercel.app/github-icon.svg" alt="icon" width="65" height="65" />
  </div>
</div>
<br>


## Setup Instructions ⚙️

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/django-authentication-system.git
cd django-authentication-system
```

### 2. Set Up Virtual Environment

```bash
python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Start the Development Server

```bash
python manage.py runserver
```

### 6. Access the Application

Open your browser and visit: [Login Page](https://login-lac-psi-76.vercel.app/)

---

## File Structure 📂

```plaintext
django-authentication-system/
├── authentication/      # Django app containing views, models, and templates
│   ├── views.py          # Contains login, registration, and password recovery logic
│   ├── models.py         # User model for database storage
│   └── templates/        # HTML templates for the app
├── manage.py             # Django management script
├── db.sqlite3            # Default SQLite database (auto-generated)
└── requirements.txt      # Python dependencies
```

---

## How It Works 🔑

### User Registration

1. Users enter their username, phone number, password, and confirm password.
2. If the username or phone number already exists, an error is displayed.
3. On success, the user is redirected to the login page.

### User Login

1. Users enter their username and password.
2. The system verifies credentials and renders the result page for successful login.
3. Invalid credentials trigger an error message.

### Forgot Password

1. Users enter their registered phone number.
2. If found, the associated username and password are displayed.


---


## Contributions 🤝

Feel free to fork this repository and create pull requests for any features or fixes. Contributions are welcome!

---

## License 📝

This project is open-source and available under the MIT License.
```

Save this content in the `README.md` file in your project directory, and it will be ready to display as documentation on GitHub or any markdown-supported platform!
