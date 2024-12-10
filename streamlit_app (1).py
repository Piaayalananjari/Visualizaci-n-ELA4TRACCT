import streamlit as st
import pandas as pd
import json


st.markdown("""
    <style>
    .main { background-color: #F8F10FC; }
    .header { color: #B52EDB; font-size: 30px; font-weight: bold; }
    .subheader { color: #965EDB; font-size: 24px; font-weight: bold; }
    [data-testid="stExpander"] > div > div {
        background-color: #DB2EBA;
        border-radius: 10px;
        padding: 10px;
        border: 1px solid #DB2E52;
    }
    [data-testid="stSidebar"] {
        background-color: #DB77C8;
        color: #333333;
    }
    .stButton>button {
        background-color: #DB422E;
        color: white;
        border-radius: 5px;
        border: none;
        padding: 8px 16px;
        font-weight: bold; font-size: 16px;
    }
    .stButton>button:hover {
        background-color: #965EDB;
    }
    </style>
""", unsafe_allow_html=True)


with open('data_referencias.json', encoding='utf-8') as file:
    data = json.load(file)


def format_methodology(methodology):
    if isinstance(methodology, dict):
        formatted_methodology = ""
        for key, value in methodology.items():
            formatted_methodology += f"🔹 **{key}:** {value}\n"
        return formatted_methodology
    return "No hay información disponible sobre la metodología."


def format_programs(programs):
    if isinstance(programs, list):
        formatted_programs = ""
        for program in programs:
            if isinstance(program, dict): 
                formatted_programs += f"🔹 **{program.get('Nombre', 'No especificado')}**\n"
                formatted_programs += f"- **Descripción:** {program.get('Descripción', 'No disponible')}\n"
                if "Componentes" in program:
                    formatted_programs += "- **Componentes:**\n"
                    for key, value in program["Componentes"].items():
                        formatted_programs += f"  - {key}: {value}\n"
            else:  
                formatted_programs += f"🔹 {program}\n"
        return formatted_programs
    return "No hay programas propuestos."


def format_conclusions(conclusions):
    if isinstance(conclusions, dict):
        formatted_conclusions = ""
        for key, value in conclusions.items():
            formatted_conclusions += f"🔹 **{key}:** {value}\n"
        return formatted_conclusions
    elif isinstance(conclusions, str):
        return conclusions
    return "No hay conclusiones disponibles."


def process_data_for_visualization(data):
    programs_by_stage = {stage: [] for stage in data}
    for stage, references in data.items():
        for ref in references:
            if "Programas Propuestos" in ref:
                for program in ref["Programas Propuestos"]:
                    if isinstance(program, dict): 
                        programs_by_stage[stage].append({
                            "Título": ref.get("Título", "No especificado"),
                            "Nombre del Programa": program.get("Nombre", "No especificado"),
                            "Descripción": program.get("Descripción", "No disponible"),
                        })
    return programs_by_stage


st.sidebar.header("🔍 Selecciona una opción")
options = ["🏠 Inicio", "📚 Explorar Referencias", "📊 Visualización de Datos","📝 Reflexión Final"]
selected_option = st.sidebar.radio("Navega entre las opciones:", options)


if selected_option == "🏠 Inicio":
    st.markdown("<div class='header'>📚 Bienvenida a la Plataforma de Visualización 📚</div>", unsafe_allow_html=True)
    st.markdown("""
    ### 🧐 Contexto del Proyecto
    Este proyecto forma parte de la investigación **"Equidad de Género en Ingeniería y Ciencias: Buenas Prácticas en Educación Superior"**, desarrollado por:
    - **Estudiante**: Pía Ayala Nanjari (Ingeniería Civil).
    - **Docente Guía**: Isabel Hilliger Carrasco.
    - **Institución**: Pontificia Universidad Católica de Chile.
    - **Año**: 2024.

    ### 🔎 Definiciones de las Etapas Investigadas
    - **Atracción**: Iniciativas para inspirar a niñas y mujeres jóvenes hacia STEM.
    - **Admisión**: Programas que facilitan el ingreso de mujeres a STEM.
    - **Retención**: Estrategias para garantizar que las mujeres permanezcan en STEM.
    - **Desarrollo**: Actividades de mentoría, networking y formación profesional.

    ### 🛠️ Metodología
    - **Identificación de referencias** relevantes a nivel global.
    - **Clasificación** en etapas clave (Atracción, Admisión, Retención, Desarrollo).
    - **Análisis cualitativo y cuantitativo** para identificar barreras y facilitadores.

    ¡Explora las siguientes secciones para obtener más detalles y visualizaciones! ✨
    """)


elif selected_option == "📚 Explorar Referencias":
    st.markdown("<div class='header'>📚 Exploración de Referencias 📚</div>", unsafe_allow_html=True)
    total_titles = sum(len(v) for v in data.values())
    st.markdown(f"### 📖 Total de Títulos Analizados: {total_titles}")
    st.markdown("Selecciona una etapa para explorar sus referencias asociadas.")
    
    stage_selected = st.sidebar.selectbox("Selecciona una etapa para explorar", [""] + list(data.keys()))
    if stage_selected:
        st.markdown(f"## Referencias para la Etapa: {stage_selected}")
        references = data.get(stage_selected, [])
        for ref in references:
            with st.expander(ref["Título"]):
                st.write(f"**Referencia:** {ref.get('Referencia', 'No disponible')}")
                st.write(f"**Resumen:** {ref.get('Resumen', 'No disponible')}")
                st.write(f"**Año:** {ref.get('Año', 'No especificado')}")
                st.write(f"**Zona geográfica:** {ref.get('Zona geográfica', 'No especificada')}")
                if "Metodología" in ref:
                    st.write("**Metodología:**")
                    st.markdown(format_methodology(ref["Metodología"]))
                if "Programas Propuestos" in ref:
                    st.write("**Programas Propuestos:**")
                    st.markdown(format_programs(ref["Programas Propuestos"]))
                if "Hallazgos y Contribuciones" in ref:
                    st.write("**Hallazgos y Contribuciones:**")
                    for key, value in ref["Hallazgos y Contribuciones"].items():
                        st.write(f"- **{key}:** {value}")
                if "Conclusiones y Reflexiones sobre la Metodología" in ref:
                    st.write("**Conclusiones y Reflexiones sobre la Metodología:**")
                    st.markdown(format_conclusions(ref["Conclusiones y Reflexiones sobre la Metodología"]))


elif selected_option == "📊 Visualización de Datos":
    programs_by_stage = process_data_for_visualization(data)
    st.markdown("<div class='header'>📊 Visualización de Iniciativas 📊</div>", unsafe_allow_html=True)
    st.markdown("""
    ### 📋 Descripción
    En esta sección, se presentan tablas interactivas de los **programas propuestos** organizados por etapa.

    🔍 Selecciona una etapa para visualizar los programas asociados.
    """)

    for stage, programs in programs_by_stage.items():
        if programs:
            st.markdown(f"#### 📌 Programas Propuestos en la Etapa: {stage}")
            df = pd.DataFrame(programs)
            st.markdown(f"🔍 **Total de Programas en esta etapa:** {len(df)}")
            st.dataframe(df, use_container_width=True)
        else:
            st.markdown(f"#### 📌 No se encontraron programas en la Etapa: {stage}")

elif selected_option == "📝 Reflexión Final":
    st.markdown("<div class='header'>📝 Reflexión Final sobre la Investigación 📝</div>", unsafe_allow_html=True)
    st.markdown("""
    # Reflexión Final sobre la Investigación en Equidad de Género en STEM

    ## Introducción

    La equidad de género en las disciplinas STEM (Ciencia, Tecnología, Ingeniería y Matemáticas) no es solo una meta ética, sino una necesidad estratégica para abordar los desafíos del siglo XXI. A pesar de los avances logrados en las últimas décadas, las mujeres continúan enfrentando barreras sustanciales para acceder, permanecer y progresar en estas áreas. Este proyecto aborda esta problemática a través de una revisión sistemática y exhaustiva de la literatura existente, con el objetivo de identificar las barreras persistentes, analizar los programas implementados y proponer soluciones efectivas.

    Basado en un marco metodológico riguroso, este estudio clasifica las iniciativas en cuatro etapas fundamentales del ciclo educativo y profesional: **Atracción**, **Admisión**, **Retención** y **Desarrollo**. A través de esta estructura, se logra comprender de manera más precisa las áreas donde las mujeres son desproporcionadamente desfavorecidas y dónde las intervenciones pueden tener mayor impacto.

    ---

    ## Metodologías y Diseño de la Revisión

    El éxito de una revisión sistemática depende de la selección y análisis cuidadoso de las fuentes, así como de la implementación de estrategias claras para extraer, categorizar y evaluar la información relevante. En este proyecto, se adoptaron las siguientes metodologías:

    1. **Selección de Fuentes de Datos**:
        - Se recopilaron alrededor de 56 estudios de casos, informes técnicos, artículos académicos y evaluaciones de programas. Las fuentes abarcaron tanto investigaciones longitudinales como análisis específicos a nivel de instituciones y regiones.
        - La inclusión de datos cualitativos (entrevistas, testimonios y estudios de caso) complementó los hallazgos cuantitativos (estadísticas de matrícula, tasas de deserción y resultados de encuestas).

    2. **Criterios de Clasificación**:
        - Cada referencia se clasificó dentro de una de las cuatro etapas previamente definidas, permitiendo un análisis organizado de las barreras y estrategias específicas.
        - Se aplicaron herramientas de análisis temático para identificar patrones recurrentes en los desafíos y soluciones propuestos.

    3. **Estrategias Implementadas en la Revisión**:
        - **Análisis Transversal:** Se compararon hallazgos entre diferentes contextos geográficos, considerando factores socioeconómicos y culturales.
        - **Análisis Longitudinal:** Estudios que abarcan periodos prolongados fueron evaluados para identificar tendencias y cambios a lo largo del tiempo.
        - **Mapeo de Actores Clave:** Se identificaron los roles de instituciones educativas, gobiernos, organizaciones internacionales y empresas en el diseño y ejecución de programas.

    ---

    ## Hallazgos Principales

    La revisión permitió identificar una serie de barreras persistentes y desafíos, clasificados por etapa. Cada hallazgo se enriquece con ejemplos específicos y datos clave extraídos de las referencias analizadas.

    ### **1. Atracción: Generando Interés en STEM**

    Uno de los mayores retos en esta etapa es la falta de interés inicial en STEM entre niñas y mujeres jóvenes, influenciado por:

    - **Estereotipos de Género:** Desde edades tempranas, las niñas enfrentan mensajes culturales que asocian STEM con habilidades "masculinas". Por ejemplo, estudios en Estados Unidos y Europa muestran que más del 70% de las niñas perciben que las matemáticas son "difíciles" o "no interesantes" debido a la falta de modelos de rol.
    - **Falta de Representación Femenina:** Las niñas rara vez ven a mujeres científicas o ingenieras destacadas en los currículos escolares o en los medios.

    **Estrategias Implementadas:**
    - **Campañas de Visibilidad Temprana:** Programas como "Girls Who Code" y "STEM Ambassadors" han logrado un impacto significativo. Estas iniciativas incluyen visitas escolares, talleres interactivos y charlas inspiradoras lideradas por mujeres profesionales en STEM.
    - **Revisión de Currículos Escolares:** En países como Suecia y Finlandia, se han diseñado programas educativos que integran referencias explícitas a mujeres científicas, como Marie Curie o Rosalind Franklin, para inspirar a las niñas.

    ### **2. Admisión: Facilitando el Ingreso**

    El acceso de mujeres a programas de STEM en instituciones de educación superior sigue siendo limitado, especialmente en regiones con menores recursos económicos. Entre las barreras identificadas se encuentran:

    - **Pruebas de Admisión Estandarizadas:** Diseñadas sin considerar las diferencias de género en la preparación académica y social, estas pruebas tienden a favorecer a los hombres.
    - **Falta de Apoyo Financiero:** En muchos países, las becas STEM no abordan las barreras adicionales que enfrentan las mujeres, como responsabilidades familiares.

    **Estrategias Implementadas:**
    - **Políticas de Paridad de Género:** Universidades en Canadá y Australia han introducido cuotas de género para garantizar una representación mínima de mujeres en programas de ingeniería y tecnología.
    - **Becas Exclusivas para Mujeres:** Iniciativas como "Women in Tech Scholarships" ofrecen apoyo financiero dirigido exclusivamente a mujeres interesadas en STEM, cubriendo no solo la matrícula, sino también costos adicionales como cuidado infantil.

    ### **3. Retención: Superando Barreras en el Camino**

    Aunque muchas mujeres logran ingresar a STEM, una proporción significativa abandona sus estudios o carreras debido a:

    - **Ambientes Hostiles:** Estudios en América Latina y Asia muestran que las mujeres enfrentan discriminación directa e indirecta en aulas y laboratorios dominados por hombres.
    - **Falta de Mentoría:** La ausencia de modelos femeninos y mentores accesibles limita la capacidad de las estudiantes para navegar los desafíos académicos y profesionales.

    **Estrategias Implementadas:**
    - **Programas de Mentoría:** Redes como "Lean In Circles" y "MentorHer" han conectado a miles de mujeres con mentoras que ofrecen orientación académica y profesional.
    - **Capacitación en Diversidad:** Universidades en Noruega y Alemania han implementado talleres obligatorios para profesores y estudiantes, enfocados en crear ambientes inclusivos.

    ### **4. Desarrollo: Promoviendo Liderazgo y Progreso Profesional**

    En esta etapa, las mujeres enfrentan barreras para avanzar hacia roles de liderazgo o acceder a programas de posgrado, incluyendo:

    - **Desigualdad Salarial:** A nivel global, las mujeres en STEM ganan entre un 15% y un 25% menos que sus homólogos masculinos.
    - **Falta de Redes de Apoyo:** Las mujeres tienen menos acceso a redes profesionales que faciliten el avance en sus carreras.

    **Estrategias Implementadas:**
    - **Programas de Liderazgo:** Talleres como "Women in Leadership" han demostrado ser efectivos para aumentar la confianza y las habilidades de liderazgo entre las participantes.
    - **Redes Profesionales:** Grupos como "Society of Women Engineers" proporcionan oportunidades de networking, becas y recursos educativos.

    ---

    ## Reflexión y Sugerencias Futuras

    Aunque los resultados de esta investigación son alentadores, queda mucho por hacer. Entre las recomendaciones clave se encuentran:

    - **Fortalecer Políticas Públicas:** Los gobiernos deben priorizar la equidad de género en STEM como parte de sus agendas educativas y laborales.
    - **Ampliar el Alcance de los Programas:** Es necesario adaptar las iniciativas a contextos culturales y económicos diversos, especialmente en países en desarrollo.
    - **Promover la Investigación Continua:** Evaluar el impacto de las intervenciones a largo plazo permitirá identificar mejores prácticas y áreas de mejora.

    ---

    ## Reflexión Final

    La equidad de género en STEM es un objetivo alcanzable, pero requiere un esfuerzo colectivo y sostenido. Este proyecto demuestra que las intervenciones específicas, respaldadas por datos y análisis rigurosos, pueden transformar significativamente el panorama para las mujeres en estas disciplinas. Es un llamado a la acción para que gobiernos, instituciones educativas y la sociedad trabajen juntos hacia un futuro más inclusivo y equitativo.
    """)



