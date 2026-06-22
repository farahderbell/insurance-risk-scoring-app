from flask import Blueprint, request, session
from services.auth_service import AuthService

auth_bp = Blueprint("auth", __name__)
service = AuthService()
@auth_bp.route("/signup", methods=["POST"])
def signup():
    data = request.get_json()

    service.register(
        data.get("username"),
        data.get("email"),
        data.get("password"),
        data.get("role")
    )

    # Auto-login after signup
    session["user"] = data.get("username")
    return {"message": "User created and logged in"}

@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.get_json()

    user = service.login(
        email=data.get("email"),
        password=data.get("password")
    )

    if user:
        session["user"] = user.get("username")
        return {"message": "Login success"}

    return {"message": "Invalid credentials"}, 401