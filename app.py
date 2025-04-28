from flask import Flask, jsonify, request
from datetime import datetime
import pytz

app = Flask(__name__)

API_TOKEN = "supersecrettoken123"

capital_timezones = {
    "Washington": "America/New_York",
    "London": "Europe/London",
    "Paris": "Europe/Paris",
    "Tokyo": "Asia/Tokyo",
    "Sydney": "Australia/Sydney"
}

def token_required(f):
    def decorator(*args, **kwargs):
        auth_header = request.headers.get('Authorization')
        if auth_header and auth_header.startswith("Bearer "):
            token = auth_header.split(" ")[1]
            if token == API_TOKEN:
                return f(*args, **kwargs)
        return jsonify({"error": "Unauthorized"}), 401
    decorator.__name__ = f.__name__
    return decorator

@app.route('/api/hello', methods=['GET'])
def hello():
    return jsonify({"message": "Hello, world!"})

@app.route('/api/secure-data', methods=['GET'])
@token_required
def secure_data():
    return jsonify({"secret": "This is protected info!"})

@app.route('/api/time', methods=['GET'])
@token_required
def get_time():
    capital = request.args.get('capital')
    if not capital:
        return jsonify({"error": "No capital city provided."}), 400
    
    tz_name = capital_timezones.get(capital)
    if not tz_name:
        return jsonify({"error": f"Capital city '{capital}' not found in database."}), 404
    
    tz = pytz.timezone(tz_name)
    local_time = datetime.now(tz)
    utc_offset = local_time.strftime('%z')
    utc_offset_formatted = f"UTC{utc_offset[:3]}:{utc_offset[3:]}"

    return jsonify({
        "capital": capital,
        "local_time": local_time.strftime('%Y-%m-%d %H:%M:%S'),
        "utc_offset": utc_offset_formatted
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
