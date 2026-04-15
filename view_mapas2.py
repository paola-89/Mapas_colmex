import streamlit as st
import os
from PIL import Image

# 📁 Ruta a tus mapas
IMG_DIR = "output/VP_ae/mapas"

st.set_page_config(layout="wide")
st.title("Mapas Demográficos 🗺️")

# 🎛️ Controles
sexo = st.selectbox("Selecciona sexo:", ["Hombre", "Mujer"])
anio = st.selectbox("Selecciona año:", ["1990", "1995", "2000", "2005", "2010", "2020"])

# 📂 Obtener archivos
files = [
    f for f in os.listdir(IMG_DIR)
    if sexo in f and anio in f
]

orden = ["95-99", "100-104", "105-109", "110-114", "115+"]
files = sorted(files, key=lambda x: next((i for i, e in enumerate(orden) if e in x), 99))

# 🖼️ Mostrar mapas en grid
cols = st.columns(2)

for i, file in enumerate(files):
    img_path = os.path.join(IMG_DIR, file)
    image = Image.open(img_path)
    
    with cols[i % 2]:
        st.image(image, caption = file.replace("mapa_", "").replace(".png", ""), use_container_width=True)