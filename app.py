from flask import Flask, jsonify
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"message": "Flask is running"})

@app.route('/time', methods=['GET', 'POST'])
def get_time():
    now = datetime.utcnow()
    return jsonify({
        "message": f"Today is {now.strftime('%A')}, and the current time is {now.strftime('%H:%M:%S UTC')}"
    })

