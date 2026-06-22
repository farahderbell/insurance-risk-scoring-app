import hashlib
from entities import user
from repositories.user_repository import UserRepository

class AuthService:

    def __init__(self):
        self.repo = UserRepository()

    def register(self, username, email, password, role):
        hashed = hashlib.sha256(password.encode()).hexdigest()
        self.repo.create(username, email, hashed, role)

    def login(self, email, password):
        hashed = hashlib.sha256(password.encode()).hexdigest()
        user = self.repo.get_by_email(email)

        if user and user["password"] == hashed:
            return user
        return None