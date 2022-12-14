#! C:\Users\ADMIN\AppData\Local\Programs\Python\Python310\python.exe

# save this as api.py
from flask import Flask
from flask_cors import CORS
from datetime import timedelta

app = Flask(__name__)

app.secret_key = "secret key"
app.config['PERMANENT_SESSION_LIFETIME'] =  timedelta(minutes=10)
CORS(app)