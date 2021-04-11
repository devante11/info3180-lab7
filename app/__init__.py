from flask import Flask
from flask_wtf.csrf import CSRFProtect
from app.config import Config




app = Flask(__name__)
csrf = CSRFProtect(app)
app.config['UPLOAD_FOLDER'] = './app/static/uploads'
app.config.from_object(__name__)



from app import views
