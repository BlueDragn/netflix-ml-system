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
