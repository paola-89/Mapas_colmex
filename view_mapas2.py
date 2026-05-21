
import streamlit as st
import os
from PIL import Image

st.set_page_config(layout="wide")

st.title("Mapas Demográficos 🗺️")

st.write("Se muestra la proporción de población estatal respecto al total de la república mexicana")

# 📁 Rutas
IMG_DIRS = {
    "VP": "output/VP_ae/mapas",
    "VC": "output/VC_ae/mapas"
}

# 🎛️ Controles
tipo = st.selectbox("Tipo de vivienda:", ["VP", "VC"])
sexo = st.selectbox("Sexo:", ["Hombre", "Mujer"])
anio = st.selectbox("Año:", ["1990", "1995", "2000", "2005", "2010", "2020"])

IMG_DIR = IMG_DIRS[tipo]

#  Obtener archivos
files = [
    f for f in os.listdir(IMG_DIR)
    if sexo in f and anio in f
]

# ordenar por edad
orden = ["95-99", "100-104", "105-109", "110-114", "115+"]

files = sorted(
    files,
    key=lambda x: next((i for i, e in enumerate(orden) if e in x), 99)
)

# Mostrar mapas 
cols = st.columns(2)

for i, file in enumerate(files):
    img_path = os.path.join(IMG_DIR, file)
    
    with cols[i % 2]:
        caption = file.replace("mapa_", "").replace(".png", "")
        st.image(img_path, caption=caption, use_container_width=True)
