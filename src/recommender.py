'''
Main Logic:
Input title -> Find Index -> Get Vector -> Call similarity -> Return top results

'''
import numpy as np
def find_index(df, title):
    result =  df[df["title"] == title].index[0]

    if result.empty:
        raise ValueError(f"Title '{title}' not found in the DataFrame.")
    return result.index[0]



def recommend(df, sim_matrix, title):
    idx = find_index(df, title)
    scores = sim_matrix[idx]

    indices = np.argsort(scores)
    top_indices = indices[::1][1:11]

    return df.iloc[top_indices]["title"].tolist()

