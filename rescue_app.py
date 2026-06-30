import streamlit as st
from streamlit_geolocation import streamlit_geolocation
import pandas as pd

st.set_page_config(page_title="K9 Nexus - Rescate", layout="wide")

# Detectar la URL base automáticamente
# Si estás en Streamlit Cloud, esto capturará tu URL pública
base_url = st.query_params.get("base_url", "http://localhost:8501")

# --- LÓGICA DE LA VÍCTIMA ---
if st.query_params.get("mode") == "help":
    st.title("🆘 Formulario de Emergencia")
    st.write("Presione el botón para enviar su ubicación a la central:")
    
    loc = streamlit_geolocation()
    if loc and loc.get('latitude'):
        st.success(f"Ubicación capturada: {loc['latitude']}, {loc['longitude']}")
        st.info("Su ubicación ha sido enviada.")
    st.stop()

# --- LÓGICA DEL RESCATISTA ---
st.title("🛡️ Panel de Rescate K9 Nexus")

# Input para teléfono
tel = st.text_input("Teléfono de la víctima:")

if st.button("Generar Enlace"):
    # Si la app detecta que está en la nube, usará la URL pública
    # Si estás en local, usa localhost.
    # Para forzar la URL pública, puedes escribirla aquí manualmente:
    # url_base = "https://TU-APP.streamlit.app" 
    
    enlace = f"{base_url}/?mode=help&tel={tel}"
    st.info("Copie y envíe este enlace a la víctima:")
    st.code(enlace)

st.write("---")
st.subheader("Mapa de Operaciones")
st.info("Esperando alertas...")
