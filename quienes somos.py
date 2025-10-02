# Importar streamlit
import streamlit as st

# ---------------------  Contenido del sitio   --------------------------#
# Sección Inicial
st.title("¿Quien Soy?")
st.badge("¿Quien soy?", color="green", icon=":material/chevron_right:")

# Sutítulo
st.header("Aqui te comento mas sobre quien soy y por que hago este tipo de paginas", divider=True)
#imagen mas una descripción
st.image("t.webp", caption="Yo")
#escritura
st.write(
"""
**
Hola, soy Tito Calderón, un gran fan de la música urbana en Chile. Desde hace años me apasiona seguir a distintos artistas, descubrir nuevas canciones y compartir con otros lo que me gusta de este género.

Este sitio lo hice para rendir un pequeño homenaje a Lucky Brown, mostrando su música, trayectoria e influencia. Mi idea es que las personas que lleguen aquí puedan conocerlo mejor y disfrutar tanto como yo de su estilo único.

No soy productor ni cantante, solo un seguidor entusiasta que disfruta aprender y difundir lo mejor de la música urbana. Espero que esta página se convierta en un espacio para fans, curiosos y amantes de los buenos ritmos...***
""")

