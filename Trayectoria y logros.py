# Importar streamlit
import streamlit as st

# ---------------------  Contenido del sitio   --------------------------#
# Sección Inicial
st.title("Trayectoria y Logros")
st.badge("Trayectoria", color="green", icon=":material/chevron_right:")

# Sutítulo
st.header("Aqui te presento la gran trayectoria de Lucky Brown", divider=True)
#imagen mas una descripción
st.image("t.webp", caption="Logros")
#escritura
st.write(
"""
**A pesar de que su carrera es reciente, ya ha acumulado más de 120 a 130 millones de reproducciones en plataformas digitales.
En Spotify alcanza más de 2 millones de oyentes mensuales, cifra muy alta para un artista chileno en ascenso.
Varios de sus singles han entrado al Top 100 de Spotify Chile, lo que lo pone al nivel de otros artistas urbanos reconocidos.
Sus canciones se han viralizado en TikTok, lo que le ha permitido llegar a públicos más jóvenes y convertir temas como Me veo rico o Mándame tu ubi en fenómenos.
Ha tenido la oportunidad de presentarse en conciertos masivos como telonero, lo cual le da vitrina frente a miles de personas y lo posiciona como una promesa del género.
Su primer EP, El de la Nueva Baby (2023), marcó un hito porque consolidó su propuesta y mostró variedad de estilos, siendo bien recibido en la escena urbana chilena..***
""")
