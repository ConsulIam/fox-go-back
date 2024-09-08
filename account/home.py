import streamlit as st

st.header("Home")
st.subheader(
    f":tada: Bem-vindo {st.session_state.name} à sua Plataforma de Gestão de Clientes! :tada:", divider=True
)

home_description = """Aqui é o seu ponto de partida para criar uma conexão verdadeira com seus clientes e transformar visitas esporádicas em recorrentes. No Home, você encontrará um panorama geral do desempenho de sua estratégia de fidelização. Tenha acesso rápido ao número de cupons emitidos, redimidos e em andamento :bar_chart:. Observe de perto como sua base de clientes está respondendo às campanhas e identifique oportunidades para surpreender ainda mais seus visitantes! :rocket:

#### Destaques:

* *Visão Geral de Atividades*: Veja um resumo das interações mais recentes e acompanhe a evolução do engajamento dos clientes com suas ofertas.

* *Cupones*: Crie cupones para produtos e dias chaves!. Garanta o retorno do seus clientes e a a efetiva medição do retorno :dart:
"""

st.markdown(home_description)