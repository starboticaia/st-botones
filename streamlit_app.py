import streamlit as st

# demo de texto y botón
animales = ['gato', 'perro', 'pez', 'lagarto']

animal = st.text_input('Pide un animal...')

if st.button('Ver disponibilidad'):
    disponible = animal.lower() in animales
    if disponible:
      st.write('¡Lo tenemos!')
    else:
      st.write('Lo sentimos, no lo tenemos.')
