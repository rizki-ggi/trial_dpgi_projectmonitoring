import streamlit as st
from streamlit_cookies_manager import CookiesManager

cookies = CookiesManager()

# Function to check the password
def check_password():
    # Check cookies for login status
    cookies.load()
    if "password_correct" in cookies and cookies["password_correct"] == "true":
        st.session_state["password_correct"] = True
        return True

    if "password_correct" not in st.session_state:
        st.session_state["password_correct"] = False

    if not st.session_state["password_correct"]:
        with st.form("login_form"):
            st.text_input("Password", type="password", key="password")
            submit_button = st.form_submit_button(label="Submit")

            if submit_button:
                if st.session_state["password"] == "ggi2025":
                    st.session_state["password_correct"] = True
                    # Set cookies to persist login status
                    cookies["password_correct"] = "true"
                    cookies.save()
                    st.experimental_rerun()  # Rerun to update state
                else:
                    st.error("Incorrect password.")

    return st.session_state["password_correct"]

# Function to sign out
def sign_out():
    st.session_state["password_correct"] = False
    # Clear cookies
    cookies["password_correct"] = "false"
    cookies.save()
