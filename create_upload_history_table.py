from app import create_app, db
from app.models import User, UploadHistory

# Create an instance of the Flask application
app = create_app()

# Push the application context
with app.app_context():
    # Create the UploadHistory table
    db.create_all()
