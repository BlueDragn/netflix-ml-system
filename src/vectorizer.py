'''
Handle TF-IDF:
- fit()
- Transform()
- return tfidf_matrix + vectorizer

'''

from sklearn.feature_extraction.text import TfidfVectorizer
from scipy.sparse import hstack

def vectorize(df):
    title_vectorizer = TfidfVectorizer(stop_words='english', max_features=5000)
    genres_vectorizer = TfidfVectorizer(stop_words='english', max_features=5000)
    desc_vectorizer = TfidfVectorizer(stop_words='english', max_features=5000)

    title_vec = title_vectorizer.fit_transform(df["title"])
    genres_vec = genres_vectorizer.fit_transform(df["listed_in"])
    desc_vec = desc_vectorizer.fit_transform(df["description"])

    return title_vec, genres_vec, desc_vec

def apply_weights(title_vec, genres_vec, desc_vec, w_title=1, w_genres=3, w_desc=1):


    final_matrix = hstack([
        (w_title * title_vec),
        (w_genres * genres_vec),
        (w_desc * desc_vec)
    ])

    return final_matrix
