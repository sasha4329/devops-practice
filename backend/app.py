from flask import Flask, jsonify
from flask_cors import CORS
import os
import psycopg2
from prometheus_flask_exporter import PrometheusMetrics

app = Flask(__name__)
CORS(app)

# 1. Инициализация метрик Prometheus
metrics = PrometheusMetrics(app, path='/api/metrics')
metrics.info('app_info', 'Application info', version='1.0.0')

USER = os.environ.get("STUDENT_ID", "XX")

@app.route("/api/hello", methods=["GET"])
def hello():
    return jsonify({
        "message": f"Hello from student red{USER}!",
        "student": f"red{USER}",
        "status": "ok"
    })

# 2. Правильный и готовый эндпоинт здоровья для ворот качества
@app.route('/api/health', methods=['GET'])
def health():
    return jsonify({"status": "healthy"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
