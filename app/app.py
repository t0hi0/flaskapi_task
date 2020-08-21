from flask import Flask, request


app = Flask(__name__)
app.config["DEBUG"] = True
hello_message = dict(response="It's API for get json file and calculate sum of numbers. "
                              "Try send json file {'numbers': [1,2,3,4]} to /add.")


@app.route("/", methods=["GET", "POST"])
def home():
    # Return home page
    return hello_message, 200


@app.route("/add", methods=["GET", "POST"])
def add_nums():
    if request.method == 'POST':
        # Check for json data in request
        if request.data:
            # Get json data from request
            data = request.json
            try:
                # Try calculate a sum of numbers and return result or error msg
                result = sum(data['numbers'])
                response = {"Sum of numbers is": result}
                return response, 200
            except Exception as e:
                return dict(error="Calculation Error", exception=str(e),
                            message="Review operation parameters, json file and try again"), 400
        else:
            return dict(error="Check json file name or file existence and try again"), 400
    else:
        return hello_message, 405


@app.errorhandler(404)
def page_not_found(error):
    return dict(response="Page does not exist. Try send json file to /add"), 404


if __name__ == "__main__":
    app.run(host="0.0.0.0")
