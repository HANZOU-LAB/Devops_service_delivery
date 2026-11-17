import os
from flask import Flask, jsonify

app = Flask(__name__)
VERSION = os.getenv("APP_VERSION", "v1.0.0")


@app.route('/')
def info():
    """Endpoint principal com informações sintéticas do serviço."""
    return jsonify({
        "service_name": "Internal Service Info Desk",
        "support_contact": "admin@internal.lab",
        "service_hours": "08:00 - 17:00 UTC",
        "version": VERSION
    }), 200


@app.route('/health')
def health():
    """Endpoint de monitorização automática de saúde."""
    return jsonify({"status": "broken"}), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
