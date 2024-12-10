# Plataforma de Visualización de Equidad de Género en STEM

Este proyecto es una herramienta interactiva diseñada para explorar, analizar y reflexionar sobre la equidad de género en las áreas de Ciencia, Tecnología, Ingeniería y Matemáticas (STEM). La plataforma combina visualizaciones dinámicas y análisis exhaustivos basados en una revisión sistemática de literatura científica.

## 📚 **Contexto del Proyecto**

La equidad de género en STEM es fundamental para construir un futuro inclusivo y sostenible. Este proyecto aborda la representación insuficiente de mujeres en STEM a través del análisis de 56 referencias bibliográficas que exploran iniciativas, barreras y facilitadores. El objetivo principal es proporcionar una herramienta que permita a investigadores, docentes y responsables de políticas analizar datos cualitativos y cuantitativos relacionados con la inclusión femenina en STEM, organizados en las siguientes **cuatro etapas clave**:

1. **Atracción**: Cómo inspirar a niñas y mujeres jóvenes hacia STEM.
2. **Admisión**: Estrategias que faciliten su ingreso a programas STEM.
3. **Retención**: Iniciativas para garantizar la permanencia en STEM.
4. **Desarrollo**: Promoción del liderazgo y progreso profesional.

## 🛠️ **Estructura y Funcionalidades**

La plataforma está estructurada en cuatro secciones principales, accesibles desde el menú de navegación lateral:

1. **🏠 Inicio**: Introducción al proyecto y su contexto. Explicación de las etapas clave investigadas. Detalle de la metodología utilizada, combinando análisis cualitativo y cuantitativo.
2. **📚 Explorar Referencias**: Permite navegar por las referencias organizadas según las etapas de investigación. Cada referencia muestra:
    - **Título**.
    - **Resumen**.
    - **Metodología** utilizada.
    - **Programas Propuestos** relacionados.
    - **Hallazgos y Contribuciones**.
    - **Conclusiones** clave.
3. **📊 Visualización de Datos**: Presenta visualizaciones interactivas organizadas por etapas:
    - Tablas interactivas con los programas propuestos en cada etapa.
    - Resumen de la cantidad de programas por etapa. Herramienta clave para identificar patrones en las iniciativas propuestas.
4. **📝 Reflexión Final**: Análisis exhaustivo de los hallazgos, reflexiones y recomendaciones. Detalle de las metodologías implementadas y su impacto. Identificación de barreras persistentes y sugerencias para futuras iniciativas.

## 📂 **Estructura del Proyecto**
├── data_referencias.json # Archivo con los datos de referencias bibliográficas. 
├── streamlit_app.py # Código principal del proyecto en Streamlit. 
├── README.md # Documento de introducción al proyecto.


## 🧑‍🔬 **Metodología**

La plataforma utiliza un enfoque sistemático para organizar y analizar los datos, con las siguientes estrategias:

1. **Revisión Sistemática de Literatura**: Revisión de más de 56 referencias relevantes para identificar barreras y facilitadores en STEM.
2. **Clasificación en Etapas**: Organización de referencias en Atracción, Admisión, Retención y Desarrollo.
3. **Visualización de Datos**: Tablas interactivas y resúmenes cuantitativos para explorar programas y estrategias clave.
4. **Reflexión Final**: Ensayo detallado basado en los resultados y análisis recopilados.

## 🚀 **Cómo Ejecutar el Proyecto**

### Prerrequisitos
- **Python 3.8 o superior.**
- Dependencias requeridas:
  - `streamlit`
  - `pandas`

### Instalación
1. Clonar este repositorio:
   ```bash
   git clone https://github.com/tu-repositorio.git
2. cd tu-repositorio
3. pip install -r requirements.txt (importante!!)

### Ejecución en la bash
1. colocar lo siguiente en la bash : streamlit run streamlit_app.py --server.enableCORS false --server.enableXsrfProtection false
2. Hacer click en:
 Local URL: http://localhost:8502

 (Este se encuentra público para su visualización)



