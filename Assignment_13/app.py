from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Software E-Commerce ML Model is Running"

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    time_spent = data.get("time_spent", 0)
    pages_visited = data.get("pages_visited", 0)

    if time_spent > 10 and pages_visited > 5:
        result = "Will Buy Software"
    else:
        result = "Will Not Buy Software"

    return jsonify({"prediction": result})

if __name__ == "__main__":
    app.run(debug=True)

