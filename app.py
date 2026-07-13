import streamlit as st

from pdf_reader import extract_text
from recommendation import recommend_jobs

# -----------------------------
# Page Configuration
# -----------------------------

st.set_page_config(
    page_title="AI Job Recommendation System",
    page_icon="💼",
    layout="wide"
)

st.title("💼 AI Job Recommendation System")
st.write("Upload your Resume (PDF) and get the Top 5 Recommended Jobs.")

uploaded_file = st.file_uploader(
    "Upload Resume",
    type=["pdf"]
)

if uploaded_file is not None:

    with open(uploaded_file.name, "wb") as f:
        f.write(uploaded_file.getbuffer())

    resume_text = extract_text(uploaded_file.name)

    st.success("Resume Uploaded Successfully!")

    if st.button("Recommend Jobs"):

        jobs = recommend_jobs(resume_text)

        st.subheader("Top Recommended Jobs")

        for i, job in enumerate(jobs, start=1):

            st.markdown(f"## {i}. {job['Job Title']}")

            st.write(f"**Similarity Score:** {job['Similarity']} %")

            with st.expander("Job Description"):

                st.write(job["Job Description"])

            st.divider()