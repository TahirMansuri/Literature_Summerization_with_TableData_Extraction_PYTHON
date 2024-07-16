from app.models import User
from flask_login import login_user

def perform_login(username, password):
    user = User.query.filter_by(username=username).first()
    if user and user.password == password:  # Simple password check for demonstration
        login_user(user)
        return True
    else:
        return False
