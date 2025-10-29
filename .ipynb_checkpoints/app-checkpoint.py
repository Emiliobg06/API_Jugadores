from flask import Flask, jsonify
import json

app = Flask(__name__)

# Load your JSON from file
with open("nationali.json", "r", encoding="utf-8") as f:
    report = json.load(f)

@app.route("/")
def home():
    return "Welcome to the Nationality Report API!"

@app.route("/report")
def get_report():
    return jsonify(report)

@app.route("/nationalities")
def get_nationalities():
    return jsonify(report.get("nationalities", []))

@app.route("/top/<int:n>")
def get_top_n(n):
    top_n = sorted(report["nationalities"], key=lambda x: x["playerCount"], reverse=True)[:n]
    return jsonify(top_n)

if __name__ == "__main__":
    app.run(debug=True, port=5000)