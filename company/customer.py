import streamlit as st
import random
from datetime import datetime

st.header("Clientes")

name = "Nombre"
whatsapp_number = "WhatsApp"
last_interaction = "Última iteração"
cupons_used = "Cupones usados"
cupons_spend = "Valor gasto"

names = ["Juan", "Ana", "Luis", "María", "Carlos", "Elena", "Pedro", "Lucía", "Miguel", "Sara", 
           "Andrés", "Laura", "Sofía", "Diego", "Camila", "Daniel", "Valeria", "Jorge", "Gabriela", "Roberto"]
customers_data = []

for i in range(20):
    customer = {
        name: names[i],  # Usa los nombres en orden; puedes usar random.choice(nombres) si quieres nombres aleatorios.
        whatsapp_number: f"+55518810{random.randint(10000, 99999)}",  # Genera un número de WhatsApp aleatorio
        last_interaction: datetime.fromtimestamp(random.randint(int(datetime(2024, 7, 1).timestamp()), 
                                                                  int(datetime(2024, 7, 31).timestamp()))),  # Fecha aleatoria en julio 2024
        cupons_used: random.randint(0, 10),  # Número aleatorio de cupones usados
        cupons_spend: f"R${random.uniform(0, 1000):.2f}"  # Gasto en cupones formateado
    }
    customers_data.append(customer)

st.table(customers_data)