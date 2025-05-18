import streamlit as st

# Must be the very first command
st.set_page_config(
    page_title="Digital Spark",
    page_icon="assets/logo.svg",
    layout="centered"
)

# Imports
from utils.load_css import load_local_css
from app_pages import home, login, signup

# Load CSS
load_local_css()

# Initialize session state
if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False
if 'username' not in st.session_state:
    st.session_state['username'] = ""

# Sidebar logo
st.sidebar.image("assets/logo.svg", width=150)

# Show main app content
# If user is logged in, show dashboard directly
if st.session_state['logged_in']:
    import dashboard_main 
    dashboard_main.show()
else:
    # Show login/signup/home only if not logged in
    menu = ["Home", "Sign Up", "Login"]
    choice = st.sidebar.radio("Navigate", menu)

    if choice == "Home":
        home.show()
    elif choice == "Login":
        login.show()
    elif choice == "Sign Up":
        signup.show()