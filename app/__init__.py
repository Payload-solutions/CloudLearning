from flask import Flask
from flask_sqlalchemy import SQLAlchemy
# from app.models.streptococcus_regression
from flask_cors import CORS

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root_payload:@localhost/DeepTraining"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
CORS(app)

from app import routes