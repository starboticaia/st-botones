import streamlit as st

# demo de entrada numérica y botón
st.header("Calculadora de euros a dólares")
valor_dolar = st.number_input('Valor del dólar')
euros = st.number_input('Introduce la cantidad de euros.')

if st.button('Calcular'):
    dolares = euros*valor_dolar
    st.write(f"{euros} € equivalen a {dolares} $")
