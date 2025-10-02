# Importar streamlit
import streamlit as st

# ---------------------  Contenido del sitio   --------------------------#
# Sección Inicial
st.title("Proyectos recientes y futuros")
st.badge("Proyectos", color="green", icon=":material/chevron_right:")

# Sutítulo
st.header("Los proyectos a futuros de Lucky Brown", divider=True)
#imagen mas una descripción
st.image("galactico.webp", caption="Proyetos")
#escritura
st.write(
"""
***La carrera de Lucky Brown ha estado marcada por lanzamientos estratégicos que han consolidado su posición en la escena urbana chilena. En 2023, presentó su primer EP, titulado “El de la Nueva Baby”, una producción que incluyó varios sencillos y mostró su versatilidad como artista. Este trabajo fue clave porque le permitió diferenciarse de otros cantantes emergentes y le abrió la posibilidad de ser considerado como una figura seria dentro del género.
En el tRanscurso de 2024, sorprendió con canciones como Coa Xorete, que reflejó un lado más explícito y callejero, distinto de sus temas románticos o bailables. Con esta estrategia demostró que no se limita a un solo estilo, sino que busca llegar a públicos diversos. Ese mismo año, continuó lanzando sencillos que reforzaron su presencia en las listas de streaming, manteniendo su popularidad en alza.
Actualmente, en 2025, se encuentra preparando su primer álbum de estudio oficial, titulado “Color de Rosa”. Como adelanto, estrenó el sencillo Sola en Casa, que generó gran expectativa entre sus fanáticos y medios especializados. Este proyecto es considerado un paso crucial en su carrera, pues un álbum completo le permitirá mostrarse con mayor madurez artística y consolidar un sonido propio.
El objetivo de Lucky Brown es expandir su música hacia mercados internacionales, principalmente en países como México, Argentina y Colombia, donde el reggaetón chileno está teniendo mayor repercusión. Con el respaldo de su sello, busca que “Color de Rosa” no solo sea un éxito local, sino también una puerta de entrada hacia Latinoamérica. De esta manera, sus proyectos recientes y futuros lo posicionan como un artista en plena evolución y con aspiraciones de convertirse en un nombre reconocido fuera de Chile.
...***
""") 