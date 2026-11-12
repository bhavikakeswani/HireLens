import streamlit as st
from app import analyze_resume_job

st.set_page_config(
    page_title="HireLens",
    page_icon="🎯",
    layout="wide"
)

st.title("HireLens 🎯")
st.subheader("AI-Powered Job Hunting Assistant")

st.write(
    "Analyze your resume against a job description, "
    "identify skill gaps, and prepare for interviews."
)

st.divider()

st.header("Resume and Job Description")

resume_text = st.text_area(
    "Paste your Resume",
    placeholder="Paste your resume text here...",
    height=250
)

job_description = st.text_area(
    "Paste Job Description",
    placeholder="Paste the job description here...",
    height=250
)

if st.button("Analyze Resume", type="primary"):

    if not resume_text.strip() or not job_description.strip():
        st.warning("Please enter both your resume and job description.")

    else:
        try:
            with st.spinner("Analyzing your resume... Please wait."):

                result = analyze_resume_job(
                    resume_text,
                    job_description
                )

            st.success("Resume analysis completed!")

            st.header("Resume Analysis")

            st.subheader("Match Summary")
            st.write(result["match_summary"])

            col1, col2 = st.columns(2)

            with col1:
                st.subheader("Matching Skills")

                for skill in result["matching_skills"]:
                    st.write(f"• {skill}")

            with col2:
                st.subheader("Missing Skills")

                for skill in result["missing_skills"]:
                    st.write(f"• {skill}")

            st.subheader("Resume Improvement Suggestions")

            for suggestion in result["resume_improvements"]:
                st.write(f"• {suggestion}")

            st.subheader("Interview Preparation Topics")

            for topic in result["interview_topics"]:
                st.write(f"• {topic}")

        except Exception as e:
            st.error(f"Career analysis failed: {e}")