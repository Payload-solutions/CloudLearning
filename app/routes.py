from app import app
from flask import jsonify


@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "message": "working home!!"
    })


@app.route("/neuron", methos=["GET", "POST"])
def neuron_test():
    return "Something"
