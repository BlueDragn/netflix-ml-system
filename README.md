# 🎬 Netflix Content-Based Recommendation System

A modular machine learning system that recommends similar movies and shows using **TF-IDF vectorization** and **cosine similarity** on textual features.

---

## 🚀 Overview

This project implements a **content-based filtering** recommendation system that suggests titles similar to a given input, based on:

- **Title** — highest weight
- **Genre** — medium weight
- **Description** — base weight

Text features are combined, vectorized with TF-IDF, and compared using cosine similarity to rank and return the top-N most similar titles.

---

## 🧠 How It Works

```
Raw Data → Feature Engineering → TF-IDF Vectorization → Cosine Similarity → Top-N Recommendations
```

| Step | Description |
|------|-------------|
| 1. Load Data | Reads `cleaned_data.csv` into a pandas DataFrame |
| 2. Feature Engineering | Combines title, genre, and description into a single weighted `combined_text` field |
| 3. TF-IDF Vectorization | Converts text to numerical vectors; builds vocabulary and computes IDF scores |
| 4. Cosine Similarity | Computes pairwise similarity scores across all titles |
| 5. Recommendation | Finds input title, ranks similar items, returns top-N results |

---

## 📂 Project Structure

```
netflix-ml-system/
├── data/
│   └── cleaned_data.csv         # Preprocessed Netflix dataset
├── src/
│   ├── data_loader.py           # Loads and validates the dataset
│   ├── feature_builder.py       # Combines and weights text features
│   ├── vectorizer.py            # TF-IDF vectorization logic
│   ├── similarity.py            # Cosine similarity computation
│   └── recommender.py           # Recommendation interface
├── main.py                      # Entry point
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

**Requirements:** Python 3.8+

```bash
git clone <your-repo-url>
cd netflix-ml-system

python3 -m venv venv
source venv/bin/activate        # On Windows: venv\Scripts\activate

pip install -r requirements.txt
```

**Dependencies:**

```
pandas
numpy
scikit-learn
```

---

## 📦 Dataset

This project uses the **Netflix Movies and TV Shows** dataset, available on [Kaggle](https://www.kaggle.com/datasets/shivamb/netflix-shows).

Download `netflix_titles.csv`, run your cleaning script, and save the output as `data/cleaned_data.csv`.

The cleaned dataset should contain at minimum these columns:

| Column | Description |
|--------|-------------|
| `title` | Movie or show name |
| `listed_in` | Genre(s) |
| `description` | Short synopsis |

---

## ▶️ Usage

```bash
python main.py
```

**Example output:**

```
Input: "Inception"

Top 5 Recommendations:
1. Interstellar        — Similarity: 0.87
2. The Dark Knight     — Similarity: 0.81
3. Tenet               — Similarity: 0.79
4. Shutter Island      — Similarity: 0.74
5. Memento             — Similarity: 0.71
```

---

## 🧪 Technologies Used

| Library | Purpose |
|---------|---------|
| `pandas` | Data loading and manipulation |
| `numpy` | Numerical operations |
| `scikit-learn` | TF-IDF vectorization and cosine similarity |

---

## ⚠️ Limitations

- Uses **lexical** (word-matching) similarity, not semantic understanding — "action" and "thriller" are treated as unrelated terms
- Feature weighting is manually tuned (heuristic), not learned from data
- No evaluation metrics (e.g., precision@k, recall) are implemented
- Cold-start problem: cannot recommend for titles not in the dataset

---

## 🔧 Future Improvements

- **Semantic embeddings** — replace TF-IDF with BERT or Sentence Transformers for contextual understanding
- **TF-IDF tuning** — experiment with n-grams, stopword removal, and min/max document frequency
- **Evaluation pipeline** — add offline metrics to measure recommendation quality
- **Collaborative filtering** — combine with user interaction data for hybrid recommendations
- **API or web interface** — expose recommendations via a REST API or simple UI

---

## 📌 Project Status

| Milestone | Status |
|-----------|--------|
| Data loading and cleaning | ✅ Complete |
| Feature engineering | ✅ Complete |
| TF-IDF vectorization | ✅ Complete |
| Cosine similarity computation | ✅ Complete |
| Recommendation pipeline | ✅ Complete |
| Evaluation metrics | 🔲 Planned |
| Web interface | 🔲 Planned |

---

## 🧠 Learning Outcomes

- Built an end-to-end ML pipeline from scratch with a modular architecture
- Applied TF-IDF vectorization and cosine similarity in a real-world context
- Practiced feature engineering with weighted text fields
