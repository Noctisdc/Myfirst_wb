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
         st.subheader("Este es tu primer viaje")
         st.write("La vida en japon es mas divertida")
         resp = st.checkbox("estoy de acuerdo")
         if resp:
                  st.write("Correcto")

with col12
st.subheader("este es tu segundo viaje")
modo = st.radio("que modalidad es la principal en tu interfaz", ("visual", "auditiva", "tactil"))
if modo == "visual":
         st.write("Los ojos son fundamentales para tu viaje")
if modo == "auditiva": 
         st.write("El oido es lo mejor para tu viaje")
if modo== "Tactil":
         st.write("El tacto es lo mas importante en tu viaje")

st.subheader("uso de botones")
if st.button("Presiona el boton"):
    st.write("Gracias por presionar")
else:
         st.write("No has presionado aun")
