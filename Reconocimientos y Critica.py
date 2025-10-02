# Importar streamlit
import streamlit as st

# ---------------------  Contenido del sitio   --------------------------#
# Sección Inicial
st.title("Reconocimiento y Critica")
st.badge("Reconocimiento", color="green", icon=":material/chevron_right:")

# Sutítulo
st.header("Los reconocimientos y critica de Lucky Brown", divider=True)
#imagen mas una descripción
st.image("reco.jpg", caption="Reconocimiento")
#escritura
st.write(
"""
**
Aunque su trayectoria aún es relativamente corta, Lucky Brown ha logrado captar la atención de la crítica y los medios especializados en música urbana. Su nombre aparece constantemente en portales como Los40 Chile, Aldea Local y Bandas Chilenas, donde se lo describe como uno de los exponentes más prometedores del reggaetón nacional. Estas menciones no son menores, ya que reflejan la manera en que su trabajo ha trascendido más allá de los fanáticos para convertirse en un tema de conversación dentro de la industria.

Uno de los puntos más destacados por la crítica es su versatilidad musical. Se le reconoce la capacidad de transitar entre estilos distintos: desde reggaetón romántico y melódico hasta canciones más duras y explícitas. Esta dualidad le da un carácter único dentro de la escena chilena, donde muchos artistas suelen encasillarse en un solo tipo de propuesta. También se valora su capacidad de conectar con el público joven, que ve en él una figura fresca, cercana y auténtica.

En cuanto a reconocimientos formales, aún no ha recibido premios de gran envergadura internacional. Sin embargo, su crecimiento sostenido en plataformas como Spotify y TikTok es considerado en sí mismo un indicador de éxito. La crítica coincide en que, de mantener este ritmo de lanzamientos y popularidad, es muy probable que en los próximos años pueda ser nominado a importantes certámenes musicales, tanto en Chile como en el extranjero.

En resumen, la recepción de la crítica hacia Lucky Brown ha sido mayormente positiva, subrayando su potencial de proyección internacional. Más allá de los números, se lo considera un artista en evolución, con las herramientas necesarias para representar al reggaetón chileno en escenarios más grandes y competitivos.***
""")