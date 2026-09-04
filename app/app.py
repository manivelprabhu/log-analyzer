from flask import Flask, jsonify
from collections import Counter

app = Flask(__name__)

LOG_FILE = "sample.log"


@app.route("/")
def home():
    return "Prabhu - Log Analyzer App is running!"


@app.route("/analyze")
def analyze():
    try:
        with open(LOG_FILE, "r") as file:
            logs = file.readlines()

        levels = []

        for line in logs:
            parts = line.strip().split()

            if len(parts) >= 3:
                levels.append(parts[2])

        count = Counter(levels)

        return jsonify({
            "total_logs": len(logs),
            "INFO": count.get("INFO", 0),
            "WARNING": count.get("WARNING", 0),
            "ERROR": count.get("ERROR", 0)
        })

    except FileNotFoundError:
        return jsonify({
            "error": "Log file not found"
        }), 404


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
