import streamlit as st
from models.user import User
from backend.user_db import db  # our singleton DB class
from utils.load_css import load_local_css
load_local_css()

class UserManager:
    def sign_up_user(self, username, email, password):
        if db.get_user(email):
            return False, "Email already exists."
        new_user = User(username, email, password)
        db.add_user(new_user)
        return True, "🎉 Account created successfully!, Login Now for explore packages"

def show():
    st.subheader("Create an Account")

    username = st.text_input("Username")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")

    if st.button("Sign Up"):
        manager = UserManager()
        success, message = manager.sign_up_user(username, email, password)
        if success:
            st.success(message)
        else:
            st.warning(message)
