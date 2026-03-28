'''
Handle TF-IDF:
- fit()
- Transform()
- return tfidf_matrix + vectorizer

'''

from sklearn.feature_extraction.text import TfidfVectorizer

def vectorize(df):
    text_data = df["combined_text"]
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(text_data)
    return tfidf_matrix, vectorizer

