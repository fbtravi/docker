# app.py
from flask import Flask
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/nocache")
def nocache():
    date = datetime.now()
    return str(date)

@app.route("/cache")
def cache():
    date = datetime.now()
    return str(date)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)
cç