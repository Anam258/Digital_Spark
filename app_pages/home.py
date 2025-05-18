import streamlit as st
import os

def local_css(file_name):
    with open(os.path.join("assets", file_name)) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("styles.css")

def show():
    # Hero Section
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        <div class='hero-left'>
            <h1>📈 Grow Your Brand Online</h1>
            <h4>Your Social Media, Fully Handled.</h4>
            <p><strong>Digital Spark</strong> helps small business owners & solo creators shine 
            with ready-to-post content, visual calendars, and payment-ready packages.</p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.image("assets/social_media.svg", use_container_width=True)

    st.markdown("---")

    # ✅ Services Section
    st.markdown("<div class='services-section'>", unsafe_allow_html=True)
    st.markdown("<h3 class='section-title'>🚀 Our Services</h3>", unsafe_allow_html=True)

    services = [
        {"icon": "📅", "title": "Monthly Theme Calendars", "desc": "Strategically planned content calendars every month."},
        {"icon": "✍️", "title": "Content That Converts", "desc": "Captivating captions, hooks & CTAs to boost engagement."},
        {"icon": "🎨", "title": "Beautiful Post Templates", "desc": "Eye-catching designs ready to customize and post."},
        {"icon": "💳", "title": "Simulated Payment System", "desc": "Practice real business scenarios with mock payments."},
    ]

    cols = st.columns(2)
    for i, service in enumerate(services):
        with cols[i % 2]:
            st.markdown(f"""
                <div class='service-card'>
                    <div class='service-icon'>{service["icon"]}</div>
                    <div class='service-content'>
                        <h4>{service["title"]}</h4>
                        <p>{service["desc"]}</p>
                    </div>
                </div>
            """, unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)

    # Benefits Section
    st.markdown("<div class='benefits-section'>", unsafe_allow_html=True)
    st.markdown("<h3 class='section-title'>✨ Why Choose Digital Spark?</h3>", unsafe_allow_html=True)

    benefits = [
    {"icon": "⚡", "title": "Save Hours Weekly", "desc": "No more struggling with daily post ideas – we give you a full calendar."},
    {"icon": "📊", "title": "Grow Faster", "desc": "Reach more people and build your brand with strategic posting."},
    {"icon": "💡", "title": "Stress-Free Content", "desc": "Professionally crafted templates & captions so you don’t overthink."},
    {"icon": "💰", "title": "Affordable Plans", "desc": "Simulated pricing options perfect for learners and new businesses."},
    ]

    cols = st.columns(2)
    for i, benefit in enumerate(benefits):
     with cols[i % 2]:
      st.markdown(f"""
     <div class='benefit-card'>
                <div class='benefit-icon'>{benefit["icon"]}</div>
                <div class='benefit-content'>
                    <h4>{benefit["title"]}</h4>
                    <p>{benefit["desc"]}</p>
                </div>
            </div>
        """, unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)

    # Testimonials Section
    st.markdown("<div class='testimonials-section'>", unsafe_allow_html=True)
    st.markdown("<h3 class='section-title'>💬 What Our Users Say</h3>", unsafe_allow_html=True)

    reviews = [
    {"avatar": "👩‍💼", "name": "Sara M.", "text": "Digital Spark helped me plan my entire month of content in a day! Absolute game changer."},
    {"avatar": "👨‍💻", "name": "Ali R.", "text": "I finally started posting consistently and saw real growth. Super easy to use too."},
    {"avatar": "👩‍🎨", "name": "Nida K.", "text": "The templates are beautiful and engaging. My page has never looked better!"},
              ]
    cols = st.columns(3)
    for i, review in enumerate(reviews):
       with cols[i]:
        st.markdown(f"""
            <div class='review-card'>
                <div class='avatar'>{review["avatar"]}</div>
                <h5>{review["name"]}</h5>
                <p class='review-text'>“{review["text"]}”</p>
            </div>
        """, unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)

    st.info("👈 Use the sidebar to Sign Up, Login, or explore packages!")
# Footer Section
    st.markdown("""
    <div class="footer">
        <p>© 2025 Digital Spark. All rights reserved.</p>
        <div class="footer-links">
            <a href="https://wa.me/923343452590" target="_blank">WhatsApp</a> |
            <a href="https://www.facebook.com/share/18jXsSgKSS/" target="_blank">Facebook</a> |
            <a href="#">Privacy Policy</a> |
            <a href="#">Terms of Service</a>
        </div>
    </div>
    """, unsafe_allow_html=True)


