# Enhanced Literature Summarization with Table Data Extraction

This Flask web application allows users to upload PDF documents, extract text and table data, and receive summarized content.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your_username/LRProject2.git
   cd LRProject2
   
2. Install dependencies:

pip install -r requirements.txt
Ensure that you have Python 3.x installed on your system.

**Libraries and Dependencies**
The project requires the following Python libraries (with specified versions):

Flask==2.0.2
Flask-SQLAlchemy==3.0.1
Flask-Login==0.5.0
PyPDF2==1.26.0
numpy==1.21.1
pandas==1.3.1
nltk==3.6.2
summarizer==0.0.10
pdfplumber==0.5.29

## Running the Application
Set up your Flask application:

python run.py
Open your web browser and go to http://localhost:5000

## Features
- User registration and login
- PDF upload and content extraction (text and tables)
- Summarization of extracted content
- Project Structure
   app/: Contains the Flask application files.
   run.py: Python script to run the Flask application.
   verify.py: Script to verify installed libraries and versions.

## License
This project is licensed under the MIT License - see the LICENSE file for details.


### requirements.txt File

Create a `requirements.txt` file in the root directory of your project. It should list all the dependencies with their versions:

Flask==2.0.2
Flask-SQLAlchemy==3.0.1
Flask-Login==0.5.0
PyPDF2==1.26.0
numpy==1.21.1
pandas==1.3.1
nltk==3.6.2
summarizer==0.0.10
pdfplumber==0.5.29

### Git Commands to Push

After setting up the `README.md` and `requirements.txt` files, follow these commands to push your project to GitHub:

```bash
# Initialize Git repository
git init

# Add all files to staging area
git add .

# Commit the changes
git commit -m "Initial commit: Setting up Flask project for Enhanced Literature Summarization"

# Create a new repository on GitHub (if not already created)
# Use the following command to add your GitHub repository as the origin remote
git remote add origin https://github.com/your_username/LRProject2.git

# Push the changes to GitHub
git push -u origin master
