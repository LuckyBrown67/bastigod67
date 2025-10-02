# Importar streamlit
import streamlit as st

# ---------------------  Contenido del sitio   --------------------------#
# Sección Inicial
st.title("¿Quien es Lucky Brown?")
st.badge("Introducción", color="green", icon=":material/chevron_right:")

# Sutítulo
st.header("", divider=True)
#imagen
st.image("li.webp", caption="Artista")
#escritura
st.write(""" Lucky Brown, cuyo nombre real es Marco Sepúlveda, es un cantante y compositor chileno nacido en Santiago. Con tan solo 19 años, ha logrado posicionarse como una de las figuras emergentes más destacadas del género urbano en Chile. Su estilo fusiona reggaetón con influencias latinas tradicionales, creando un sonido único que ha capturado la atención de jóvenes y adultos por igual.

Desde su irrupción en la escena musical, Lucky ha demostrado una notable capacidad para conectar con su audiencia a través de letras sinceras y melodías pegajosas. Su ascenso meteórico en plataformas como Spotify y YouTube refleja el impacto que ha tenido en la música urbana nacional. """)