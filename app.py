from flask import Flask
from prometheus_client import Counter, generate_latest, CONTENT_TYPE_LATEST

app = Flask(__name__)
REQUESTS = Counter("http_requests_total", "Total HTTP requests", ["path"])

@app.route("/")
def index():
    REQUESTS.labels(path="/").inc()
    return "Hello DevOps v1 - Accessible sur 192.168.56.10:8080"

@app.route("/metrics")
def metrics():
    REQUESTS.labels(path="/metrics").inc()
    return generate_latest(), 200, {"Content-Type": CONTENT_TYPE_LATEST}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
