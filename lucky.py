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
pg = st.navigation(["quienes somos.py", "home.py", "intro.py" , "cancione.py" , "Trayectoria y logros.py", "Estilo musical.py", "Colaboraciones.py", "Influencia en redes sociales.py", "proyectos.py","Reconocimientos y critica.py"])
pg.run()