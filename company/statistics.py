import streamlit as st
from datetime import datetime, timedelta
import random

# Função para gerar dados simulados
def generate_simulated_data():
    # Gerar uma lista de clientes fictícios
    clients = [f'Cliente {i:02}' for i in range(1, 11)]
    
    # Gerar dados simulados para mensagens de WhatsApp
    data = []
    for _ in range(100):
        cliente = random.choice(clients)
        mensagens_enviadas = random.randint(1, 50)
        cupons_recebidos = random.randint(1, 20)
        valor_cupons_reais = round(random.uniform(10.0, 200.0), 2)
        data.append({
            'Cliente': cliente,
            'Mensagens_WhatsApp_Enviadas': mensagens_enviadas,
            'Cupons_Recebidos': cupons_recebidos,
            'Valor_Cupons_Reais': valor_cupons_reais,
            'Data': datetime.now() - timedelta(days=random.randint(0, 30))
        })
    
    # Agregar dados por cliente
    summary = {}
    for entry in data:
        cliente = entry['Cliente']
        if cliente not in summary:
            summary[cliente] = {
                'Mensagens_WhatsApp_Enviadas': 0,
                'Cupons_Recebidos': 0,
                'Valor_Cupons_Reais': 0.0
            }
        summary[cliente]['Mensagens_WhatsApp_Enviadas'] += entry['Mensagens_WhatsApp_Enviadas']
        summary[cliente]['Cupons_Recebidos'] += entry['Cupons_Recebidos']
        summary[cliente]['Valor_Cupons_Reais'] += entry['Valor_Cupons_Reais']
    
    return data, summary

# Gerar dados simulados
data, summary = generate_simulated_data()

# Título da página
st.title('Estatísticas de Mensagens e Cupons')

# Seção 1: Estatísticas de Mensagens de WhatsApp Enviadas por Cliente
st.header('Estatísticas de Mensagens de WhatsApp Enviadas por Cliente')
mensagens_por_cliente = {cliente: valores['Mensagens_WhatsApp_Enviadas'] for cliente, valores in summary.items()}
st.bar_chart(mensagens_por_cliente)

# Seção 2: Estatísticas de Cupons por Cliente
st.header('Estatísticas de Cupons por Cliente')
cupons_por_cliente = {cliente: valores['Cupons_Recebidos'] for cliente, valores in summary.items()}
st.bar_chart(cupons_por_cliente)

# Seção 3: Valor dos Cupons em Reais por Cliente
st.header('Estatísticas de Valor dos Cupons em Reais por Cliente')
valor_cupons_por_cliente = {cliente: valores['Valor_Cupons_Reais'] for cliente, valores in summary.items()}
st.bar_chart(valor_cupons_por_cliente)

# Seção 4: Análises Adicionais
st.header('Análises Adicionais')

# Taxa de conversão de cupons (mensagens enviadas para cupons recebidos)
taxa_conversao = {cliente: valores['Cupons_Recebidos'] / valores['Mensagens_WhatsApp_Enviadas'] if valores['Mensagens_WhatsApp_Enviadas'] > 0 else 0 for cliente, valores in summary.items()}
st.line_chart(taxa_conversao)

# Média de valor dos cupons
media_valor_cupons = sum(valor_cupons_por_cliente.values()) / len(valor_cupons_por_cliente)
st.metric(label="Média de Valor dos Cupons (R$)", value=f"{media_valor_cupons:.2f}")

# Número total de cupons e mensagens
total_mensagens = sum(mensagens_por_cliente.values())
total_cupons = sum(cupons_por_cliente.values())
st.metric(label="Total de Mensagens Enviadas", value=total_mensagens)
st.metric(label="Total de Cupons Recebidos", value=total_cupons)