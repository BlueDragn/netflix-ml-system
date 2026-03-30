'''
Entry point:
- call all components
- run recommend("title")
'''


from src.data_loader import load_data
from src.feature_builder import build_features
from src.vectorizer import vectorize
from src.similarity import compute_similarity
from src.recommender import recommend

def main():
    #1. Load data
    df = load_data()





    #2. Build features
    df = build_features(df)
    print(df[["title", "listed_in", "description", "combined_text"]].head(10))

    #3. Vectorize
    tfidf_matrix, vectorizer = vectorize(df)

    print("TF-IDF Matrix shape:", tfidf_matrix.shape)
    print(vectorizer.get_feature_names_out()[:20])


    #4. Compute similarity
    sim_matrix = compute_similarity(tfidf_matrix)

    #Debug

    print(sim_matrix[0][1])
    print(sim_matrix[0][2])
    print(sim_matrix[10][20])
    print(sim_matrix[0][0])
    print(sim_matrix.max())

    #5. Recommend
    title = "Inception"
    recommendations = recommend(df, sim_matrix, title)


    #6. Output results
    print("Your input movie:", title)
    print("Top Recommendations:")

    for i, movie in enumerate(recommendations, start=1):
        print(f"{i}. {movie}")

if __name__ == "__main__":
    main()