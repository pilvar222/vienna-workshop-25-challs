#!/usr/bin/env python3
from flask import Flask, request, send_file, jsonify, abort
import os
import logging

app = Flask(__name__)

# Disable Flask logging for cleaner output
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

FLAG_DIRECTORY = "/app/flags"

@app.route('/')
def index():
    return """
    <h1>Flag Viewer Service</h1>
    <p>Welcome to our country flag viewing service!</p>
    <p>Use <code>/flag?country=&lt;3-letter-code&gt;</code> to view a country's flag.</p>
    <p>Example: <a href="/flag?country=USA">/flag?country=USA</a></p>
    <p>All country codes must be exactly 3 characters long for security reasons.</p>
    <br>
    <p><small>Available countries: USA, GBR, FRA, DEU, JPN, CAN, AUS, etc.</small></p>
    """

@app.route('/flag')
def get_flag():
    country = request.args.get('country', '')
    
    if not country:
        return jsonify({"error": "Please provide a country parameter"}), 400
    
    # Security check: only allow 3-character country codes
    if len(country) != 3:
        return jsonify({
            "error": f"Country code must be exactly 3 characters long. You provided {len(country)} characters.",
            "provided": country,
            "hint": "Try a standard 3-letter country code like USA, GBR, FRA..."
        }), 400
    
    # Normalize to uppercase for consistency
    country_upper = country.upper()
    
    # Construct file path - be careful about directory traversal!
    if '..' in country_upper or '/' in country_upper:
        return jsonify({"error": "Invalid characters in country code"}), 400
    
    flag_path = os.path.join(FLAG_DIRECTORY, f"{country_upper}.svg")
    
    # Check if file exists and serve it
    if os.path.exists(flag_path):
        return send_file(flag_path, mimetype='image/svg+xml')
    else:
        return jsonify({
            "error": f"Flag not found for country: {country_upper}",
            "path_checked": flag_path
        }), 404

@app.route('/health')
def health():
    return jsonify({"status": "healthy", "flags_available": len(os.listdir(FLAG_DIRECTORY))})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9010, debug=False) 