# app.py
from datetime import datetime

from flask import Flask, request
from prometheus_flask_exporter import PrometheusMetrics


app = Flask(__name__)
metrics = PrometheusMetrics(app)

# static information as metric
metrics.info('app_info', 'Application info', version='1.0.3')

@app.route("/")
def main():
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
    app.run(host='0.0.0.0', port=8000)