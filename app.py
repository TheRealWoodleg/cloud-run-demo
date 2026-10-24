import logging
from flask import Flask, jsonify

app = Flask(__name__)
logging.basicConfig(level=logging.INFO)

@app.route("/")
def home():
    return jsonify(message="Hello from Cloud Run", version="v1")

@app.route("/health")
def health():
    return "ok", 200

@app.route("/boom")
def boom():
    logging.error("Simulated failure in /boom")
    raise RuntimeError("Simulated failure")
