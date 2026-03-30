'''
Main Logic:
Input title -> Find Index -> Get Vector -> Call similarity -> Return top results

'''
import numpy as np
def find_index(df, title):
    result =  df[df["title"].str.contains(title, case=False, na=False)]

    if result.empty:
        print("No match found for title:", title)
        print(df[df["title"].str.contains(title, case=False, na=False)][["title"]].head(20))
        return None

    if len(result) > 1:
        print("Multiple matches found for title:", title)
        print(result[["title"]].head(20))

    return result.index[0]



def recommend(df, sim_matrix, title):
    idx = find_index(df, title)

    if idx is None:
        return ["Movie not found in dataset"]

    #INPUT DEBUG
    print("\n=== INPUT ===")
    print("Title:", df.iloc[idx]["title"])
    print("Genre:", df.iloc[idx]["listed_in"])
    print("Description:", df.iloc[idx]["description"])
    print("=== END INPUT ===\n")



    scores = sim_matrix[idx]
    indices = np.argsort(scores)
    top_indices = indices[::1][1:11]

    results = []

    print("\n=== RECOMMENDATIONS DEBUG ===")

    for i in top_indices:
        results.append({
            "title": df.iloc[i]["title"],
            "genre": df.iloc[i]["listed_in"],
            "description": df.iloc[i]["description"],
            "score": scores[i],

        })

    return results

