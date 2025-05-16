from flask import Flask, jsonify
from datetime import datetime
import pytz

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    return "Flask is running"

@app.route("/check-enrollment", methods=["GET"])
def check_enrollment():
    # Get current time in IST
    ist = pytz.timezone('Asia/Kolkata')
    current_time = datetime.now(ist).time()

    start_time = datetime.strptime("10:00", "%H:%M").time()
    end_time = datetime.strptime("17:00", "%H:%M").time()

    # Check if current time is within range
    if start_time <= current_time <= end_time:
        return jsonify({"enrollment_open": True, "message": "Yes, it's time for enrollment."})
    else:
        return jsonify({"enrollment_open": False, "message": "No, enrollment is closed now."})

if __name__ == "__main__":
    app.run(debug=True)
