from flask import Blueprint, request, session
from services.auth_service import AuthService

auth_bp = Blueprint("auth", __name__)
service = AuthService()
@auth_bp.route("/signup", methods=["POST"])
def signup():
    data = request.get_json()

    user = service.register(
        data.get("username"),
        data.get("email"),
        data.get("password"),
        data.get("role")
    )

    # Auto-login after signup - store full user data
    session["user"] = {
        "id": user["id"],
        "username": user["username"],
        "email": user["email"],
        "role": user["role"]
    }
    return {"message": "User created and logged in", "user": session["user"]}

@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.get_json()

    user = service.login(
        email=data.get("email"),
        password=data.get("password")
    )

    if user:
        session["user"] = {
            "id": user["id"],
            "username": user["username"],
            "email": user["email"],
            "role": user["role"]
        }
        return {"message": "Login success", "user": session["user"]}

    return {"message": "Invalid credentials"}, 401

@auth_bp.route("/logout", methods=["POST", "GET"])
def logout():
    session.clear()
    # If it's a GET request (from template), redirect to login
    if request.method == "GET":
        from flask import redirect
        return redirect("/login")
    # If it's a POST request (API), return JSON
    return {"message": "Logged out successfully"}