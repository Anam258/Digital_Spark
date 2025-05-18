# content_tools.py

import streamlit as st

class ToolsSection:
    def __init__(self):
        self.tools = [
            {"icon": "🗓️", "title": "View Calendar", "desc": "See your themed monthly content calendar."},
            {"icon": "📄", "title": "Explore Templates", "desc": "Use ready-made post templates to boost your content."},
            {"icon": "📈", "title": "Performance Stats", "desc": "Analyze your content's performance and engagement."},
            {"icon": "⚙️", "title": "Customize Plan", "desc": "Adjust your package or content preferences."},
        ]

    def render(self):
        st.markdown("<div class='dashboard-tools'>", unsafe_allow_html=True)
        st.markdown("<h3 class='section-title'>✨ Your Tools</h3>", unsafe_allow_html=True)

        cols = st.columns(2)
        for i, tool in enumerate(self.tools):
            with cols[i % 2]:
                st.markdown(f"""
                    <div class='tool-card'>
                        <div class='tool-icon'>{tool["icon"]}</div>
                        <div class='tool-content'>
                            <h4>{tool["title"]}</h4>
                            <p>{tool["desc"]}</p>
                        </div>
                    </div>
                """, unsafe_allow_html=True)

        st.markdown("</div>", unsafe_allow_html=True)