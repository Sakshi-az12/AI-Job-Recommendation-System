import pandas as pd
import numpy as np

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from preprocess import nlp_pipeline

# ----------------------------
# Load Datasets
# ----------------------------

resume_df = pd.read_csv("UpdatedResumeDataSet.csv")
job_df = pd.read_csv("job_df.csv")

# ----------------------------
# Clean Resume
# ----------------------------

resume_df["clean_resume"] = resume_df["Resume"].apply(nlp_pipeline)

# ----------------------------
# Clean Job Description
# ----------------------------

job_df["clean_job"] = job_df["Job Description"].apply(nlp_pipeline)

# ----------------------------
# TF-IDF Vectorizer
# ----------------------------

tfidf = TfidfVectorizer()

job_vectors = tfidf.fit_transform(job_df["clean_job"])

# ----------------------------
# Recommendation Function
# ----------------------------

def recommend_jobs(resume_text):

    clean_resume = nlp_pipeline(resume_text)

    resume_vector = tfidf.transform([clean_resume])

    similarity = cosine_similarity(resume_vector, job_vectors)

    top5 = np.argsort(similarity[0])[::-1][:5]

    jobs = []

    for index in top5:

        jobs.append(
            {
                "Job Title": job_df.iloc[index]["Job Title"],
                "Job Description": job_df.iloc[index]["Job Description"],
                "Similarity": round(similarity[0][index] * 100, 2),
            }
        )

    return jobs