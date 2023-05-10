from flask import Flask, request, jsonify, send_file, flash
import os
import requests

app = Flask(__name__)
app.secret_key = '123456'

@app.route("/", methods=["GET", "POST"])
def home():
    data = ['helloWorld']
    return jsonify(data)


if __name__ == "__main__":
    from waitress import serve
    serve(app, host="0.0.0.0", port=5000)