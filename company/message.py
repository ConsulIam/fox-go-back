import streamlit as st
import yaml
import os

# Funções para carregar e salvar configurações e mensagens

def load_messages():
    if os.path.exists('.streamlit/messages.yaml'):
        with open('.streamlit/messages.yaml') as file:
            data = yaml.safe_load(file)
            if data is None:
                return {'messages': {}}
            return data
    return {'messages': {}}

def save_messages(messages):
    with open('.streamlit/messages.yaml', 'w') as file:
        yaml.safe_dump(messages, file)

# Função para exibir uma aba com seu formulário
def display_tab(tab_id, messages, current_user):
    if tab_id not in messages['messages']:
        # Se a aba não tem mensagem, solicitar título e conteúdo
        with st.form(key=f'new_{tab_id}'):
            title = st.text_input('Nome mensagem', key=f'{tab_id}_title')
            content = st.text_area('Mensagem', key=f'{tab_id}_content')
            submit_button = st.form_submit_button('Salvar Mensagem')
            if submit_button:
                messages['messages'][tab_id] = {
                    'title_message': title,
                    'content_message': content,
                    'user_message': current_user,
                    'datecreated_message': '2024-09-08'  # Use a data atual se necessário
                }
                save_messages(messages)
                st.success('Mensagem salva')
    else:
        # Se a aba já tem mensagem, mostrar opções para editar ou excluir
        st.write("Nome Mensagem")
        st.write(f"{messages['messages'][tab_id]['title_message']}")
        st.write("Mensagem")
        st.write(f"{messages['messages'][tab_id]['content_message']}")
        col1, col2 = st.columns([1, 1])
        with col1:
            edit_button = st.button('Editar Mensagem', key=f'{tab_id}_edit')
        with col2:
            delete_button = st.button('Excluir Mensagem', key=f'{tab_id}_delete')
        
        if edit_button:
            with st.form(key=f'{tab_id}_edit_form'):
                title = st.text_input('Nome mensagem', value=messages['messages'][tab_id]['title_message'], key=f'{tab_id}_title_edit')
                content = st.text_area('Mensagem', value=messages['messages'][tab_id]['content_message'], key=f'{tab_id}_content_edit')
                st.text_input("Hola", value=messages['messages'][tab_id]['title_message'] )
                st.text_input("Chao", value=f'{tab_id}_edit_form')
                save_button = st.form_submit_button('Salvar alteração')
                if save_button:
                    messages['messages'][tab_id]['title_message'] = title
                    messages['messages'][tab_id]['content_message'] = content
                    save_messages(messages)
                    st.success('Mensagem editada com sucesso')
        if delete_button:
            del messages['messages'][tab_id]
            save_messages(messages)
            st.success('Mensagem excluída com sucesso')

# Configuração inicial
current_user = st.session_state.get('username', 'desconhecido')  # Usuário atual

# Aplicativo principal
st.title('Gestão de Mensagens de WhatsApp')
messages = load_messages()

# Inicializar abas
if 'tabs' not in st.session_state:
    st.session_state['tabs'] = list(messages['messages'].keys()) if messages['messages'] else ['001']

# Adicionar ou remover abas
col1, col2 = st.columns([1, 3])
with col1:
    if st.button('Adicionar Aba'):
        new_tab_id = f"{len(st.session_state['tabs']) + 1:03}"  # Garantir que seja uma string com zeros à esquerda
        if new_tab_id not in st.session_state['tabs']:
            st.session_state['tabs'].append(new_tab_id)
            if new_tab_id not in messages['messages']:
                messages['messages'][new_tab_id] = {
                    'title_message': '',
                    'content_message': '',
                    'user_message': current_user,
                    'datecreated_message': '2024-09-08'  # Use a data atual se necessário
                }
                save_messages(messages)
with col2:
    if st.button('Remover Última Aba') and len(st.session_state['tabs']) > 1:
        tab_to_remove = st.session_state['tabs'].pop()
        if tab_to_remove in messages['messages']:
            del messages['messages'][tab_to_remove]
            save_messages(messages)

# Mostrar abas como tabs com ícone
if st.session_state['tabs']:  # Garantir que `tabs` não esteja vazio
    tab_labels = [f"✉️ {tab_id}" for tab_id in st.session_state['tabs']]  # Etiquetas das abas com ícone
    tab_elements = st.tabs(tab_labels)

    for tab_id, tab_element in zip(st.session_state['tabs'], tab_elements):
        with tab_element:
            display_tab(tab_id, messages, current_user)
else:
    st.write("Não há abas para exibir.")
