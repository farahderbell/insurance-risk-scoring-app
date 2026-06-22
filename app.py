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
    
    user = session["user"]
    user_role = user.get("role")
    
    # Redirect to role-specific dashboard
    if user_role == "admin":
        return redirect("/dashboard/admin")
    elif user_role == "data_scientist":
        return redirect("/dashboard/data-scientist")
    elif user_role == "underwriter":
        return redirect("/dashboard/underwriter")
    else:
        # Default dashboard for other roles
        return render_template("home.html", user=user)

@app.route("/dashboard/admin")
def admin_dashboard():
    if "user" not in session:
        return redirect("/login")
    if session["user"].get("role") != "admin":
        return {"message": "Access denied"}, 403
    
    return render_template("dashboard/admin.html", user=session["user"])

@app.route("/dashboard/data-scientist")
def data_scientist_dashboard():
    if "user" not in session:
        return redirect("/login")
    if session["user"].get("role") != "data_scientist":
        return {"message": "Access denied"}, 403
    
    return render_template("dashboard/data-scientist.html", user=session["user"])

@app.route("/dashboard/underwriter")
def underwriter_dashboard():
    if "user" not in session:
        return redirect("/login")
    if session["user"].get("role") != "underwriter":
        return {"message": "Access denied"}, 403
    
    return render_template("dashboard/underwriter.html", user=session["user"])

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