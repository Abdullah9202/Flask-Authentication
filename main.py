from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash, gen_salt
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


# Home Route
@app.route('/')
def home():
    return render_template("index.html")


# Register user Route
@app.route('/register', methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # Hashing and Salting the password
        hashed_Salted_Password = generate_password_hash(request.form.get("password"), method="pbkdf2:sha256", salt_length=8)
        # Registering the new user
        new_user = User(
            name=request.form.get("name"),
            email=request.form.get("email"),
            password=hashed_Salted_Password, # Storing the hashed + salted password in DB
        )
        # Check if the email is already registered
        if User.query.filter_by(email=new_user.email).first() is None:
            # Adding in DB
            db.session.add(new_user)
            db.session.commit()
            # Returning the secret page in case of success
            return redirect(url_for("secrets"))
        else:
            flash("This email is already registered", "error")
    return render_template("register.html")


# Login user Route
@app.route('/login', methods=["GET", "POST"])
def login():
    form = User()
    
    # Getting the user details
    email = request.form.get("email")
    password = request.form.get("password")

    # Checking if the email exists in DB
    if not User.query.filter_by(email=email).first():
        flash("Email does not exists", "error")
        return redirect(url_for("login.html"))

    # Getting the hashed and salted password from DB
    hashed_Salted_Password = User.query.filter_by(email=email).get("password")

    # Checking if the password is incorrect
    if not check_password_hash(hashed_Salted_Password, password):
        flash("Incorrect password", "error")
        return redirect(url_for("login.html"))
    
    # Rendering the login page in case of success
    return render_template("login.html", form=form)


# Secrets Route
@app.route('/secrets')
def secrets():
    return render_template("secrets.html")


# Logout Route
@app.route('/logout')
def logout():
    pass


# Download Route
@app.route('/download')
def download():
    return send_from_directory('static', "files/cheat_sheet.pdf", as_attachment=True)


# Executing as script
if __name__ == "__main__":
    # Line below only required once, when creating DB. 
    with app.app_context():
        db.create_all()
    app.run(debug=True, host="127.0.0.1", port="8080")
