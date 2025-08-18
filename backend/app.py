import os
from flask import Flask, request, jsonify
from flask_cors import CORS
import mysql.connector
from mysql.connector import errorcode
import bcrypt

DB_HOST = os.getenv("DB_HOST", "db")
DB_USER = os.getenv("DB_USER", "appuser")
DB_PASSWORD = os.getenv("DB_PASSWORD", "apppass")
DB_NAME = os.getenv("DB_NAME", "appdb")

def get_db():
    return mysql.connector.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME
    )

app = Flask(__name__)
CORS(app)

@app.route("/api/health", methods=["GET"])
def health():
    return jsonify({"status": "ok"}), 200

@app.route("/api/signup", methods=["POST"])
def signup():
    data = request.get_json() or {}
    email = data.get("email", "").strip().lower()
    password = data.get("password", "")

    if not email or not password:
        return jsonify({"error": "email and password required"}), 400

    try:
        cnx = get_db()
        cur = cnx.cursor(dictionary=True)
        cur.execute("SELECT id FROM users WHERE email=%s", (email,))
        if cur.fetchone():
            return jsonify({"error": "user already exists"}), 409

        pw_hash = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())
        cur.execute("INSERT INTO users (email, password_hash) VALUES (%s, %s)", (email, pw_hash))
        cnx.commit()
        return jsonify({"message": "signup successful"}), 201
    except mysql.connector.Error as err:
        return jsonify({"error": str(err)}), 500
    finally:
        try:
            cur.close()
            cnx.close()
        except Exception:
            pass

@app.route("/api/signin", methods=["POST"])
def signin():
    data = request.get_json() or {}
    email = data.get("email", "").strip().lower()
    password = data.get("password", "")

    if not email or not password:
        return jsonify({"error": "email and password required"}), 400

    try:
        cnx = get_db()
        cur = cnx.cursor(dictionary=True)
        cur.execute("SELECT id, password_hash FROM users WHERE email=%s", (email,))
        row = cur.fetchone()
        if not row or not bcrypt.checkpw(password.encode("utf-8"), row["password_hash"].encode("utf-8") if isinstance(row["password_hash"], str) else row["password_hash"]):
            return jsonify({"error": "invalid credentials"}), 401

        return jsonify({"message": "signin successful", "user_id": row["id"]}), 200
    except mysql.connector.Error as err:
        return jsonify({"error": str(err)}), 500
    finally:
        try:
            cur.close()
            cnx.close()
        except Exception:
            pass

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)