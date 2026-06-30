import streamlit as st
from streamlit_geolocation import streamlit_geolocation
import pandas as pd
import os

st.set_page_config(page_title="K9 Nexus - Rescate", layout="wide")

DB_FILE = "ubicaciones.csv"

# Función para guardar ubicación en el archivo compartido
def guardar_ubicacion(tel, lat, lon):
    df = pd.DataFrame([{"Telefono": tel, "Lat": lat, "Lon": lon}])
    if os.path.exists(DB_FILE):
        df.to_csv(DB_FILE, mode='a', header=False, index=False)
    else:
        df.to_csv(DB_FILE, index=False)

# --- LÓGICA DE LA VÍCTIMA ---
if st.query_params.get("mode") == "help":
    tel_victima = st.query_params.get("tel", "Desconocido")
    st.title("🆘 Formulario de Emergencia")
    st.write("Presione el botón para enviar su ubicación a la central:")
    
    loc = streamlit_geolocation()
    if loc and loc.get('latitude'):
        lat, lon = loc['latitude'], loc['longitude']
        st.success(f"Ubicación capturada: {lat}, {lon}")
        
        if st.button("Enviar ubicación a Rescatistas"):
            guardar_ubicacion(tel_victima, lat, lon)
            st.info("¡Ubicación enviada correctamente!")
    st.stop()

# --- LÓGICA DEL RESCATISTA ---
st.title("🛡️ Panel de Rescate K9 Nexus")

# Cargar y mostrar ubicaciones recibidas
if os.path.exists(DB_FILE):
    df = pd.read_csv(DB_FILE)
    st.subheader("📍 Mapa de Víctimas Localizadas")
    st.map(df)
    st.dataframe(df)
else:
    st.info("Esperando alertas de víctimas...")

st.divider()
tel = st.text_input("Teléfono de la víctima:")
if st.button("Generar Enlace"):
    # IMPORTANTE: Reemplaza por la URL real de tu app en Streamlit Cloud
    base_url = "https://rescueapp-ms4hhy9pgff7kvzibnadp8.streamlit.app" 
    st.code(f"{base_url}/?mode=help&tel={tel}")
