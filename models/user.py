# User class using OOP principles
class User:
    def __init__(self, username, email, password):
        # Initialize user with basic credentials
        self.username = username
        self.email = email
        self.password = password

    def check_password(self, password):
        # Compare input password with stored one
        return self.password == password
