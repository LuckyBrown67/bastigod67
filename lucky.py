# Importar streamlit
import streamlit as st

# Configurar la pagina
st.set_page_config(
    page_title="Lucky Brown",
    page_icon=":no_entry:", # Usar el comando python -m rich.emoji para ver lista de emojis
    layout="centered",
)

# Configuración de Logo
st.logo(
    "li.webp",
)
#para iniciar las paginas
pg = st.navigation(["quienes_somos.py", "home.py", "intro.py", "cancione.py", "Trayectoria_y_logros.py", "Estilo_musical.py", "Colaboraciones.py", "Influencia_en_redes_sociales.py", "proyectos.py", "Reconocimientos_y_Critica.py"])

pg.run()




