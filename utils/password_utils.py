# Import libs
import streamlit as st
import streamlit_authenticator as stauth

def pass_hash(password):
    hashed_password = stauth.Hasher([password]).generate()
    hashed_password = hashed_password[0]
    return hashed_password