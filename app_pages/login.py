import streamlit as st
from backend.user_db import db
from utils.load_css import load_local_css
import dashboard_main  

load_local_css()

def show():
    if 'login_success' not in st.session_state:
        st.session_state['login_success'] = False

    if st.session_state['login_success']:
        # Smooth welcome message
        st.success(f"Welcome back, {st.session_state['username']}!")
        with st.spinner("Loading your dashboard..."):
            st.sleep(1)  # Small delay for transition feel
        dashboard_main.show()
        return

    st.subheader("Login to Your Account")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        user = db.authenticate_user(email, password)
        if user:
            st.session_state['logged_in'] = True
            st.session_state['username'] = user.username
            st.session_state['login_success'] = True
            st.rerun()  # Refresh to trigger dashboard render
        else:
            st.error("Invalid email or password.")