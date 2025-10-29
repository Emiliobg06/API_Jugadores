from flask import Flask, jsonify
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)

with open("league_reports.json", "r", encoding="utf-8") as f:
    report = json.load(f)

@app.route("/")
def home():
    return "Welcome to the Nationality Report API!"

@app.route("/report")
def get_report():
    return jsonify(report)


if __name__ == "__main__":
    app.run(debug=True)