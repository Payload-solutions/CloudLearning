from flask import Flask
# from app.models.streptococcus_regression
from flask_cors import CORS
from app.models.neuron_classification import NeuronClassification

NeuronClassification(epochs_number=1000,
                    input_shape_val=9,
                    output_shape_val=3)




app = Flask(__name__)
# app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root_payload:@localhost/DeepTraining"
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# db = SQLAlchemy(app)
CORS(app)


# import features
from app import routes
