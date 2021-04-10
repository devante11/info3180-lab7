from flask import Flask
from app.config import Config
from flask_wtf.csrf import CSRFProtect


UPLOAD_FOLDER = './app/static/uploads'

app = Flask(__name__)

csrf = CSRFProtect(app)

app.config.from_object(__name__)
filefolder = app.config['UPLOAD_FOLDER']

from app import views
