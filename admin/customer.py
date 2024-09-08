import streamlit as st

pg = st.navigation(
    [st.Page("manage_account.py"), st.Page("create_account.py")], position="hidden"
)
pg.run()
