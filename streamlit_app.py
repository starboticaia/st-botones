import streamlit as st

# demo de entrada numérica y botón
st.header("Calculadora de pulgadas a centímetros")
pulgadas = st.number_input('Pulgadas:')

if st.button('Calcular'):
    centimetros = pulgadas*2.51
    st.write(f"{pulgadas}" equivalen a {centimetros} cm.")
