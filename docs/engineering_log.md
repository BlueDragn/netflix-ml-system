# 🧾 Engineering Log — Project 2.5  
**Project:** Content-Based Recommendation System (TF-IDF)  
**Period Covered:** March 23 to 29 2026  

---

## 📅 Phase 1: Project Initialization

### Objective
- Build a content-based recommendation system  
- Input: title, genre, description  
- Output: top-N similar titles  

### Decisions
- TF-IDF for vectorization  
- Cosine similarity for comparison  
- Modular architecture  

---

## 📅 Phase 2: System Architecture

### Pipeline
```
Data → Feature Engineering → Vectorization → Similarity → Recommendation
```

### Modules
```
data_loader
feature_builder
vectorizer
similarity
recommender
```

### Issue
- Data flow confusion  

### Fix
```
Input → Transform → Output
```

---

## 📅 Phase 3: Feature Engineering

### Work
- Created combined_text column  
- Combined:
  - title
  - genre
  - description  

### Cleaning
```python
str.lower()
str.strip()
fillna("")
```

### Weighting
```
title → high
genre → medium
description → base
```

### Issues
- Missing spaces
- NaN errors

---

## 📅 Phase 4: Vectorization

### Implementation
```python
text_data = df["combined_text"]
vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(text_data)
```

### Learnings
- Vocabulary = dimensions  
- TF = per row  
- IDF = across dataset  

### Issues
- Passed DataFrame instead of column  
- Confused fit vs transform  

---

## 📅 Phase 5: Similarity

### Implementation
```python
from sklearn.metrics.pairwise import cosine_similarity

sim_matrix = cosine_similarity(tfidf_matrix, tfidf_matrix)
```

### Output
```
n × n similarity matrix
```

### Issue
- Tried using vectorizer in similarity  

---

## 📅 Phase 6: Recommendation Logic

### Implementation
```python
idx = df[df["title"] == title].index[0]
scores = sim_matrix[idx]

import numpy as np
top_indices = np.argsort(scores)[::-1][1:11]

df.iloc[top_indices]["title"]
```

### Fixes
- Removed self match  
- Handled missing title  

### Issues
- .empty used on int  
- sorting confusion  

---

## 📅 Phase 7: Integration

### main.py Flow
```python
df = data_loader()
df = build_features(df)
tfidf_matrix, vectorizer = vectorize(df)
sim_matrix = similarity(tfidf_matrix)
recommend(df, sim_matrix, title)
```

### Issues
- Wrong imports  
- Wrong arguments  

---

## 📅 Phase 8: Debugging

### Fixed
- File path issues  
- Type errors  
- Function mismatch  

### Rule learned
```
check type → check value → fix
```

---

## 📅 Phase 9: Output Evaluation

### Result
- Working system  
- Poor recommendation quality  

### Reason
- TF-IDF is lexical  
- Description dominates  
- Genre weak  

---

## 📅 Phase 10: Documentation

### Completed
- README  
- Engineering log  
- Engineering notes  

### Decision
```
Freeze v1 baseline
```

---

# 📊 Current Status

```
✔ Pipeline complete  
✔ System working  
⚠ Output weak  
```

---

# 🧠 Key Outcomes

- Built full ML pipeline  
- Understood TF-IDF + similarity  
- Learned modular system design  
- Practiced debugging  

---

# ⚠️ Gaps

- Python fluency  
- pandas / numpy usage  
- debugging independence  
- feature engineering  

---

# 🚀 Next Phase

- Improve features  
- Tune TF-IDF  
- improve ranking  
- strengthen debugging  

---

## 📌 Conclusion

Working baseline complete.  
Next phase: improve system quality.

-------
-------




# Experiments/ Tests
## March 30, 2026

---

## 🎯 Task  
Test impact of using **title-only feature** on recommendation quality

---

## ⚙️ Change Made  
- Modified `combined_text` to include only `title`  
- Removed `genre` and `description` from feature set  

---

## 🧪 Experiment 1  
**Input:** "Inception"  

### Result  
- All similarity scores = 0.0  
- Output recommendations appear random  

### Observation  
- No overlap between "Inception" and other titles  

### Insight  
- Unique titles produce zero similarity  
- Title alone does not provide shared features  

---

## 🧪 Experiment 2  
**Input:** "Love"  

### Result  
- Multiple titles contain "love"  
- Still similarity scores ≈ 0.0  

### Observation  
- Word overlap exists but has negligible effect  

### Insight  
- TF-IDF downweights common words  
- Common words do not contribute meaningfully  

---

## 🧪 Experiment 3  
**Input:** "The Dark Knight"  

### Result  
- Movie not found in dataset  

### Observation  
- Input not present in dataset  

### Insight  
- System depends entirely on dataset  
- No handling for external/unavailable input  

---

## ⚠️ Issues Noted  

- Title feature too weak for similarity  
- Common words ineffective due to TF-IDF  
- System fails when input not in dataset  
- Output becomes random when scores are equal  

---

## 🧠 Key Learnings  

- Feature quality directly impacts similarity  
- TF-IDF relies on distinctive words  
- Title-only representation is insufficient  
- Input validation and matching are critical  

---

## ✅ Decision  

- [x] Do not use title-only as final feature  
- [x] Move to testing description-only  
- [x] Later combine features with weighting  

---

## 🔁 Next Step  

Test `description` as primary feature and compare results

---

## 🎯 Task  
Evaluate effectiveness of **genre-only feature** for content-based recommendation

---

## ⚙️ Change Made  
- Modified `combined_text` to include only `listed_in` (genre)  
- Removed `title` and `description` from feature set  
- Cleaned and lowercased genre text  

---

## 🧪 Experiment  
**Input:** "Bird Box"  

---

## 📊 Result  
- All similarity scores = 0.0  
- Recommendations appear unrelated (anime, kids TV, comedy, etc.)

---

## 🔍 Observation  
- Input genres: `dramas, sci-fi & fantasy, thrillers`  
- Output genres do not overlap with input genres  
- No shared tokens between input and recommended items  

---

## 🧠 Analysis  

### 1. Sparse Vocabulary Overlap  
- Genre categories differ across items  
- Example:  
  - Input → "thrillers"  
  - Other items → "horror movies"  
- No exact token match → similarity = 0  

---

### 2. Inconsistent Genre Representation  
- Same concept represented differently:  
  - "dramas" vs "drama"  
  - "thrillers" vs "thriller"  
- No normalization applied → treated as different tokens  

---

### 3. Lack of Semantic Understanding  
- TF-IDF relies on exact word matching  
- Cannot capture relationships like:  
  - thriller ≈ horror  
  - sci-fi ≈ fantasy  

---

### 4. Limited Feature Depth  
- Genre provides only high-level categorization  
- Lacks detailed descriptive information  

---

## ⚠️ Issues Identified  

- Zero similarity due to lack of token overlap  
- Genre labels are inconsistent across dataset  
- No preprocessing for normalization (stemming/standardization)  
- Weak similarity signal despite structured feature  

---

## 🧠 Key Learnings  

- Structured features alone are not sufficient without normalization  
- TF-IDF fails when vocabulary is inconsistent  
- Exact matching is a major limitation in category-based features  
- Feature representation quality directly impacts similarity  

---

## ✅ Decision  

- [x] Genre-only feature is insufficient for reliable recommendations  
- [x] Do not use genre as standalone feature  
- [x] Use genre as **supporting feature in combination**  

---

## 🔁 Next Step  

- Test **description-only feature**  
- Later combine: `description + genre + title (weighted)`

----
----

## 🎯 Task  
Evaluate effectiveness of **description-only feature** for content-based recommendation

---

## ⚙️ Change Made  
- Modified `combined_text` to include only `description`  
- Removed `title` and `genre` from feature set  
- Applied text cleaning and normalization  

---

## 🧪 Experiment  
**Input:** "Bird Box"  

---

## 📊 Result  

- Non-zero similarity scores observed  
- Top scores range: ~0.12 – 0.18  
- Recommendations ranked meaningfully  

---

## 🔍 Sample Output  

Top recommendations include:

- Prey  
- The Rain  
- Hell or High Water  
- The 12th Man  
- Midnight Mass  

---

## 🔍 Observation  

- Recommended items share thematic similarity:
  - survival  
  - danger  
  - crisis situations  
  - human struggle  

- Descriptions show overlapping vocabulary:
  - "survival", "escape", "threat", "danger"  

---

## 🧠 Analysis  

### 1. Rich Vocabulary → Better Overlap  
- Descriptions contain detailed narrative context  
- Higher probability of shared tokens across items  
- Leads to meaningful cosine similarity  

---

### 2. TF-IDF Effectiveness  
- Important terms (e.g., "survival", "threat") get higher weights  
- Common words are downweighted appropriately  
- Improves relevance of similarity computation  

---

### 3. Emergent Semantic Behavior  
- Even without deep learning, system captures:
  - thematic similarity  
  - contextual relationships  

---

### 4. Stable Ranking  
- Non-zero similarity enables proper ranking  
- Higher scores correspond to more relevant items  

---

## ⚠️ Limitations Identified  

- No true semantic understanding (word-level only)  
- Synonyms not captured (e.g., "alien" vs "extraterrestrial")  
- No personalization  
- Dependent on text quality in dataset  

---

## 🧠 Key Learnings  

- Feature richness significantly improves recommendation quality  
- Description is the most informative feature among tested options  
- TF-IDF performs well when vocabulary overlap exists  
- Proper feature engineering is more impactful than algorithm change  

---

## ✅ Decision  

- [x] Use description as primary feature  
- [x] Combine with genre and title for improved system  
- [x] Move toward weighted feature combination  

---

## 🔁 Next Step  

- Build **combined feature system**:
  - description (high weight)  
  - genre (medium weight)  
  - title (low weight)  

---

## ⚡ Final Insight  

> Meaningful similarity emerges when feature representation captures sufficient context and vocabulary overlap.




