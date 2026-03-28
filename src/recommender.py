'''
Main Logic:
Input title -> Find Index -> Get Vector -> Call similarity -> Return top results

'''
def find_index(df, title):
    return  df[df["title"] == title].index[0]



def recommend(df,sim_matrix,title):
    idx = find_index(df, title)
    scores = sim_matrix[idx]
    return scores

