from flask import Flask, jsonify
from datetime import datetime, timedelta

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, Flask is running!"

@app.route('/current_time', methods=['GET'])
def current_time():
    now_utc = datetime.utcnow()
    ist_offset = timedelta(hours=5, minutes=30)
    now_ist = now_utc + ist_offset

    current_day = now_ist.strftime('%A')
    current_hour = now_ist.strftime('%H:%M:%S')  # Get current time in HH:MM:SS format
    current_date = now_ist.strftime('%Y-%m-%d')  # Get current date in YYYY-MM-DD format

    return jsonify({
        "Current_Date": current_date,
        "Current_Time": current_hour,
        "Current_Day": current_day
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
