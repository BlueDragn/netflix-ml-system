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



def recommend(df, sim_matrix, title, top_n=10):
    idx = find_index(df, title)

    if idx is None:
        return []


    scores = sim_matrix[idx]

    indices = np.argsort(scores)[::-1]
    top_indices = indices[1:1 + top_n]



    return df.iloc[top_indices]["title"].tolist()

