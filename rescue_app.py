import streamlit as st
from streamlit_geolocation import streamlit_geolocation
import pandas as pd

st.set_page_config(page_title="K9 Nexus - Rescate", layout="wide")

# --- LÓGICA DE LA VÍCTIMA ---
# Si el enlace tiene ?mode=help, se ejecuta esto:
if st.query_params.get("mode") == "help":
    st.title("🆘 Formulario de Emergencia")
    st.write("Presione el botón para enviar su ubicación a la central:")
    
    loc = streamlit_geolocation()
    if loc and loc.get('latitude'):
        st.success(f"Ubicación capturada: {loc['latitude']}, {loc['longitude']}")
        # Nota: Aquí se necesitaría una base de datos real (Supabase/Firebase) 
        # para que la central reciba esto en tiempo real.
    st.stop() # Detiene el resto del código para que no vea el panel de control

# --- LÓGICA DEL RESCATISTA (PANEL) ---
st.title("🛡️ Panel de Rescate K9 Nexus")
st.subheader("Generar Enlace de Rescate")

tel = st.text_input("Teléfono de la víctima:")
if st.button("Generar Enlace"):
    # IMPORTANTE: Aquí debes poner la IP pública de tu servidor 
    # o el enlace que tu servicio de hosting te dé.
    # Por ahora, mantendremos localhost para pruebas locales.
    enlace = f"http://localhost:8501/?mode=help&tel={tel}"
    st.info("Copie y envíe este enlace:")
    st.code(enlace)

st.write("---")
st.write("### Mapa de Operaciones")
st.info("Esperando que las víctimas abran el enlace y acepten el permiso de GPS...")