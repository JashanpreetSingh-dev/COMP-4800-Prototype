from flask import Flask
import requests


app = Flask(__name__)

@app.route("/")
def hello_world():
    return f"<p>Hello, World!</p>"
