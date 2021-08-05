from app import app
from flask import jsonify


@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "message": "working home!!"
    })


@app.route("/neuron", methods=["GET", "POST"])
def neuron_test():
    return "Something"


@app.route("/test", methods=["GET"])
def test_route():
    return jsonify({
        "data": [x for x in range(1, 10)]
    })
