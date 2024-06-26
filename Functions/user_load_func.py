from flask_login import LoginManager
# My Files (Classes)
from classes.user_class import db, User

login_manager = LoginManager()

# User loader function
@login_manager.user_loader
def load_user(user_id):
    # return db.session.query(User).get(user_id) # Returning the user form DB using user_id
    return User.query.get(int(user_id))