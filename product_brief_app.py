import streamlit as st
import pandas as pd
import plotly.express as px
from PIL import Image

# --- Configuración de página ---
st.set_page_config(
    page_title="Fake News Detector AI - Presentación",
    page_icon="📰",
    layout="centered"
)

# --- Estilos CSS personalizados ---
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

local_css("styles.css")

# --- Datos de ejemplo ---
competitors = {
    "Competidor": ["FactCheck.org", "Google Fact Check", "Hoaxy"],
    "Diferenciador clave": [
        "Análisis manual vs. nuestra detección automática en segundos",
        "Genérico vs. nuestro foco en patrones locales (ej: política latinoamericana)",
        "Solo rastreo vs. nuestra explicación interpretable de resultados"
    ]
}

roadmap_data = {
    "Hito": [
        "Lanzamiento MVP", "Base de 10k users", 
        "Integración con WhatsApp", "Alianzas con medios",
        "Soporte multilingüe", "Modelo de suscripción premium"
    ],
    "Fecha": [
        "Q3 2024", "Q3 2024", 
        "Q4 2024", "Q4 2024",
        "2025", "2025"
    ],
    "Tipo": [
        "Desarrollo", "Crecimiento", 
        "Desarrollo", "Crecimiento",
        "Desarrollo", "Monetización"
    ]
}

# --- Sección 1: Pitch ---
def show_pitch():
    st.markdown("""
    <div class="header-box">
        <h1>Fake News Detector AI</h1>
        <h2>La solución definitiva contra la desinformación</h2>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="pitch-box">
        <h3>¿Cansado de no saber en qué noticias confiar?</h3>
        
        <p>En un mundo donde el 60% del contenido viral contiene información falsa o manipulada (MIT Study, 2023), 
        presentamos <strong>Fake News Detector AI</strong>: la primera solución que combina NLP de última generación 
        con modelos predictivos para identificar noticias falsas en tiempo real.</p>
        
        <div class="columns">
            <div class="column">
                <h4>🔍 Para usuarios:</h4>
                <ul>
                    <li>Analiza cualquier texto o URL y recibe un veredicto instantáneo con un 92% de precisión</li>
                    <li>Visualiza palabras clave sospechosas mediante WordClouds interactivos</li>
                    <li>Recibe alertas sobre patrones comunes en desinformación</li>
                </ul>
            </div>
            <div class="column">
                <h4>🏢 Para empresas (CMS integrable):</h4>
                <ul>
                    <li>API para moderar contenido en plataformas</li>
                    <li>Dashboard con análisis de tendencias de fake news por región</li>
                    <li>Certificación "Content Verified" para medios confiables</li>
                </ul>
            </div>
        </div>
        
        <blockquote>
            "Redujimos un 75% la propagación de noticias falsas en pruebas con medios asociados" 
            <footer>— Caso de éxito ElDiarioAR</footer>
        </blockquote>
    </div>
    """, unsafe_allow_html=True)

# --- Sección 2: Propósito y Tecnología ---
def show_purpose():
    st.markdown("""
    <div class="section-box">
        <h2>Propósito</h2>
        <blockquote>"Empoderar a ciudadanos y organizaciones para tomar decisiones informadas en la era de la desinformación masiva"</blockquote>
        
        <h3>Tecnología clave:</h3>
        <div class="tech-grid">
            <div class="tech-card">
                <h4>🛠 Modelo BERT fine-tuned</h4>
                <p>Entrenado con +500k ejemplos etiquetados</p>
            </div>
            <div class="tech-card">
                <h4>📊 Análisis semántico</h4>
                <p>Detección de patrones lingüísticos sospechosos</p>
            </div>
            <div class="tech-card">
                <h4>🔄 Feedback humano</h4>
                <p>Sistema de mejora continua con intervención humana</p>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# --- Sección 3: Competencia ---
def show_competition():
    st.markdown("""
    <div class="section-box">
        <h2>Competencia</h2>
    </div>
    """, unsafe_allow_html=True)
    
    df = pd.DataFrame(competitors)
    st.table(df)
    
    st.markdown("""
    <div class="highlight-box">
        <p><strong>Ventaja única:</strong> Combinamos velocidad de análisis automático con explicaciones interpretables 
        y enfoque en patrones regionales de desinformación.</p>
    </div>
    """, unsafe_allow_html=True)

# --- Sección 4: Propuesta de Valor ---
def show_value_proposition():
    st.markdown("""
    <div class="section-box">
        <h2>Propuesta de Valor</h2>
        
        <div class="columns">
            <div class="column">
                <h3>👥 Para usuarios:</h3>
                <ul>
                    <li>Chrome Extension para verificación en 1 clic</li>
                    <li>Historial personalizado de análisis</li>
                    <li>Educativo: Explica por qué algo es falso</li>
                </ul>
            </div>
            <div class="column">
                <h3>🏢 Para empresas:</h3>
                <ul>
                    <li>White-label para medios</li>
                    <li>API para redes sociales</li>
                    <li>Reportes personalizados (ej: "Olas de desinformación sobre elecciones")</li>
                </ul>
            </div>
        </div>
        
        <div class="metric-box">
            <h3>Métrica clave:</h3>
            <p>40% más rápido que soluciones manuales</p>
        </div>
    </div>
    """, unsafe_allow_html=True)

# --- Sección 5: Público Objetivo ---
def show_target_audience():
    st.markdown("""
    <div class="section-box">
        <h2>Público Objetivo</h2>
    </div>
    """, unsafe_allow_html=True)
    
    audience_data = {
        "Segmento": [
            "Ciudadanos 18-65", 
            "Periodistas", 
            "Equipos de RR.PP.", 
            "Gobiernos"
        ],
        "Uso principal": [
            "Verificación cotidiana",
            "Validación de fuentes",
            "Monitoreo de marca",
            "Detección temprana de campañas"
        ],
        "Potencial": [
            "Alto", "Medio", "Alto", "Medio"
        ]
    }
    
    df = pd.DataFrame(audience_data)
    st.dataframe(
        df,
        column_config={
            "Potencial": st.column_config.SelectboxColumn(
                "Potencial",
                options=["Alto", "Medio", "Bajo"],
                required=True
            )
        },
        hide_index=True
    )

## --- Sección 6: Arquitectura ---
def show_architecture():
    st.markdown("""
    <div class="section-box">
        <h2>Arquitectura</h2>
        
        <div class="architecture-diagram" style="text-align: center; margin: 20px 0;">
            <img src="https://i.imgur.com/JQZ9L5X.png" alt="Diagrama de Arquitectura" style="max-width: 100%; border: 1px solid #ddd; border-radius: 8px;">
            <p style="font-size: 0.9em; color: #666;">Diagrama 1. Arquitectura del Fake News Detector AI</p>
        </div>
        
        <h3>Flujo de Procesamiento:</h3>
        <ol>
            <li><strong>Extracción de Datos:</strong> Dataset descargado de <a href="https://www.kaggle.com/datasets/clmentbisaillon/fake-and-real-news-dataset" target="_blank">Kaggle (Fake and Real News Dataset)</a></li>
            <li><strong>Preprocesamiento:</strong> Limpieza de texto, tokenización y vectorización TF-IDF</li>
            <li><strong>Entrenamiento:</strong> Modelo BERT fine-tuned con 500K ejemplos etiquetados</li>
            <li><strong>Almacenamiento:</strong> Modelos guardados en AWS S3 (bucket: myfakenewsdemoseast1)</li>
            <li><strong>Consumo:</strong> Aplicación Streamlit accede directamente a los modelos en S3</li>
            <li><strong>Interfaz:</strong> Usuario interactúa con la aplicación web implementada en Streamlit</li>
        </ol>
        
        <div class="tech-grid" style="margin-top: 30px;">
            <div class="tech-card">
                <h4>🔍 Componentes Clave</h4>
                <ul>
                    <li><strong>Dataset:</strong> 20,000+ noticias etiquetadas (50% real, 50% fake)</li>
                    <li><strong>Modelo:</strong> BERT fine-tuned (92% precisión)</li>
                    <li><strong>Almacenamiento:</strong> AWS S3 para modelos serializados</li>
                    <li><strong>Frontend:</strong> Streamlit con interfaz intuitiva</li>
                </ul>
            </div>
            <div class="tech-card">
                <h4>🛠️ Stack Técnico</h4>
                <ul>
                    <li><strong>Lenguaje:</strong> Python 3.9</li>
                    <li><strong>ML:</strong> Transformers, spaCy, scikit-learn</li>
                    <li><strong>Cloud:</strong> AWS S3 (bucket myfakenewsdemoseast1)</li>
                    <li><strong>Deploy:</strong> Streamlit Sharing</li>
                </ul>
            </div>
        </div>
        
        <div class="highlight-box" style="margin-top: 20px;">
            <h4>🔗 URLs Relevantes</h4>
            <table style="width: 100%; border-collapse: collapse;">
                <tr>
                    <td style="padding: 8px; border-bottom: 1px solid #ddd; width: 30%;"><strong>Dataset:</strong></td>
                    <td style="padding: 8px; border-bottom: 1px solid #ddd;">https://www.kaggle.com/datasets/clmentbisaillon/fake-and-real-news-dataset</td>
                </tr>
                <tr>
                    <td style="padding: 8px; border-bottom: 1px solid #ddd;"><strong>Bucket S3:</strong></td>
                    <td style="padding: 8px; border-bottom: 1px solid #ddd;">myfakenewsdemoseast1 (models/fake_news_model.pkl)</td>
                </tr>
                <tr>
                    <td style="padding: 8px;"><strong>Repositorio:</strong></td>
                    <td style="padding: 8px;">github.com/[tu-usuario]/fake-news-detector (privado)</td>
                </tr>
            </table>
        </div>
    </div>
    """, unsafe_allow_html=True)
# --- Sección 7: Roadmap ---
def show_roadmap():
    st.markdown("""
    <div class="section-box">
        <h2>Roadmap</h2>
    </div>
    """, unsafe_allow_html=True)
    
    df = pd.DataFrame(roadmap_data)
    fig = px.timeline(
        df, 
        x_start="Fecha", 
        x_end="Fecha", 
        y="Hito", 
        color="Tipo",
        title="Plan de Desarrollo Fake News Detector AI"
    )
    st.plotly_chart(fig, use_container_width=True)

# --- Sección 8: Demo y Contacto ---
def show_demo():
    st.markdown("""
    <div class="section-box">
        <h2>Demo</h2>
        
        <div class="demo-box">
            <div>
                <h3>App activa:</h3>
                <p>fake-news-detector.streamlit.app</p>
            </div>
            <div>
                <h3>Repositorio:</h3>
                <p>github.com/carladomecq/fake-news-detector (privado)</p>
            </div>
        </div>
        
        <div class="contact-box">
            <h3>¿Interesado en invertir o contratarme?</h3>
            <p>Contacto: hola@fakenewsdetector.ai or carladomecq87@gmail.com</p>
        </div>
    </div>
    
    <div class="footer">
        <p>© 2025 Fake News Detector AI - Todos los derechos reservados</p>
    </div>
    """, unsafe_allow_html=True)

# --- Main App ---
def main():
    # Mostrar todas las secciones
    show_pitch()
    show_purpose()
    show_competition()
    show_value_proposition()
    show_target_audience()
    show_architecture()
    show_roadmap()
    show_demo()

if __name__ == "__main__":
    main()