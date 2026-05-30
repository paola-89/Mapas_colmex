
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

# Selectores
tipo = st.selectbox("Tipo de vivienda:", ["VP", "VC"])

sexos = ["Hombre", "Mujer"]
anios = ["1990", "1995", "2000", "2005", "2010", "2020"]

sexo_sel = st.multiselect(
    "Sexo:",
    sexos,
    default=sexos)

anio_sel = st.multiselect(
    "Año:",
    anios,
    default=anios)

IMG_DIR = IMG_DIRS[tipo]

#  Obtener archivos
files = [
    f for f in os.listdir(IMG_DIR)
    if any(sexo in f for sexo in sexo_sel)
    and any(anio in f for anio in anio_sel)
]

# ordenar por edad
orden = ["95-99", "100-104", "105-109", "110-114", "115+"]

files = sorted(
    files,
    key=lambda x: next((i for i, e in enumerate(orden) if e in x), 99)
)

# Mostrar mapas 
sexo_txt = ", ".join(sexo_sel)
anio_txt = ", ".join(anio_sel)

st.subheader(f"Sexo: {sexo_txt} | Año: {anio_txt}")

if not files:
    st.warning("No hay mapas para estos filtros")
else:
    st.write(f"Mapas mostrados: {len(files)}")
    
    cols = st.columns(2)
    
    for i, file in enumerate(files):
        img_path = os.path.join(IMG_DIR, file)
        
        with cols[i % 2]:
            caption = file.replace("mapa_", "").replace(".png", "")
            st.image(img_path, caption=caption, use_container_width=True)
