import streamlit as st
from PIL import Image

# --- PAGE CONFIG ---
st.set_page_config(page_title="Veera Raghavulu Bathula Portfolio", page_icon="📊", layout="wide")

# --- DATA FROM RESUME ---
NAME = "Veera Raghavulu Bathula"
EMAIL = "veeraraghavulubathula@gmail.com"
LOCATION = "Magdeburg, Germany"
PHONE = "015566091979"

# --- SIDEBAR SETUP ---
with st.sidebar:
    st.title(NAME)
    st.write(f"📍 {LOCATION}")
    st.write(f"📧 {EMAIL}")
    st.write(f"📞 {PHONE}")
    st.markdown("---")
    # Replace these with your actual links
    st.write("🔗 [LinkedIn](https://linkedin.com/in/veeraraghavulu)")
    st.write("💻 [GitHub](https://github.com/Mech123)")
    st.write("📊 [Tableau](https://public.tableau.com)")
    st.write("🧠 [HuggingFace](https://huggingface.co)")

# --- HERO SECTION ---
st.title(f"Hi, I'm {NAME} 👋")
st.subheader("Data Engineer | M.Sc. Digital Engineering Student")
st.write("Data Engineer with over 3 years of experience building clean, traceable cloud data pipelines for analytics, dashboards, and AI applications.")

# --- ABOUT ME ---
st.header("👩‍💻 Professional Summary")
st.write("""
I have over 3 years of professional experience in building clean, traceable cloud data pipelines. 
Currently, I am a Master's student at Otto-von-Guericke-Universität Magdeburg focusing on Data Engineering and Artificial Intelligence. 
I specialize in collecting and preparing data using Python, Spark, and SQL to improve the performance and stability of productive reports.
""")

# --- SKILLS ---
st.header("🧠 Technical Skills")
col1, col2 = st.columns(2)
with col1:
    st.markdown("**Programming & Data Management**")
    st.write("- Python, C, SQL, Shell Scripting (Unix/Linux), Scala (Spark)")
    st.write("- Informatica (IICS & PowerCenter), AWS S3, Google BigQuery, Athena")
    st.write("- Snowflake, SAP Data Warehouse, ETL/ELT, SCD (Typ 1/2)")
with col2:
    st.markdown("**Big Data, ML & Tools**")
    st.write("- NumPy, Pandas, Matplotlib, Seaborn, PySpark, Docker, Apache Airflow")
    st.write("- Web Scraping (Scrapy, Selenium, BeautifulSoup, Zyte API)")
    st.write("- Power BI, Qlik Sense, Tableau, MS Excel")

# --- EXPERIENCE ---
st.header("💼 Work Experience")

# Current Role
st.subheader("Werkstudent Data Engineering | IWH - Halle")
st.write("*12/2024 – Present*")
st.markdown("""
- Developing scalable web-scraping pipelines for real estate and economic data using Scrapy and Selenium.
- Processing unstructured HTML into MongoDB and CSV datasets using Python, Regex, and Pandas.
- Implementing data quality checks to ensure reproducible workflows for research projects.
""")

# Previous Role
st.subheader("Data / ETL Engineer | Deloitte")
st.write("*09/2021 – 03/2024*")
st.markdown("""
- Built a central data hub and implemented over 150 ETL pipelines using Informatica and Airflow.
- Modeled Star and Snowflake schemas in Oracle, MS SQL Server, and AWS Athena.
- Automated recurring loading and control processes with Unix scripts and Python to reduce manual effort.
""")

# --- PROJECTS ---
st.header("🚀 Key Projects")
p_col1, p_col2 = st.columns(2)

with p_col1:
    st.subheader("Fine-tuning OpenAI Whisper")
    st.write("Developed a reproducible training pipeline for Bengali & Telugu ASR using PyTorch, Hugging Face, and PEFT (LoRA).")
    st.subheader("Data-Job-Trends Dashboard")
    st.write("Created a Power BI dashboard using DAX and Power Query to visualize global job trends and KPIs.")

with p_col2:
    st.subheader("GCP & BigQuery Analytics")
    st.write("Built an analytics workflow for churn prediction using BigQuery SQL and Python, integrating SAP Data Warehouse sources.")
    st.subheader("NYC Taxi Data Ingestion")
    st.write("Set up a containerized PostgreSQL instance with Docker for CSV data ingestion via Python and SQLAlchemy.")

# --- EDUCATION ---
st.header("🎓 Education")
st.write("**M.Sc. Digital Engineering (Informatics)** | Otto-von-Guericke-Universität Magdeburg (2024 - Present)")
st.write("**B.Tech Mechanical Engineering** | Lakireddy Bali Reddy College of Engineering (2017 - 2021)")

# --- CERTIFICATIONS ---
st.header("🏅 Certifications")
st.write("- Google Associate Cloud Engineer Learning Path")
st.write("- Microsoft Certified: Azure Fundamentals (AZ-900)")
st.write("- Informatica Cloud Data Integration Services (IICS)")
st.write("- Deep Learning with PyTorch & LLMs in Python (Datacamp)")

st.write("---")
st.write("Designed by Veera Raghavulu Bathula")