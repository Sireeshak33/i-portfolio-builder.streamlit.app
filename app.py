import streamlit as st
from jinja2 import Template
from engine import generate_tailored_resume
from templates import RESUME_HTML_TEMPLATE

st.set_page_config(page_title="Portfolio Builder", layout="wide")
st.title("💼 AI Portfolio Builder")

col1, col2 = st.columns([1, 1])

with col1:
    raw_profile = st.text_area("Your Raw Details (Education, Skills, Projects):", height=200)
    job_desc = st.text_area("Target Job Description:", height=150)
    generate_btn = st.button("🚀 Optimize Portfolio")

if "resume_data" not in st.session_state:
    st.session_state.resume_data = None

if generate_btn and raw_profile and job_desc:
    with st.spinner("AI is formatting your details..."):
        st.session_state.resume_data = generate_tailored_resume(raw_profile, job_desc)

with col2:
    if st.session_state.resume_data:
        tmpl = Template(RESUME_HTML_TEMPLATE)
        rendered_html = tmpl.render(data=st.session_state.resume_data)
        
        st.components.v1.html(rendered_html, height=600, scrolling=True)
        st.download_button("Download Source Code (.html)", rendered_html, file_name="index.html")
    else:
        st.info("Your customized web portfolio will render here.")
