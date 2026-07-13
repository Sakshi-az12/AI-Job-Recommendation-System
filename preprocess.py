import spacy
# Load spaCy English model
nlp = spacy.load("en_core_web_sm")
def nlp_pipeline(text):
    """
    Perform NLP preprocessing:
    - Lowercase
    - Lemmatization
    - Remove stopwords
    - Remove punctuation
    """
    doc = nlp(str(text))
    cleaned_words = []
    for token in doc:
        if (
            not token.is_stop
            and not token.is_punct
            and not token.is_space
        ):
            cleaned_words.append(token.lemma_.lower())
    return " ".join(cleaned_words)