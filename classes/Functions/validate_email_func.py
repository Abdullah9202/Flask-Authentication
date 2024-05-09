import re
# My Files (Classes)
from classes.user_class import db, User

# Function to validate the entered emails
def validate_email(email):
    # Regular expression for validating email addresses
    email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if not re.match(email_regex, email):
        return False  # Email format is invalid
    # Checking if the email is already registered
    if db.session.query(User).filter_by(email=email).first():
        return False # Email Already Present        
    return True