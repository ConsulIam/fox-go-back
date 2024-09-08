import streamlit as st

st.header("Manager Account")
st.write(f"You are logged in as {st.session_state.role}.")
