import streamlit as st
from PIL import Image

# --- PAGE CONFIG ---
st.set_page_config(page_title="Veera Raghavulu Bathula Portfolio", page_icon="📊", layout="wide")

# --- DATA EXTRACTION FROM RESUME ---
NAME = "Veera Raghavulu Bathula" [cite: 1]
EMAIL = "veeraraghavulubathula@gmail.com" [cite: 2]
LOCATION = "Magdeburg, Germany" [cite: 3]
PHONE = "015566091979" [cite: 3]

# --- SIDEBAR SETUP ---
with st.sidebar:
    st.title(NAME) [cite: 1]
    st.write(f"📍 {LOCATION}") [cite: 3]
    st.write(f"📧 {EMAIL}") [cite: 2]
    st.write(f"📞 {PHONE}") [cite: 3]
    st.markdown("---")
    st.write("🔗 [LinkedIn](https://linkedin.com)") [cite: 6]
    st.write("💻 [GitHub](https://github.com)") [cite: 4]
    st.write("📊 [Tableau](https://public.tableau.com)") [cite: 4]
    st.write("🧠 [HuggingFace](https://huggingface.co)") [cite: 4]

# --- HERO SECTION ---
st.title(f"Hi, I'm {NAME} 👋") [cite: 1]
st.subheader("Data Engineer | M.Sc. Digital Engineering Student") [cite: 7, 21]
st.write("Data Engineer with over 3 years of experience building clean, traceable cloud data pipelines for analytics and AI. ")

# --- ABOUT ME ---
st.header("👩‍💻 Professional Summary")
st.write("""
I specialize in collecting, cleaning, and preparing data using Python, Spark, and SQL. [cite: 8, 9] 
Currently, I am a Master's student at Otto-von-Guericke-Universität Magdeburg focusing on Data Engineering and AI. [cite: 10, 21, 22] 
Previously, I optimized ETL processes at Deloitte using AWS and Airflow to enhance report performance. [cite: 9]
""")

# --- SKILLS ---
st.header("🧠 Technical Skills")
col1, col2 = st.columns(2)
with col1:
    st.markdown("**Programming & Data Management**")
    st.write("- Python, SQL, Shell Scripting (Unix/Linux), Scala (Spark) [cite: 12]")
    st.write("- Informatica (IICS & PowerCenter), AWS S3, Google BigQuery, Snowflake [cite: 13]")
    st.write("- MongoDB, Oracle, MS SQL Server, Athena [cite: 8, 13]")
with col2:
    st.markdown("**Big Data, ML & Tools**")
    st.write("- PySpark, Apache Airflow, Docker, Pandas, NumPy [cite: 14]")
    st.write("- Scrapy, Selenium, API-Integration, Web Scraping [cite: 16]")
    st.write("- Power BI, Tableau, Qlik Sense [cite: 15, 42]")

# --- EXPERIENCE ---
st.header("💼 Work Experience")

# Current Role
st.subheader("Werkstudent Data Engineering | IWH - Halle") [cite: 26, 27]
st.write("*12/2024 – Present*") [cite: 26]
st.markdown("""
- Developing scalable web-scraping pipelines for European real estate data using Scrapy and Selenium. [cite: 28, 29]
- Processing unstructured HTML into MongoDB/CSV datasets using Python and Regex. [cite: 30]
- Automating data cleaning and quality checks for empirical research. [cite: 31, 32]
""")

# Previous Role
st.subheader("Data / ETL Engineer | Deloitte") [cite: 34, 35]
st.write("*09/2021 – 03/2024*") [cite: 34]
st.markdown("""
- Built a central data hub and implemented 150+ ETL pipelines using Informatica and Airflow. [cite: 36]
- Modeled Star and Snowflake schemas in AWS Athena and MS SQL Server. [cite: 36]
- Automated data quality checks and Unix scripting to reduce manual effort. [cite: 37, 39]
""")

# --- PROJECTS ---
st.header("🚀 Key Projects")
p_col1, p_col2 = st.columns(2)

with p_col1:
    st.subheader("Fine-tuning OpenAI Whisper") [cite: 46]
    st.write("Built a PyTorch/Hugging Face pipeline for Bengali & Telugu ASR using PEFT/LoRA. [cite: 48, 50]")
    st.subheader("Data-Job-Trends Dashboard") [cite: 61]
    st.write("Developed a Power BI dashboard using DAX and Power Query to visualize global job trends. [cite: 63, 65, 66]")

with p_col2:
    st.subheader("GCP & BigQuery Analytics") [cite: 54]
    st.write("Created a churn prediction workflow integrating SAP data into BigQuery. [cite: 56, 57]")
    st.subheader("NYC Taxi Data Ingestion") [cite: 68]
    st.write("Containerized PostgreSQL instance with Docker for CSV data ingestion via SQLAlchemy. [cite: 70, 71]")

# --- EDUCATION ---
st.header("🎓 Education")
st.write("**M.Sc. Digital Engineering** | Otto-von-Guericke-Universität Magdeburg (2024 - Present) [cite: 21, 22]")
st.write("**B.Tech Mechanical Engineering** | Lakireddy Bali Reddy College of Engineering (2017 - 2021) [cite: 23, 24]")

# --- CERTIFICATIONS ---
st.header("🏅 Certifications")
st.write("- Google Associate Cloud Engineer [cite: 79]")
st.write("- Microsoft Certified: Azure Fundamentals (AZ-900) [cite: 78]")
st.write("- Informatica IICS & PowerCenter Expert Level [cite: 80, 81]")
st.write("- Deep Learning with PyTorch & LLMs in Python (Datacamp) [cite: 76, 77]")

st.write("---")
st.write("Designed by Veera Raghavulu Bathula ")