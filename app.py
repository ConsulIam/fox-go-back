# utf-8 encoded
# Import libs
import yaml
import streamlit as st
from yaml.loader import SafeLoader
import streamlit_authenticator as stauth
from streamlit_authenticator.utilities import (
    CredentialsError,
    ForgotError,
    Hasher,
    LoginError,
    RegisterError,
    ResetError,
    UpdateError,
)

# Page configs
st.set_page_config(
    page_title="Fox Go Back",
    page_icon="assets/img/fox_go_back_icon.png",
    layout="centered",
    initial_sidebar_state="auto",
    menu_items=None,
)

# Loading config file
with open(".streamlit/detal.yaml") as file:
    config = yaml.load(file, Loader=SafeLoader)

# Create the authenticator object
authenticator = stauth.Authenticate(
    config["credentials"],
    config["cookie"]["name"],
    config["cookie"]["key"],
    config["cookie"]["expiry_days"],
    config["pre-authorized"],
)

col1, col2 = st.columns([1, 3])
with col1:
    st.image("assets/img/fox_go_back_icon.png", use_column_width=True)
with col2:
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.title("FoxGoBack")

# Define role for session_state
if "role" not in st.session_state:
    st.session_state.role = None

def logout():
    st.session_state.role = None
    st.rerun()


def on_logout(arg):
    st.session_state.role = None
    page_dict = {}
    authentication_status = None
    pg = st.navigation({"Account": account_pages} | page_dict)
    pg.run()
    st.rerun()


# logout_page = st.Page(logout, title="Log out", icon=":material/logout:")
settings = st.Page("account/settings.py", title="Settings", icon=":material/settings:")
home = st.Page("account/home.py", title="Home", icon=":material/home:")

# Instance login form
name, authentication_status, username = authenticator.login(
    fields={
        "Form name": "Login",
        "Username": "Usuário",
        "Password": "Senha",
        "Login": "Fazer login",
    },
    location="main",
)

statistics = st.Page("company/statistics.py", title="Estatísticas", icon=":material/healing:")
customer = st.Page("company/customer.py", title="Clientes", icon=":material/healing:")
message = st.Page(
    "company/message.py", title="Mensagens", icon=":material/healing:"
)
admin = st.Page("admin/admin.py", title="Admin", icon=":material/person_add:")
register = st.Page("admin/register.py", title="Cadastro", icon=":material/settings:")

account_pages = [home, settings]
statistics_pages = [statistics]
company_pages = [customer, message]
admin_pages = [admin, register]
page_dict = {}

if st.session_state.role in [0, 1]:
    page_dict["Estatísticas"] = statistics_pages
if st.session_state.role in [2, 1, 0]:
    page_dict["Estabelecimento"] = company_pages
if st.session_state.role == 0:
    page_dict["Admin"] = admin_pages

if authentication_status:
    authenticator.logout(button_name="Sair", location="main", callback=on_logout)
    user_info = config["credentials"]["usernames"].get(username, {})
    user_role = user_info.get("role")
    st.session_state.role = user_role
    if len(page_dict) > 0:
        pg = st.navigation({"Account": account_pages} | page_dict)
        pg.run()
elif authentication_status == False:
    st.error("Usuário/senha incorretos")
elif authentication_status == None:
    st.warning("Por favor ingrese seu usuário e senha")
