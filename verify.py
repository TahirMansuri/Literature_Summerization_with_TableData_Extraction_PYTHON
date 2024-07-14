import flask
import PyPDF2
import numpy as np
import pandas as pd
import nltk
import summarizer
import pdfplumber
import sqlalchemy
import flask_login

print("Flask:", flask.__version__)
print("PyPDF2:", PyPDF2.__version__)
print("numpy:", np.__version__)
print("pandas:", pd.__version__)
print("nltk:", nltk.__version__)
print("summarizer:", summarizer.__version__)
print("pdfplumber:", pdfplumber.__version__)
print("SQLAlchemy:", sqlalchemy.__version__)
print("Flask-Login:", flask_login.__version__)
