from db import get_connection

class UserRepository:

    @staticmethod
    def create(username, email, password, role):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            INSERT INTO users (username, email, password, role)
            VALUES (%s, %s, %s, %s)
        """, (username, email, password, role))

        conn.commit()
        conn.close()

    @staticmethod
    def get_by_email(email):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM users WHERE email=%s", (email,))
        user = cursor.fetchone()

        conn.close()
        return user
    