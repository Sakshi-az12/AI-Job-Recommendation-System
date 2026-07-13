# 💼 AI Job Recommendation System using NLP

## 📌 Project Overview

The **AI Job Recommendation System** is a Natural Language Processing (NLP) based application that recommends suitable jobs by comparing a user's resume with job descriptions.

The system preprocesses resume text, converts text into TF-IDF vectors, calculates cosine similarity, and recommends the top matching jobs.

---

## 🎯 Objectives

* Extract text from a resume (PDF)
* Clean and preprocess text using NLP
* Compare resume with job descriptions
* Recommend the Top 5 matching jobs
* Display similarity score

---

## 🛠 Technologies Used

* Python
* Streamlit
* Pandas
* NumPy
* spaCy
* Scikit-learn
* PDFPlumber

---

## 📚 NLP Techniques

* Tokenization
* Lemmatization
* Stopword Removal
* TF-IDF Vectorization
* Cosine Similarity

---

## 📂 Project Structure

```text
AI-Job-Recommendation-System/
│
├── app.py
├── preprocess.py
├── recommendation.py
├── pdf_reader.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── dataset/
│   ├── UpdatedResumeDataSet.csv
│   └── job_df.csv
```

---

## 🚀 Installation

### Clone Repository

```bash
git clone https://github.com/your-username/AI-Job-Recommendation-System.git
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Download spaCy Model

```bash
python -m spacy download en_core_web_sm
```

### Run the Application

```bash
streamlit run app.py
```

---

## ✨ Features

* Upload Resume (PDF)
* Resume Text Extraction
* NLP Preprocessing
* TF-IDF Vectorization
* Cosine Similarity Matching
* Top 5 Job Recommendations

---

## 📊 Dataset

* UpdatedResumeDataSet.csv
* job_df.csv

---

## 📷 Screenshots

Add screenshots of:

* Home Page
* Resume Upload
* Recommendation Results

---

## 👩‍💻 Author

**Sakshi Waghmare**

Diploma in Information Technology

---

## 📄 License

This project is created for educational and learning purposes.
