# dashboard_main.py

import streamlit as st
from utils.load_css import load_local_css
from content_tools import ToolsSection
from packages import PackageSection
from payment import PaymentSection

def show():
    load_local_css()

    # Sign Out Button in Sidebar
    with st.sidebar:
        st.markdown("---")
        if st.button("🔒 Sign Out"):
            st.session_state['logged_in'] = False
            st.session_state['username'] = ""
            st.session_state['selected_plan'] = None
            st.session_state['selected_price'] = None
            st.session_state['show_payment'] = False
            st.rerun()

    # Dashboard Header
    st.markdown("<div class='dashboard-header'>", unsafe_allow_html=True)
    st.markdown(f"<h2>📊 Welcome, <span class='highlight-user'>{st.session_state['username']}</span>!</h2>", unsafe_allow_html=True)
    st.markdown("<p>Here you’ll find your content tools, templates, and performance insights.</p>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

    # Tools Section
    tools = ToolsSection()
    tools.render()

    # Package Section
    pkg_section = PackageSection()
    pkg_section.render_packages()

    # Payment Section
    payment = PaymentSection()
    payment.render()
