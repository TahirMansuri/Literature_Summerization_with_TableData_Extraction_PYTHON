import os
from datetime import datetime
from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from app.models import User, UploadHistory
from app import db
from flask import flash, redirect, url_for, request
from werkzeug.utils import secure_filename
from app.login_logic import perform_login
main = Blueprint('main', __name__)

# Allowed extensions for file uploads
ALLOWED_EXTENSIONS = {'pdf'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@main.route('/')
@main.route('/index')
def index():
    return render_template('index.html', title='Home')

@main.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # Get form data
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']

        # Create a new User instance
        new_user = User(username=username, email=email, password=password)

        # Add the new user to the database
        db.session.add(new_user)
        db.session.commit()

        return redirect(url_for('main.index'))  # Redirect to home page after registration

    return render_template('register.html', title='Register')

@main.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if perform_login(username, password):
            return redirect(url_for('main.dashboard'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
            return render_template('login.html', title='Login')
    return render_template('login.html', title='Login')

@main.route('/dashboard')
@login_required
def dashboard():
    # Retrieve the upload history for the current user
    history = UploadHistory.query.filter_by(user_id=current_user.id).all()
    return render_template('dashboard.html', title='Dashboard', history=history)


@main.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index'))


@main.route('/upload', methods=['POST'])
@login_required
def upload():
    if 'file' not in request.files:
        flash('No file part', 'danger')
        return redirect(url_for('main.dashboard'))

    file = request.files['file']
    if file.filename == '':
        flash('No selected file', 'danger')
        return redirect(url_for('main.dashboard'))

    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join('uploads/', filename))
        # Save upload info to the database if needed
        upload_history = UploadHistory(
            username=current_user.username,
            pdf_name=filename,
            date_uploaded=datetime.utcnow(),
            user_id=current_user.id
        )
        db.session.add(upload_history)
        db.session.commit()


        flash('File successfully uploaded', 'success')
        return redirect(url_for('main.dashboard'))

    flash('Invalid file type', 'danger')
    return redirect(url_for('main.dashboard'))
