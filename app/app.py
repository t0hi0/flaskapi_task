import json

import flask
from flask import request

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route("/", methods=["GET"])
def home():
    # Return home page
    return dict(response="Hello. It's flask API for get json file and calculate sum of numbers. "
                         "Go to /add and try this: /add?file=/full/path/to/file.json. Json file structure: "
                         "{'numbers': [1,2,3,4]}"), 200


@app.route("/add", methods=["GET"])
def add_nums():
    # Get file path from request and try open file
    file_path = request.args["file"]
    try:
        with open(file_path) as f:
            file = json.load(f)
    except FileNotFoundError as e:
        return dict(error="File path Error", exception=str(e),
                    message="Review json file path and try again"), 400
    try:
        # Try calculate a sum of numbers and return result or error msg
        result = sum(file['numbers'])
        response = {"Sum of numbers is": result}
        return response, 200
    except Exception as e:
        return dict(error="Calculation Error", exception=str(e),
                    message="Review operation parameters, json file and try again"), 400


@app.errorhandler(404)
def page_not_found(error):
    return dict(response="Page does not exist. Go to /add and try this: "
                         "/add?file=/full/path/to/file.json"), 404


if __name__ == "__main__":
    app.run(host="0.0.0.0")
