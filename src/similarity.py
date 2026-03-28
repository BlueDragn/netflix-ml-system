'''
Compute cosine similarity
'''

from sklearn.metrics.pairwise import cosine_similarity

def similarity(tfidf_matrix):
    return cosine_similarity(tfidf_matrix, tfidf_matrix)
