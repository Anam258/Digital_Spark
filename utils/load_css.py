# utils/load_css.py
import streamlit as st
import os

def load_local_css(file_name="styles.css"):
    with open(os.path.join("assets", file_name)) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)