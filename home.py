# Importar streamlit
import streamlit as st

# ---------------------  Contenido del sitio   --------------------------#
# Sección Inicial
st.title("¿Que encuentras en esta pagina?")
st.badge("Te lo presentamos", color="green", icon=":material/chevron_right:")

# Sutítulo
st.header("Aqui te comento sobre que hay en esta pagina", divider=True)
#imagen mas una descripción
st.image("priv.jpg", caption="¿Que hay?")
#escritura
st.write(
"""
** Esta página web está dedicada al músico Lucky Brown, un artista destacado dentro del funk y soul contemporáneo. El objetivo de este sitio es dar a conocer su trayectoria, su estilo único y el impacto que ha tenido en la música.
Aquí encontrarás información sobre:

Temas: un repaso de sus composiciones más reconocidas.

Canciones: sus lanzamientos más importantes y populares.

Biografía: datos sobre su vida y sus inicios en la música.

Trayectoria: el recorrido de su carrera artística.

Estilo musical: influencias, géneros y características de su sonido.

Influencia en redes sociales: cómo conecta con su público y difunde su obra.

Y más: curiosidades y detalles que ayudan a comprender mejor a Lucky Brown.

La temática principal de esta página es la difusión de la obra musical de Lucky Brown y el reconocimiento de su aporte al funk y al soul, mostrando por qué sigue siendo una figura relevante en la escena actual.
...***
""")
