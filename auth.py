import streamlit as st

# Function to check the password
def check_password():
    if "password_correct" not in st.session_state:
        st.session_state["password_correct"] = False

    # Check if already logged in through query params
    if "password_correct" not in st.session_state or not st.session_state["password_correct"]:
        query_params = st.experimental_get_query_params()
        if "logged_in" in query_params and query_params["logged_in"][0] == "true":
            st.session_state["password_correct"] = True
            return True

    if not st.session_state["password_correct"]:
        with st.form("login_form"):
            st.text_input("Password", type="password", key="password")
            submit_button = st.form_submit_button(label="Submit")

            if submit_button:
                if st.session_state["password"] == "ggi2025":
                    st.session_state["password_correct"] = True
                    # Set query parameter to persist login status
                    st.experimental_set_query_params(logged_in="true")
                    st.experimental_rerun()  # Rerun to update session state
                else:
                    st.error("Incorrect password.")

    return st.session_state["password_correct"]

# Function to sign out
def sign_out():
    st.session_state["password_correct"] = False
    # Clear the query parameters
    st.experimental_set_query_params()
