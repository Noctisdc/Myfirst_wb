import streamlit as st
from PIL import Image

st.set_page_config(page_title="Welcome to Japan", layout="centered")

st.markdown("""
<style>
.stApp {
    background-color: #fff5f5;
}
[data-testid="stHeader"] {
    background-color: #fff5f5;
}
h1 {
    color: #bc002d;
    text-align: center;
    border-bottom: 4px solid #bc002d;
    padding-bottom: 10px;
}
h2, h3 {
    color: #8b0000;
}
div.stButton > button {
    background-color: #bc002d;
    color: white;
    border-radius: 20px;
    border: none;
    padding: 8px 24px;
}
div.stButton > button:hover {
    background-color: #8b0000;
    color: white;
}
</style>
""", unsafe_allow_html=True)

st.title("Welcome to Japan 🇯🇵")
st.header("Tu viaje empieza aquí")

nombre = st.text_input("¿Cómo te llamas, viajero?", "Viajero")
st.write(f"Konnichiwa, {nombre}. Tienes un pasaje, una maleta y cuatro capítulos por delante.")

st.divider()

tab1, tab2, tab3, tab4 = st.tabs(["🗼 Tokyo", "⛩️ Kyoto", "🍜 Osaka", "🗻 Monte Fuji"])

with tab1:
    st.subheader("Capítulo 1: Llegada a Tokyo")
    image = Image.open("images (1).jpg")
    st.image(image, caption="TOKYO", use_container_width=True)
    st.write(f"{nombre} aterriza en Tokyo al amanecer. La ciudad ya está despierta: trenes puntuales, máquinas expendedoras en cada esquina y luces de neón que no se apagan.")
    st.write("Por la tarde llega a **Shibuya**, donde cientos de personas cruzan la calle al mismo tiempo desde todas las direcciones. Después visita **Asakusa** y su templo Senso-ji, el más antiguo de la ciudad.")
    resp = st.checkbox("Estoy de acuerdo: la vida en Japón es más divertida")
    if resp:
        st.success("Correcto, el viaje apenas comienza.")

with tab2:
    st.subheader("Capítulo 2: Kyoto, la ciudad de los templos")
    st.write("Un viaje en el tren bala (Shinkansen) lleva a nuestro viajero a Kyoto, antigua capital de Japón.")
    st.write("Allí camina bajo los miles de portales rojos del santuario **Fushimi Inari** y descubre el **Kinkaku-ji**, el pabellón dorado que se refleja en un estanque.")
    modo = st.radio("¿Qué modalidad es la principal en tu viaje?", ("Visual", "Auditiva", "Táctil"))
    if modo == "Visual":
        st.write("Los ojos son fundamentales: los colores de los templos y los jardines lo dicen todo.")
    if modo == "Auditiva":
        st.write("El oído es lo mejor: campanas de templo, agua corriendo y el silencio de los jardines.")
    if modo == "Táctil":
        st.write("El tacto es lo más importante: la madera de los templos, la tela del kimono y la cerámica hecha a mano.")

with tab3:
    st.subheader("Capítulo 3: Osaka y su comida")
    st.write("En Osaka dicen que se viene a comer. En el barrio de **Dotonbori**, entre carteles gigantes y calles llenas de gente, el viajero prueba los platos más famosos de la ciudad.")
    plato = st.selectbox("¿Qué quieres probar primero?", ("Takoyaki", "Okonomiyaki", "Ramen"))
    if plato == "Takoyaki":
        st.write("Bolitas de masa rellenas de pulpo, bañadas en salsa y cubiertas con bonito seco.")
    if plato == "Okonomiyaki":
        st.write("Una especie de panqueque salado con repollo y carne, cocinado en plancha frente a ti.")
    if plato == "Ramen":
        st.write("Un caldo caliente con fideos, ideal para terminar la noche.")

with tab4:
    st.subheader("Capítulo 4: El Monte Fuji")
    st.write("El último destino es el **Monte Fuji**, la montaña más alta de Japón con 3.776 metros. Desde sus lagos, en un día despejado, se ve su cima cubierta de nieve.")
    altura = st.slider("¿Cuánto quieres subir?", 0, 3776, 1000)
    st.progress(altura / 3776)
    st.write(f"Has llegado a {altura} metros de altura.")
    if altura == 3776:
        st.success("¡Llegaste a la cima!")

st.divider()

st.subheader("Fin del viaje")
st.write(f"Así termina la historia de {nombre} en Japón: una ciudad moderna, templos antiguos, buena comida y una montaña para despedirse.")

if st.button("Presiona para comenzar otro viaje"):
    st.balloons()
    st.write("Sayonara... hasta el próximo viaje.")
