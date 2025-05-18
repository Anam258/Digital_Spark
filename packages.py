import streamlit as st

class PackageSection:
    def __init__(self):
        self.packages = [
            {
                "name": "Basic",
                "price": 2000,
                "features": [
                    "5 Social Media Posts",
                    "Basic Content Calendar",
                    "1 Template Included",
                    "Email Support"
                ]
            },
            {
                "name": "Pro",
                "price": 5000,
                "features": [
                    "15 Social Media Posts",
                    "Advanced Calendar",
                    "5 Templates Included",
                    "Priority Support"
                ]
            },
            {
                "name": "Premium",
                "price": 10000,
                "features": [
                    "Unlimited Posts",
                    "Custom Calendar",
                    "All Templates Included",
                    "1-on-1 Strategy Session"
                ]
            }
        ]

    def render_packages(self):
        st.markdown("<div class='packages-section'>", unsafe_allow_html=True)
        st.markdown("<h3 class='section-title'>Choose Your Plan</h3>", unsafe_allow_html=True)

        cols = st.columns(3)
        for i, pkg in enumerate(self.packages):
            with cols[i]:
                html = f"""
<div class='package-box'>
    <h4>{pkg['name']} Plan</h4>
    <p><strong>Price:</strong> Rs {pkg['price']}</p>
    <ul>
        {''.join([f"<li>{feature}</li>" for feature in pkg['features']])}
    </ul>
</div>
"""
                st.markdown(html, unsafe_allow_html=True)

                if st.button(f"Choose {pkg['name']}", key=pkg['name']):
                    st.session_state['selected_plan'] = pkg['name']
                    st.session_state['selected_price'] = pkg['price']
                    st.session_state['show_payment'] = True

        st.markdown("</div>", unsafe_allow_html=True)
