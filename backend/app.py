import os
import psycopg2
from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


def get_db_connection():
    return psycopg2.connect(
        host=os.environ.get("DB_HOST", "db"),
        database=os.environ.get("DB_NAME", "notes_db_03"),
        user=os.environ.get("DB_USER", "notes_user_03"),
        password=os.environ.get("DB_PASS", "password123")
    )


@app.route("/api/health", methods=["GET"])
def health():
    return jsonify({"status": "ok"})


@app.route("/api/hello", methods=["GET"])
def hello():
    return jsonify({"message": "Hello from backend"})


@app.route("/api/metrics", methods=["GET"])
def metrics():
    return jsonify({
        "service": "notes-backend",
        "status": "running"
    })


@app.route("/api/notes", methods=["GET"])
def get_notes():
    try:
        conn = get_db_connection()
        cur = conn.cursor()

        cur.execute("SELECT id, title, content FROM notes ORDER BY id DESC;")
        rows = cur.fetchall()

        cur.close()
        conn.close()

        notes = [
            {
                "id": row[0],
                "title": row[1],
                "content": row[2]
            }
            for row in rows
        ]

        return jsonify(notes)

    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/api/notes", methods=["POST"])
def create_note():
    try:
        data = request.get_json()

        title = data.get("title")
        content = data.get("content")

        if not title or not content:
            return jsonify({"error": "title and content are required"}), 400

        conn = get_db_connection()
        cur = conn.cursor()

        cur.execute(
            "INSERT INTO notes (title, content) VALUES (%s, %s);",
            (title, content)
        )

        conn.commit()
        cur.close()
        conn.close()

        return jsonify({"status": "created"}), 201

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
