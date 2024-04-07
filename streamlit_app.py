import streamlit as st

# demo de entrada numérica y botón
st.header("Calculadora de pulgadas a centímetros")
pulgadas = st.number_input('Pulgadas:')

if st.button('Calcular'):
    centimetros = pulgadas*2.51
    # añadir :.2f a un número para limitarlo a dos decimales
    st.write(f'{pulgadas}" equivalen a {centimetros}:.2f cm.')
