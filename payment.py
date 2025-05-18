import streamlit as st

class PaymentSection:
    def render(self):
        if st.session_state.get('show_payment'):
            st.markdown("<div class='payment-section'>", unsafe_allow_html=True)
            st.markdown(f"<h3>Payment for {st.session_state['selected_plan']} Plan</h3>", unsafe_allow_html=True)
            st.markdown(f"<p><strong>Amount:</strong> Rs {st.session_state['selected_price']}</p>", unsafe_allow_html=True)

            payment_method = st.selectbox("Choose Payment Method", ["Easypaisa", "JazzCash", "Bank Transfer"])
            transaction_id = st.text_input("Enter Transaction ID")

            if st.button("Submit Payment"):
                if transaction_id.strip() == "":
                    st.error("Please enter a valid Transaction ID.")
                else:
                    st.success("Payment received! Your plan has been activated.")
                    # Reset payment state
                    st.session_state['show_payment'] = False

            st.markdown("</div>", unsafe_allow_html=True)
