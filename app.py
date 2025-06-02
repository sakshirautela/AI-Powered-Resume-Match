import streamlit as st
import pdfplumber
import docx2txt  
from src.model.api import extract_skills_with_gemini
from src.model.match_score import calculate_skill_match
from dotenv import load_dotenv
import os

load_dotenv()

st.set_page_config(page_title="AI Resume Screener", layout="centered")
st.title("🤖 AI-Powered Resume Screener")
st.markdown("Upload your resume and the job description below to see how well your skills match!")

def extract_text_from_file(file):
    if file.type == "application/pdf":
        with pdfplumber.open(file) as pdf:
            text = ""
            for page in pdf.pages:
                text += page.extract_text() + "\n"
        return text
    elif file.type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":  # docx mime type
        return docx2txt.process(file)
    elif file.type == "text/plain":
        return file.read().decode("utf-8")
    else:
        return ""

resume_file = st.file_uploader("📄 Upload your Resume", type=["txt","pdf","docx"])
jd_text = st.text_area("📝 Enter Job Description", height=200)

if resume_file and jd_text:
    resume_text = extract_text_from_file(resume_file)

    with st.spinner("🔍 Extracting skills ..."):
        resume_skills = extract_skills_with_gemini(resume_text)
        jd_skills = extract_skills_with_gemini(jd_text)

    score = calculate_skill_match(resume_skills, jd_skills)

    st.success("✅ Resume processed successfully!")

    st.subheader("🎯 Match Score")
    st.progress(score / 100)
    st.metric("Skill Match %", f"{score}%")

    st.subheader("📌 Extracted Skills")
    st.write("**From Resume:**", ', '.join(resume_skills))
    st.write("**From Job Description:**", ', '.join(jd_skills))
