import streamlit as st
import pandas as pd
from datetime import datetime
import plotly.express as px
import plotly.graph_objects as go
import base64
import os

# Page configuration
st.set_page_config(
    page_title="Data Engineer Portfolio | Your Name",
    page_icon="💻",
    layout="wide",
    initial_sidebar_state="collapsed"
)


# Custom CSS
def local_css():
    st.markdown("""
    <style>
    /* Main container styling */
    .main {
        padding: 2rem;
    }

    /* Gradient text */
    .gradient-text {
        background: linear-gradient(90deg, #0078D4 0%, #5E5CE6 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: 700;
        font-size: 3rem;
        margin-bottom: 1rem;
    }

    /* Project cards */
    .project-card {
        background: linear-gradient(135deg, #0078D4 0%, #5E5CE6 100%);
        padding: 1.5rem;
        border-radius: 10px;
        color: white;
        margin: 1rem 0;
        transition: transform 0.3s ease;
    }

    .project-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 10px 20px rgba(0,0,0,0.2);
    }

    /* Client badges */
    .client-badge {
        background-color: #e6f3ff;
        padding: 0.5rem 1rem;
        border-radius: 20px;
        margin: 0.3rem;
        display: inline-block;
        font-size: 0.9rem;
        border: 1px solid #0078D4;
        font-weight: 500;
    }

    .client-badge:hover {
        background: linear-gradient(135deg, #0078D4 0%, #5E5CE6 100%);
        color: white;
        cursor: pointer;
    }

    /* Skill pills */
    .skill-pill {
        display: inline-block;
        padding: 0.5rem 1rem;
        margin: 0.3rem;
        border-radius: 25px;
        background: linear-gradient(135deg, #0078D4 0%, #5E5CE6 100%);
        color: white;
        font-size: 0.9rem;
        box-shadow: 0 2px 5px rgba(0,0,0,0.1);
    }

    /* Achievement cards */
    .achievement-card {
        background: #f8f9fa;
        padding: 1.5rem;
        border-radius: 10px;
        border-left: 5px solid #0078D4;
        margin: 1rem 0;
    }

    /* Timeline */
    .timeline-item {
        padding: 1.5rem;
        border-left: 3px solid #0078D4;
        margin: 1.5rem 0;
        background-color: #f8f9fa;
        border-radius: 0 10px 10px 0;
        position: relative;
    }

    .timeline-item::before {
        content: "●";
        color: #0078D4;
        font-size: 1.5rem;
        position: absolute;
        left: -0.75rem;
        top: 1rem;
        background: white;
    }

    /* Tech stack icons */
    .tech-icon {
        font-size: 2rem;
        margin: 0.5rem;
        display: inline-block;
    }

    /* Stats */
    .stat-card {
        background: white;
        padding: 1.5rem;
        border-radius: 10px;
        box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        text-align: center;
        margin: 0.5rem;
    }

    .stat-number {
        font-size: 2rem;
        font-weight: bold;
        color: #0078D4;
    }

    /* Footer */
    .footer {
        text-align: center;
        padding: 2rem;
        background: linear-gradient(135deg, #0078D4 0%, #5E5CE6 100%);
        color: white;
        border-radius: 10px;
        margin-top: 3rem;
    }
    </style>
    """, unsafe_allow_html=True)


# Apply custom CSS
local_css()

# Initialize session state
if 'page' not in st.session_state:
    st.session_state.page = "home"


# Navigation
def navigation():
    col1, col2, col3, col4, col5 = st.columns([1, 1, 1, 1, 1])

    with col1:
        if st.button("🏠 Home", width='stretch'):
            st.session_state.page = "home"
    with col2:
        if st.button("👨‍💻 Projects", width='stretch'):
            st.session_state.page = "projects"
    with col3:
        if st.button("📊 Skills", width='stretch'):
            st.session_state.page = "skills"
    with col4:
        if st.button("📜 Certifications", width='stretch'):
            st.session_state.page = "certifications"
    with col5:
        if st.button("📞 Contact", width='stretch'):
            st.session_state.page = "contact"

    st.markdown("---")


# Home Page
def home_page():
    # Hero Section
    col1, col2 = st.columns([2, 1])

    with col1:
        st.markdown('<h1 class="gradient-text">Data Engineer & Python Developer</h1>', unsafe_allow_html=True)
        st.markdown("### HTC Global Services | Chennai, India")
        st.markdown("""
        Results-driven Data Engineer with 4+ years of experience in designing and implementing 
        data solutions across cloud platforms. Specialized in Azure Data Factory, PySpark, and 
        Python automation. Passionate about optimizing data workflows and ensuring data integrity.
        """)

        # Quick contact buttons
        col_a, col_b, col_c = st.columns(3)
        with col_a:
            st.link_button("📧 Email Me", "mailto:shyamvimal98@gmail.com")
        with col_b:
            st.link_button("🔗 LinkedIn", "linkedin.com/in/shyam-kumar-g/")

    with col2:
        # Profile summary card
        st.markdown("""
        <div style="background: linear-gradient(135deg, #0078D4 0%, #5E5CE6 100%); padding: 2rem; border-radius: 10px; color: white;">
            <h3 style="text-align: center;">📍 Based in</h3>
            <p style="text-align: center; font-size: 1.2rem;">Chennai, India</p>
            <h3 style="text-align: center;">⏰ Experience</h3>
            <p style="text-align: center; font-size: 1.2rem;">4+ Years</p>
            <h3 style="text-align: center;">🏢 Current Role</h3>
            <p style="text-align: center; font-size: 1.2rem;">Data Engineer at HTC Global Services</p>
        </div>
        """, unsafe_allow_html=True)

    # Quick Stats
    st.markdown("## 📊 Professional Snapshot")
    col1, col2, col3, col4 = st.columns(4)

    stats = [
        {"number": "4+", "label": "Years Experience"},
        {"number": "15+", "label": "Projects Delivered"},
        {"number": "5+", "label": "Clients Served"},
        {"number": "3", "label": "Cloud Platforms"}
    ]

    for col, stat in zip([col1, col2, col3, col4], stats):
        with col:
            st.markdown(f"""
            <div class="stat-card">
                <div class="stat-number">{stat['number']}</div>
                <div>{stat['label']}</div>
            </div>
            """, unsafe_allow_html=True)

    # Key Clients
    st.markdown("## 🤝 Key Clients")
    clients = ["Silicon Labs", "TVS Motor", "Hyundai", "Internal Projects"]

    cols = st.columns(len(clients))
    for col, client in zip(cols, clients):
        with col:
            st.markdown(f'<div class="client-badge" style="text-align: center;">{client}</div>', unsafe_allow_html=True)

    # Featured Project Highlights
    st.markdown("## 🚀 Recent Highlights")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
        <div class="achievement-card">
            <h4>📊 Cost Optimization Initiative</h4>
            <p>Extracted and analyzed Azure resources across 3 environments using Python, eliminating unused objects and optimizing cloud costs</p>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class="achievement-card">
            <h4>⚡ Automated QAT Process</h4>
            <p>Developed Python script that streamlined Quality Assurance Testing, improving efficiency by 40%</p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="achievement-card">
            <h4>🔄 Data Pipeline Optimization</h4>
            <p>Created custom PySpark wrapper for MySQL, SFTP, and MongoDB connections, optimizing data extraction</p>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class="achievement-card">
            <h4>📈 Real-time Dashboard Solution</h4>
            <p>Built Flask-based API with Plotly visualizations for TVS Motor automotive data processing</p>
        </div>
        """, unsafe_allow_html=True)


# Skills Page
def skills_page():
    st.markdown('<h1 class="gradient-text">Technical Skills</h1>', unsafe_allow_html=True)

    # Programming Languages
    st.markdown("## 💻 Programming Languages")
    languages = ["Python", "PySpark", "Bash Script", "SQL"]
    cols = st.columns(len(languages))
    for col, lang in zip(cols, languages):
        with col:
            st.markdown(f'<div class="skill-pill">{lang}</div>', unsafe_allow_html=True)

    # Databases
    st.markdown("## 🗄️ Databases")
    databases = ["MySQL", "MsSQL Server"]
    cols = st.columns(len(databases))
    for col, db in zip(cols, databases):
        with col:
            st.markdown(f'<div class="skill-pill">{db}</div>', unsafe_allow_html=True)

    # Cloud & Tools
    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### ☁️ Cloud Platforms")
        clouds = ["Amazon Web Services (AWS)", "Microsoft Azure"]
        for cloud in clouds:
            st.markdown(f'<div class="skill-pill">{cloud}</div>', unsafe_allow_html=True)

    with col2:
        st.markdown("### 📊 Reporting & Visualization")
        tools = ["PowerBI", "Plotly"]
        for tool in tools:
            st.markdown(f'<div class="skill-pill">{tool}</div>', unsafe_allow_html=True)

        st.markdown("### 💿 Operating Systems")
        os_list = ["Windows", "Ubuntu", "Linux"]
        for os_name in os_list:
            st.markdown(f'<div class="skill-pill">{os_name}</div>', unsafe_allow_html=True)

    # Skill Proficiency Visualization
    st.markdown("## 📈 Skill Proficiency")

    skill_data = {
        "Python": 95,
        "SQL": 90,
        "PySpark": 80,
        "Azure": 85,
        "AWS": 75,
        "PowerBI": 80
    }

    for skill, level in skill_data.items():
        st.markdown(f"**{skill}**")
        st.progress(level / 100)


# Projects Page
def projects_page():
    st.markdown('<h1 class="gradient-text">Professional Experience</h1>', unsafe_allow_html=True)

    # HTC Global Services Header
    st.markdown("""
    <div style="background: linear-gradient(135deg, #0078D4 0%, #5E5CE6 100%); padding: 1rem; border-radius: 10px; color: white; margin-bottom: 2rem;">
        <h2 style="margin:0;">HTC Global Services, Chennai</h2>
        <p style="margin:0; font-size: 1.2rem;">Data Engineer | July 2021 - Present</p>
    </div>
    """, unsafe_allow_html=True)

    # Client Projects
    clients = [
        {
            "name": "Silicon Labs",
            "icon": "🔬",
            "projects": [
                "Developed and Triggered Stored Procedures in Azure Data Factory (ADF)",
                "Quality Assurance Testing - Validated data against test cases",
                "Production Support - Monitored JAMS jobs with automated Azure DevOps stories",
                "Automated QAT Process using Python script",
                "Cost Optimization - Analyzed Azure resources across environments using Python"
            ]
        },
        {
            "name": "TVS Motor PVT Ltd",
            "icon": "🏍️",
            "projects": [
                "Flask API Development for database requests with calculations",
                "Extracted automotive data using pyodbc library",
                "Data cleaning and preprocessing",
                "Plotly visualizations (line charts in PNG format)",
                "Automated PDF report distribution via API calls"
            ]
        },
        {
            "name": "Hyundai - BlueLink Championship",
            "icon": "🚗",
            "projects": [
                "Data transfer from AWS EC2 to Hive using PySpark API calls",
                "Ensured data accuracy and integrity",
                "Ongoing client support for PySpark and SQL optimization",
                "Cross-functional collaboration for data integration strategies"
            ]
        },
        {
            "name": "Internal Projects",
            "icon": "🏢",
            "projects": [
                "HTC Data Platform: Custom PySpark wrapper for MySQL, SFTP, MongoDB",
                "NiFi scheduling processor using Python",
                "Informatica Transformation Management: Extracted data from XML files",
                "Generated structured CSV files for Informatica transformations"
            ]
        }
    ]

    # Display clients in expandable sections
    for client in clients:
        with st.expander(f"{client['icon']} {client['name']}"):
            for project in client['projects']:
                st.markdown(f"✅ {project}")

            # Add technology tags
            if client['name'] == "Silicon Labs":
                st.markdown("**Technologies:** Azure Data Factory, Python, JAMS, Azure DevOps")
            elif client['name'] == "TVS Motor PVT Ltd":
                st.markdown("**Technologies:** Flask, Python, pyodbc, Plotly, REST APIs")
            elif client['name'] == "Hyundai - BlueLink Championship":
                st.markdown("**Technologies:** AWS EC2, Hive, PySpark, SQL")
            else:
                st.markdown("**Technologies:** PySpark, NiFi, Informatica, Python, XML")


# Certifications Page
def certifications_page():
    st.markdown('<h1 class="gradient-text">Certifications</h1>', unsafe_allow_html=True)

    # Main certification
    col1, col2 = st.columns([1, 3])

    with col1:
        st.markdown("""
        <div style="background: linear-gradient(135deg, #0078D4 0%, #5E5CE6 100%); 
                    padding: 2rem; 
                    border-radius: 10px; 
                    text-align: center;
                    color: white;">
            <h1>🏆</h1>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        ### Databricks Data Engineer Associate
        - **Issued by:** Databricks
        - **Skills validated:** Spark, Data Engineering, ETL, Performance Tuning
        - **Status:** Active
        """)

    # Recommended certifications section
    st.markdown("## 📚 Learning Path")
    st.markdown("""
    Currently preparing for:
    - 🚀 Azure Data Engineer Associate (DP-203)
    - ☁️ AWS Certified Data Analytics
    """)

    # Certification timeline
    st.markdown("## 📅 Career Development")

    timeline_data = [
        {"year": "2023", "cert": "Databricks Data Engineer Associate", "status": "✅ Completed"},
        {"year": "2024", "cert": "Azure Data Engineer Associate", "status": "🔄 In Progress"},
        {"year": "2024", "cert": "AWS Data Analytics Specialty", "status": "📅 Planned"}
    ]

    for item in timeline_data:
        st.markdown(f"""
        <div class="timeline-item">
            <strong>{item['year']}</strong> - {item['cert']} <span style="color: #0078D4;">{item['status']}</span>
        </div>
        """, unsafe_allow_html=True)


# Contact Page
def contact_page():
    st.markdown('<h1 class="gradient-text">Get In Touch</h1>', unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
        ### 📍 Contact Information

        **📍 Location:** Chennai, India  
        **📧 Email:** shyamvimal98@gmail.com  
        **📱 Phone:** +91 8667597068  
        **💼 LinkedIn:** linkedin.com/in/shyam-kumar-g/ 

        ### 🏢 Current Role
        **Data Engineer** at HTC Global Services  
        *July 2021 - Present*
        """)

        # Availability
        st.markdown("### ⏰ Availability")
        st.markdown("✅ Open for opportunities and collaboration")
        st.markdown("🌐 Working hours: IST (9 AM - 6 PM)")

    with col2:
        st.markdown("### 📧 Send a Message")

        with st.form("contact_form"):
            name = st.text_input("Name")
            email = st.text_input("Email")
            company = st.text_input("Company")
            message = st.text_area("Message", height=150)

            submitted = st.form_submit_button("Send Message", width='stretch')

            if submitted:
                if name and email and message:
                    st.success("✅ Message sent successfully! I'll get back to you within 24 hours.")
                    st.balloons()
                else:
                    st.error("❌ Please fill in all required fields (Name, Email, Message)")


# Footer
def footer():
    st.markdown("""
    <div class="footer">
        <p>© 2026 Data Engineer Portfolio | Built with Streamlit</p>
        <p style="font-size: 0.9rem;">📍 Chennai, India | 📧 your.email@example.com</p>
    </div>
    """, unsafe_allow_html=True)


# Main app
def main():
    navigation()

    if st.session_state.page == "home":
        home_page()
    elif st.session_state.page == "projects":
        projects_page()
    elif st.session_state.page == "skills":
        skills_page()
    elif st.session_state.page == "certifications":
        certifications_page()
    elif st.session_state.page == "contact":
        contact_page()

    footer()


if __name__ == "__main__":
    main()