from functools import wraps
from flask import session, redirect, jsonify

def require_login(f):
    """Vérifie que l'utilisateur est connecté"""
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if "user" not in session:
            return jsonify({"message": "Authentication required"}), 401
        return f(*args, **kwargs)
    return decorated_function

def require_role(*roles):
    """Vérifie que l'utilisateur a l'un des rôles spécifiés"""
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            if "user" not in session:
                return jsonify({"message": "Authentication required"}), 401
            
            user_role = session["user"].get("role")
            if user_role not in roles:
                return jsonify({"message": "Access denied. Required roles: " + ", ".join(roles)}), 403
            
            return f(*args, **kwargs)
        return decorated_function
    return decorator
