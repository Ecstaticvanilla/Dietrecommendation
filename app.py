import streamlit as st


def app():
    st.write("Diet Recommendation")
def login():
    if 'logged_in' not in st.session_state:
        st.session_state.logged_in = False

    if st.session_state.logged_in:
        app()
        st.write(f"Welcome, {st.session_state.username}!")
        if st.button('Log Out'):
            st.session_state.logged_in = False
            st.session_state.username = ""
            st.rerun()  
    else:
        st.title("Login Page")
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        
        if st.button("Login"):
            if username == "admin" and password == "admin": 
                st.session_state.logged_in = True
                st.session_state.username = username
                st.rerun()  
            else:
                st.error("Invalid credentials, please try again.")
login()
