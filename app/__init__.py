from flask import Flask

# from app.models.streptococcus_regression
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

from app import routes