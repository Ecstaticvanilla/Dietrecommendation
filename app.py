import streamlit as st

def app():
    st.success(f"Welcome, {st.session_state.username}!")
    st.title("🥗 Diet Recommendation")

def login():
    st.set_page_config(page_title="Diet App Login", page_icon="🍏", layout="centered")

    if 'logged_in' not in st.session_state:
        st.session_state.logged_in = False
    if 'username' not in st.session_state:
        st.session_state.username = ""

    if st.session_state.logged_in:
        app()
        st.divider()
        col1, col2, _ = st.columns([1, 1, 3])
        with col1:
            if st.button("🔒 Log Out"):
                st.session_state.logged_in = False
                st.session_state.username = ""
                st.rerun()
    else:
        st.title("🍏 Diet App Login")
        st.caption("Please enter your credentials to continue.")

        with st.container():
            username = st.text_input("Username")
            password = st.text_input("Password", type="password")

            col1, col2, _ = st.columns([1, 1, 3])
            with col1:
                login_clicked = st.button("Login")

            if login_clicked:
                if username == "Swayam" and password == "password":
                    st.session_state.logged_in = True
                    st.session_state.username = username
                    st.success("Login successful! Redirecting...")
                    st.rerun()
                else:
                    st.error("Invalid credentials, please try again.")

login()
