# Importar streamlit
import streamlit as st

# ---------------------  Contenido del sitio   --------------------------#
# Sección Inicial
st.title("Estilo Musical")
st.badge("Estilo", color="green", icon=":material/chevron_right:")

# Sutítulo
st.header("El estilo unico de Lucky Brown", divider=True)
#imagen mas una descripción
st.image("album.webp", caption="Estilo")
#escritura
st.write(
"""
**El estilo de Lucky Brown se basa principalmente en el reggaetón urbano, aunque incorpora influencias del trap y del reggaetón clásico puertorriqueño. Su versatilidad es una de sus mayores fortalezas, ya que puede moverse entre distintos matices del género. Por un lado, tiene canciones de tono romántico y bailable, como Avísame o Mírame, donde fusiona letras de amor y deseo con ritmos pegajosos que invitan a bailar. Por otro, también cultiva un estilo más explícito y callejero, presente en temas como Coa Xorete, donde el lenguaje directo y la fuerza rítmica apuntan a un público distinto.

Sus letras suelen girar en torno a la atracción, las relaciones, la belleza femenina y el estilo de vida urbano, temáticas muy conectadas con la juventud actual. En lo musical, busca una mezcla entre lo melódico y lo rítmico, logrando canciones que funcionan tanto para escuchar de forma individual como en fiestas y discotecas.

Este equilibrio entre lo suave y lo duro le ha permitido captar distintos públicos, mostrando que no se encasilla en un solo tipo de reggaetón. Su estilo es, en definitiva, una propuesta fresca que combina lo mejor de la tradición del género con la modernidad de las tendencias digitales...***
""")
