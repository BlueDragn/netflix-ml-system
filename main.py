'''
Entry point:
- call all components
- run recommend("title")
'''


from src.data_loader import load_data
from src.feature_builder import build_features
from src.vectorizer import apply_weights, vectorize
from src.similarity import compute_similarity
from src.recommender import recommend, find_index


def main():
    #1. Load data
    df = load_data()

    #2. Build features
    df = build_features(df)


    #3. Vectorize
    title_vec, genres_vec, desc_vec = vectorize(df)


    #4. Compute similarity
    final_matrix = apply_weights(title_vec, genres_vec, desc_vec)
    sim_matrix = compute_similarity(final_matrix)


    #5. Recommend
    title = "Inception"
    idx= find_index(df, title)
    top_indices = recommend(df, sim_matrix, title)


    #6. Output results
    print("\nINPUT:\n")
    print(
        df.iloc[idx]["title"],
        "|",
        df.iloc[idx]["listed_in"],
        "|",
        df.iloc[idx]["description"][:100]
    )
    print("\nTop Recommendations:\n")

    for i in top_indices:
        print(
            df.iloc[i]["title"],
            "|",
            df.iloc[i]["listed_in"],
            "|",
            df.iloc[i]["description"][:100] + "..."
            )

if __name__ == "__main__":
    main()