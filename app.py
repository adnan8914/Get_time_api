from flask import Flask, jsonify
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"message": "Flask is running"})

@app.route('/time')
def get_time():
    now = datetime.utcnow()
    return jsonify({
        "current_time": now.strftime("%Y-%m-%d %H:%M:%S UTC")
    })
