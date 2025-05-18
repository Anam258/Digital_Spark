# backend/user_db.py

from models.user import User

# Simulated in-memory "database"
class UserDatabase:
    def __init__(self):
        self.users = {}  # email -> User object

    def add_user(self, user: User):
        if user.email in self.users:
            return False  # user already exists
        self.users[user.email] = user
        return True

    def get_user(self, email):
        return self.users.get(email, None)

    def authenticate_user(self, email, password):
        user = self.get_user(email)
        if user and user.check_password(password):
            return user
        return None


# Singleton instance to simulate persistent DB
db = UserDatabase()
