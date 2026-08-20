import streamlit as st
from PIL import Image

st.title("Welcome to Japan")

st.header("En este espacio empieza tu viaje por japon")
st.write("facil mente puedes empezar por tokyo")
image = Image.open("images (1).jpg")
st.image(image, caption = "TOKYO")

         
texto = st.text_input("konichiwa desu", "sayonara")
st.write("el texto escrito es", texto)

st.subheader("shibuya")

col1, col12 = st.columns(2)

with col1:
         st.subheader("esta es la primera columna")
         st.write("La vida en japon es mas divertida")
         resp = st.checkbox("estoy de acuerdo")
         if resp:
                  st.write("Correcto")
