import streamlit as st
import os
import yaml
import re
from utils.password_utils import pass_hash

CONFIG_PATH = '.streamlit/users.yaml'
def load_config():
    if os.path.exists(CONFIG_PATH):
        with open(CONFIG_PATH, 'r') as file:
            return yaml.safe_load(file)
    return {}

def save_config(config):
    with open(CONFIG_PATH, 'w') as file:
        yaml.dump(config, file, default_flow_style=False)

config = load_config()

#### VALIDAR CNPJ ####
def validar_cnpj(cnpj):
    # Patrón para CNPJ: 12.345.678/0001-12
    patron = r"^\d{2}\.\d{3}\.\d{3}/\d{4}-\d{2}$"
    return re.match(patron, cnpj)

#### VALIDAR EMAIL ####
def validar_email(email_user):
    # Patrón para validar correos electrónicos
    patron = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    return re.match(patron, email_user)


st.header("Cadastro")

with st.form("settings"):
    st.subheader(":material/person_add: Cadastro/atualização estabelecimento", divider=True)
    name_company = st.text_input(
        label="Nome",
        value="",
        placeholder="Nome da sua empresa",
        disabled=False,
        label_visibility="visible",
    )
    name_user = st.text_input(
        label="Usuário",
        value="",
        placeholder="usuario",
        disabled=False,
        label_visibility="visible",
    )
    email_user = st.text_input(
        label="e-mail",
        placeholder="teumail@dominio.com",
        label_visibility="visible",
    )
    if email_user:
        if validar_email(email_user):
            st.success("Correo electrónico válido.")
        else:
            st.error(
                "e-mail inválido. Por favor, ingresse um email válido (ex., usuario@dominio.com)."
            )
    failed_login_attempts = 0
    logged_in = False
    role = 2
    password_user = st.text_input(
        label="Senha",
        type="password",
        placeholder="Sua senha",
        label_visibility="visible",
    )
    cnpj_user = st.text_input(
        label="Ingrese seu CNPJ", placeholder="##.###.###/####-##"
    )
    if cnpj_user:
        if validar_cnpj(cnpj_user):
            st.success("CNPJ válido.")
        else:
            st.error("Ingrese seu CNPJ (##.###.###/####-##)")
    user_status = st.radio(
        "Status cliente",
        key="visibility",
        options=["Ativo", "Inadimplente", "Demostração"],
        index=2,
        disabled=False,
    )
    submit_button = st.form_submit_button(label="Atualizar")
    if submit_button:
        if 'credentials' not in config:
            config['credentials'] = {}
        if 'usernames' not in config['credentials']:
            config['credentials']['usernames'] = {}
        
        hashed_password = pass_hash(password_user)
        config['credentials']['usernames'][name_user] = {
            'email': email_user,
            'failed_login_attempts': failed_login_attempts,
            'logged_in': logged_in,
            'name': name_company,
            'identification': cnpj_user,
            'role': role,
            'user_status': user_status,
            'password': hashed_password
        }
        # Guardar la configuración actualizada en el archivo YAML
        save_config(config)
        st.success("Estabelecimento cadastrado/atualizado!")