import streamlit as st
from src.app import adicionar_gasto, total_gastos, cotacao_dolar

st.title("Controle de Gastos")

st.subheader("Adicionar gasto")

valor = st.number_input("Valor", min_value=0.0)

categoria = st.text_input("Categoria")

if st.button("Adicionar"):
    adicionar_gasto(valor, categoria)
    st.success("Gasto adicionado!")

st.subheader("Total de gastos")

if st.button("Ver total"):
    st.write(f"R$ {total_gastos()}")

st.subheader("Cotação do dólar")

if st.button("Ver cotação"):
    st.write(f"R$ {cotacao_dolar()}")