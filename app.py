from flask import Flask, render_template, request, jsonify
import json

app = Flask(__name__)

with open("materials.json") as f:
    materials = json.load(f)

with open("process.json") as f:
    process_steps = json.load(f)

@app.route("/")
def index():
    return render_template("index.html", materials=materials)

@app.route("/doping", methods=["POST"])
def doping():
    data = request.json
    material = data["material"]
    dtype = data["type"]

    if material == "Silicon":
        if dtype == "N":
            result = {
                "Base Material": "Silicon (Si) - 99.9999%",
                "Dopant": "Phosphorus (P) - 0.0001%"
            }
        else:
            result = {
                "Base Material": "Silicon (Si) - 99.9999%",
                "Dopant": "Boron (B) - 0.0001%"
            }
    else:
        result = {"Message": "Doping data not available"}

    return jsonify(result)

@app.route("/process")
def process():
    return jsonify(process_steps)

if __name__ == "__main__":
    app.run(debug=True)
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
