# Flask Authentication System

This repository contains files for a Flask-based authentication system.

## Files Included

1. `main.py`: This file contains the main Flask application code, including routes for home, register, login, secrets, logout, and download functionalities.

2. `user_load_func.py`: This file contains the user loader function for Flask-Login, which loads users from the database.

3. `user_class.py`: This file defines the User class for the SQLAlchemy database, including columns for id, email, password, and name.

4. `base.html`: This is the base HTML template file for the application, containing the overall structure, navigation bar, and flash messages.

5. `index.html`: This HTML file extends the base template and provides the content for the home page, including links to login and register.

6. `login.html`: This HTML file extends the base template and provides the content for the login page, including a form for users to enter their email and password.

7. `register.html`: This HTML file extends the base template and provides the content for the register page, including a form for users to register with their name, email, and password.

8. `secrets.html`: This HTML file extends the base template and provides the content for the secrets page, which is accessible only to logged-in users and displays a welcome message with the user's name and a link to download a file.

## Usage

To use this authentication system, follow these steps:

1. Clone the repository to your local machine.
2. Make sure you have Python and Flask installed.
3. Set up a virtual environment and install the required dependencies (`flask`, `flask_sqlalchemy`, `flask_login`).
4. Run the `main.py` file to start the Flask application.
5. Access the application through your web browser and navigate to the provided routes (e.g., home, login, register, secrets).
6. Register a new account, log in with your credentials, and access the secrets page.

## Credits

Developed By Abdullah Khurram <https://www.github.com/Abdullah9202>
