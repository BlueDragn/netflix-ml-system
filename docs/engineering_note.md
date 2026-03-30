 # 🧠 Engineering Notes — Project 2.5  
## **Project:** Content-Based Recommendation System (TF-IDF)

---

# 1. Problem Framing

The problem is framed as:

```text id="v18l8i"
Given a title → find similar titles
```

This is not a prediction problem.  
It is a **similarity + retrieval problem**.

Key idea:

```text id="sj3qoc"
No labels, no training target → only comparison
```

---

# 2. System Abstraction

At a high level, the system is:

```text id="bw8wzy"
Text → Representation → Similarity → Ranking → Output
```

Breaking it down:

1. Convert raw data into structured format  
2. Transform text into numerical representation  
3. Compute similarity between items  
4. Rank based on similarity  
5. Return top results  

---

# 3. Data as the Central Object

The entire system revolves around a single object:

```text id="ht2mui"
DataFrame (df)
```

Key insight:

```text id="s3xkbr"
df acts as the carrier of all information
```

- Raw data loaded into df  
- Features added to df  
- df passed across modules  

This ensures:
- consistency  
- traceability  
- modular design  

---

# 4. Feature Engineering Layer

## 4.1 Purpose

Convert multiple columns into a **single representation usable by ML**

```text id="xq9563"
title + genre + description → combined_text
```

---

## 4.2 Cleaning

Steps applied:

- Lowercasing → normalize text  
- Strip → remove extra spaces  
- fillna → prevent errors  

---

## 4.3 Feature Weighting

Not all features are equally important.

Manual weighting applied:

```text id="77p49b"
title (high importance)  
genre (medium importance)  
description (context)
```

Implemented by repetition:

```text id="9wbhtm"
(title × n) + (genre × m) + description
```

---

## 4.4 Key Insight

```text id="t1wjme"
Feature engineering defines model behavior
```

The model (TF-IDF) is simple — representation carries most of the power.

---

# 5. Vectorization Layer (TF-IDF)

## 5.1 Purpose

Convert text into numerical vectors:

```text id="xulw7w"
text → vector space
```

---

## 5.2 TF-IDF Mechanics

### TF (Term Frequency)
- Measures importance of a word in a single document  

### IDF (Inverse Document Frequency)
- Measures rarity of a word across all documents  

Combined:

```text id="pkido3"
TF × IDF → final weight
```

---

## 5.3 Vocabulary

- All unique words form the vocabulary  
- Vocabulary size = vector dimensions  

```text id="6sgi0o"
Each word = one axis in space
```

---

## 5.4 Output

```text id="trmb1j"
tfidf_matrix (n_documents × n_words)
```

- Sparse matrix  
- Each row = one title  
- Each column = one word  

---

## 5.5 Fit vs Transform

- `fit()` → learn vocabulary + IDF  
- `transform()` → apply to text  
- `fit_transform()` → combined  

Important rule:

```text id="b1xcgj"
Fit once on dataset → reuse for all inputs
```

---

# 6. Similarity Layer

## 6.1 Purpose

Measure how close two items are in vector space

---

## 6.2 Cosine Similarity

Formula concept:

```text id="ggbn82"
Similarity = cos(angle between vectors)
```

Key properties:

- Range: 0 → 1  
- 1 = identical  
- 0 = unrelated  

---

## 6.3 Matrix Computation

```text id="bfc00c"
cosine_similarity(X, X)
```

Produces:

```text id="z4lqxy"
similarity_matrix (n × n)
```

Meaning:

```text id="qw0xn2"
sim[i][j] = similarity between item i and j
```

---

## 6.4 Key Insight

```text id="6cp9qe"
Same matrix → internal comparison  
Different matrices → cross comparison
```

---

# 7. Recommendation Layer

## 7.1 Steps

1. Find index of input title  
2. Extract similarity scores  
3. Sort scores  
4. Remove self-match  
5. Select top-N  

---

## 7.2 Sorting Mechanism

Used:

```text id="4rnbxt"
np.argsort(scores)
```

Important:

```text id="7i8zy1"
Sort indices, not values
```

---

## 7.3 Output

Returns:

```text id="kbesdu"
Top-N similar titles
```

---

## 7.4 Nature of System

```text id="4ji44q"
No learning → pure retrieval + ranking
```

---

# 8. System Design Principles Applied

## 8.1 Modularity

Each module has a single responsibility:

- data_loader → load  
- feature_builder → transform  
- vectorizer → convert  
- similarity → compare  
- recommender → rank  

---

## 8.2 Data Flow

```text id="xswmdw"
df → df → matrix → similarity → results
```

Clear transformation at each step.

---

## 8.3 Function Contracts

Each function follows:

```text id="nzqy1s"
Input → Process → Output
```

---

# 9. Debugging Insights

Common errors encountered:

- Type mismatch (DataFrame vs Series vs int)  
- Wrong function arguments  
- File path issues  

---

## Debugging Framework

```text id="sbubmp"
1. Read traceback  
2. Locate error line  
3. Check variable type  
4. Print values  
5. Compare expected vs actual  
```

---

# 10. Limitations of Current System

## 10.1 Lexical Nature

TF-IDF only matches words:

```text id="xk0j05"
No semantic understanding
```

---

## 10.2 Feature Imbalance

- Description dominates due to length  
- Genre not structured properly  

---

## 10.3 No Evaluation

- No accuracy metric  
- No validation  

---

# 11. Improvement Directions

## 11.1 Representation

- Better text cleaning  
- Stronger feature weighting  
- Structured genre handling  

---

## 11.2 Vectorization

- Use n-grams  
- Remove stopwords  
- Limit vocabulary  

---

## 11.3 Model Upgrade

Future:

```text id="w5elmh"
TF-IDF → Embeddings (semantic understanding)
```

---

# 12. Engineering Learnings

## 12.1 System Thinking

- Break problem into layers  
- Define flow clearly  

---

## 12.2 Data-Centric Approach

```text id="64am0x"
Better data → better output
```

---

## 12.3 Iterative Development

```text id="tg4x27"
Build → Test → Debug → Improve
```

---

## 12.4 Execution Gap Realization

Understanding ≠ Implementation

---

# 13. Transferable Skills

These apply beyond this project:

---

## 13.1 Pipeline Design
Designing step-by-step systems

---

## 13.2 Data Handling
Working with structured data (DataFrame)

---

## 13.3 Debugging
Systematic error resolution

---

## 13.4 Library Usage
- pandas  
- numpy  
- sklearn  

---

## 13.5 Feature Engineering
Improving input instead of changing model

---

## 13.6 Modular Coding
Writing reusable components

---

## 13.7 ML System Thinking
Understanding full pipeline, not just models

---

# 📌 Final Insight

```text id="yevvw2"
ML systems are not about complex models.

They are about:
- data representation
- clean pipeline
- correct transformations
```

---



## March 30, 2026