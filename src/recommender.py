'''
Main Logic:
Input title -> Find Index -> Get Vector -> Call similarity -> Return top results

'''
import numpy as np
def find_index(df, title):
    result =  df[df["title"].str.contains(title, case=False, na=False)]

    if result.empty:
        return None

    return result.index[0]



def recommend(df, sim_matrix, title, top_n=20):
    idx = find_index(df, title)

    if idx is None:
        return []


    scores = sim_matrix[idx]

    indices = np.argsort(scores)[::-1]
    top_indices = indices[1: top_n + 1]

    input_genres = set(df.iloc[idx]["listed_in"].split(", "))
    filtered_indices = []
    for i in top_indices:
        movie_genres = set(df.iloc[i]["listed_in"].split(", "))
        if len(input_genres.intersection(movie_genres)) > 0:
            filtered_indices.append(i)

    return  filtered_indices[:top_n]



