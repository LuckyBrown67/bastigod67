# Importar streamlit
import streamlit as st

# ---------------------  Contenido del sitio   --------------------------#
# Sección Inicial
st.title("Canciones")
st.badge("Exitos", color="green", icon=":material/chevron_right:")

# Sutítulo
st.header("Aqui te presento los exitos de Lucky Brown", divider=True)
#imagen mas una descripción
st.image("ep.webp", caption="EP")
st.audio("nubes.mp3")
#escritura
st.write(
"""
**Lucky Brown ha lanzado una serie de sencillos y EPs que han sido bien recibidos tanto por la crítica como por sus seguidores. Entre sus principales trabajos se encuentran:

EP "El de la Nueva Baby" (2023): Un proyecto que destaca por su propuesta de reggaetón bailable y letras que celebran la autoestima y la belleza femenina. Incluye colaboraciones con artistas como Pailita y Jere Klein.

Álbum "I Am Lucky Brown" (2024): Su primer álbum de larga duración, que consolidó su estilo y le permitió ampliar su alcance internacional.

Sencillos destacados:

"Vengo De La Brea" (feat. Jere Klein): Un tema que combina ritmos urbanos con letras que narran historias de superación.

"Qué Será": Una canción que refleja su evolución artística y su capacidad para experimentar con nuevos sonidos.

"Sola en Casa" y "Zona": Sencillos recientes que han mantenido su presencia en las listas de éxitos.***
""")