import streamlit as st
import re


def validar_cnpj(cnpj):
    # Patrón para CNPJ: 12.345.678/0001-12
    patron = r"^\d{2}\.\d{3}\.\d{3}/\d{4}-\d{2}$"
    return re.match(patron, cnpj)


def validar_email(email_user):
    # Patrón para validar correos electrónicos
    patron = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    return re.match(patron, email_user)


st.header("Configuração")

with st.form("settings"):
    st.subheader(":wrench: Atualizar informações do estabelecimento", divider=True)
    name_company = st.text_input(
        label="Nome",
        value=st.session_state.name,
        placeholder="Nome da sua empresa",
        disabled=True,
        label_visibility="visible",
    )
    name_user = st.text_input(
        label="Usuário",
        value=st.session_state.username,
        placeholder="usuario",
        disabled=True,
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
        disabled=True,
    )
    submit_button = st.form_submit_button(label="Atualizar")
    if submit_button:
        st.write("Atualizado")
