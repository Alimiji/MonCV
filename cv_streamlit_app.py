import streamlit as st
from PIL import Image
import base64

# ----- CONFIGURATION -----
NAME = "Ali Mijiyawa"
TITLE = "Data Scientist & MLOps Engineer"
EMAIL = "a.mijiyawa@gmail.com"
PHONE = "514-261-9750"
LOCATION = "Montréal, Canada"
LINKEDIN = "https://linkedin.com/in/ali-mijiyawa-946609162"
GITHUB = "https://github.com/Alimiji"
CV_PDF_PATH = "MonCV.pdf"

# ----- FONCTIONS UTILES -----
def load_pdf(file_path):
    with open(file_path, "rb") as f:
        base64_pdf = base64.b64encode(f.read()).decode('utf-8')
    pdf_display = f'<a href="data:application/pdf;base64,{base64_pdf}" download="{file_path}">📄 Télécharger mon CV (PDF)</a>'
    return pdf_display

# ----- PAGE CONFIG -----
st.set_page_config(page_title="CV - Ali Mijiyawa", page_icon=":briefcase:", layout="wide")

# ----- HEADER -----
st.title(NAME)
st.subheader(TITLE)
st.write(f"📍 {LOCATION} | ✉️ {EMAIL} | 📞 {PHONE}")
st.markdown(f"🔗 [GitHub]({GITHUB}) | [LinkedIn]({LINKEDIN})")
st.markdown(load_pdf(CV_PDF_PATH), unsafe_allow_html=True)

# ----- À PROPOS -----
st.header("À propos de moi")
st.write("""
Scientifique de données passionné par l'intelligence artificielle et la modélisation, avec une expertise reconnue en NLP, LLMs et MLOps. 
Je conçois et déploie des solutions intelligentes en collaboration avec des équipes pluridisciplinaires.
""")

# ----- COMPÉTENCES -----
st.header("Compétences techniques")
st.write("""
- **Langages** : Python, SQL, DAX
- **IA/ML** : Scikit-learn, PyTorch, TensorFlow, Hugging Face
- **MLOps** : Docker, FastAPI, MLflow, DVC, Airflow
- **Big Data** : PySpark, Azure ML, AWS ML, Databricks
- **Bases de données** : Neo4j, PostgreSQL
- **Outils** : Power BI, GitHub, Unix/Linux
""")

# ----- EXPÉRIENCE -----
st.header("Expérience professionnelle")
st.subheader("Stagiaire en science des données - Ciena (2024)")
st.write("""
- Développement de dashboards Power BI et pipelines ETL (SQL, Python)
- Fine-tuning de LLMs (T5, GPT-3) pour assistant GPT interne
- Présentation des KPIs et recommandations stratégiques
""")

st.subheader("Stagiaire en analyse des données - Arm (2023)")
st.write("""
- Déploiement de systèmes MLOps sous Azure
- Tableaux RH interactifs avec Power BI
""")

st.subheader("Enseignant auxiliaire (UQÀM)")
st.write("""
- Cours pratiques sur SQL, NLP, Transformers
- Encadrement de projets Hugging Face
""")

# ----- PROJETS -----
st.header("Projets de science des données")
st.markdown("- 🎬 **Système de recommandation de films** – [Notebook](https://github.com/Alimiji)")
st.markdown("- 🏢 **Pipeline Big Data LMIA** – Pyspark, Hadoop")
st.markdown("- 🖼️ **Classification d’images** – Vision par ordinateur")

# ----- FORMATION -----
st.header("Formation")
st.write("""
- 🎓 M.Sc. Intelligence Artificielle – UQÀM (2023–2025)
- 🎓 AEC IA – Collège Bois-de-Boulogne (2021–2023)
- 🎓 DEP – Institut Teccart (2017–2019)
- 🎓 B.Sc. Mathématiques – Université de Lomé (2009–2014)
""")

# ----- CERTIFICATIONS -----
st.header("Certifications")
st.markdown("- ✅ Azure Data Fundamentals (DP-900) – Microsoft")
st.markdown("- ✅ Python for Everybody – Coursera / University of Michigan")

# ----- PUBLICATION -----
st.header("Publications")
st.markdown("- 📝 *The Best of Both Worlds: Exploring Wolofal in NLP* – AbjadNLP 2025")
st.markdown("  [Voir sur ACL Anthology](https://aclanthology.org/2025.abjadnlp-1.1/)")

# ----- CONTACT -----
st.header("Contact")
st.write("Des références sont disponibles sur demande. N'hésitez pas à me contacter via email ou LinkedIn.")
