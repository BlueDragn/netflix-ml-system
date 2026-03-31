'''
Entry point:
- call all components
- run recommend("title")
'''


from src.data_loader import load_data
from src.feature_builder import build_features
from src.vectorizer import apply_weights, vectorize
from src.similarity import compute_similarity
from src.recommender import recommend

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
    title = "Bird Box"
    recommendations = recommend(df, sim_matrix, title)


    #6. Output results
    print(f"Recommendations for '{title}':")
    print("\nTop Recommendations:\n")

    for i, movie in enumerate(recommendations, start=1):
        print(f"{i}. {movie}")

if __name__ == "__main__":
    main()