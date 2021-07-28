from flask import (
    Flask,
    jsonify
)


def create_app():
    app = Flask(__name__)

    # getting the configuration from the environment
    # app.config.from_object("config.DevelopmentConfig")

    @app.route("/", methods=["GET"])
    def home():
        return jsonify({
            "message": "working home!!"
        })

    return app


