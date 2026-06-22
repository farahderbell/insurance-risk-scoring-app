from flask import Flask, render_template, redirect, session
from routes.auth import auth_bp
from flask_cors import CORS



app = Flask(__name__)
app.secret_key = "secret"

app.register_blueprint(auth_bp)

CORS(app, supports_credentials=True)

@app.route("/")
def index():
    return redirect("/login")

@app.route("/login")
def login_page():
    return render_template("login.html")

@app.route("/home")
def home():
    if "user" not in session:
        return redirect("/login")
    return render_template("home.html", user=session["user"])

@app.route("/test-db")
def test_db():
    from db import get_connection

    try:
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT 'OK DB Maghrebia' AS msg")
        result = cursor.fetchone()

        conn.close()
        return result["msg"]

    except Exception as e:
        return f"DB Error: {str(e)}"


if __name__ == "__main__":
    app.run(debug=True)