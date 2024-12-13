import streamlit as st
from streamlit_cookies_manager import CookieManager

# Inisialisasi CookieManager
cookies = CookieManager()

# Function to check the password
def check_password():
    # Sinkronisasi cookies dengan browser
    if not cookies.ready():
        st.stop()  # Berhenti hingga cookies siap digunakan

    # Periksa status login dari cookies
    if "password_correct" in cookies and cookies["password_correct"] == "true":
        st.session_state["password_correct"] = True
        return True

    # Jika tidak ada dalam session state, set default
    if "password_correct" not in st.session_state:
        st.session_state["password_correct"] = False

    # Tampilkan form login jika belum login
    if not st.session_state["password_correct"]:
        with st.form("login_form"):
            st.text_input("Password", type="password", key="password")
            submit_button = st.form_submit_button(label="Submit")

            if submit_button:
                if st.session_state["password"] == "ggi2025":
                    st.session_state["password_correct"] = True
                    # Simpan status login ke cookies
                    cookies["password_correct"] = "true"
                    cookies.save()  # Simpan cookies
                    st.experimental_rerun()  # Refresh halaman
                else:
                    st.error("Incorrect password.")

    return st.session_state["password_correct"]

# Function to sign out
def sign_out():
    st.session_state["password_correct"] = False
    # Hapus status login dari cookies
    cookies["password_correct"] = "false"
    cookies.save()
