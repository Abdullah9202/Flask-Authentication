from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, current_user, logout_user
# My Files (Classes)
from classes.user_class import db, User
# My Files (Functions)
from Functions.user_load_func import login_manager, load_user

# Init Flask App
app = Flask(__name__)

# Config Flask App
app.config['SECRET_KEY'] = 'iwfL#R,3dWQE4DE#Dd'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Init Flask App with DB
db.init_app(app)

# Init the App with LoginManager
login_manager.init_app(app)

# Line below only required once, when creating DB. 
# db.create_all()


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/register')
def register():
    return render_template("register.html")


@app.route('/login', methods=["GET", "POST"])
def login():
    form = User()
    # Validating the form
    if form.validate_on_submit():
        # Getting the user details
        email = form.email.data
        password = form.password.data
        # Fetching the user from DB
        user = db.session.query(User).filter_by(email=email)
        # Validation for user
        if user:
            # Checking the password
            if check_password_hash(user.password, password):
                # Logging the user in
                login_user(user)
                # Redirecting the user in case of success
                return redirect(url_for("secrets"))
            else:
                return flash("Invalid email or password", "error")
        else:
            return flash("Invalid email or password", "error")
    return render_template("login.html")


@app.route('/secrets')
def secrets():
    return render_template("secrets.html")


@app.route('/logout')
def logout():
    pass


@app.route('/download')
def download():
    pass


# Executing as script
if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port="8080")
