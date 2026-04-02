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


---
## Experiment - Title feature Re-check (After Fix)

### Changes
- Fixed Score computation issue

### Input
- "Bird Box"
- "Love"
- "Inception"

### Observation
- Both "Bird Box" and "Love" -> multiple matches with non- zero score
- "Inception" -> no matches, score almost zero

### Conclusion
- Title similarity depends on token overlap
- Works for common words, fails for unique titles

---

## 🧪 Experiment — Genre Feature Recheck (After Fix)

### Change
- Modified combined_text to include only genre (`listed_in`)

### Input
- "Inception"

### Observation
- High similarity scores (~0.92)
- Recommendations mostly belong to:
  - Action & Adventure
  - Sci-Fi & Fantasy

### Analysis
- Genre labels are repeated across multiple items
- TF-IDF captures strong overlap due to identical tokens
- Results show clustering based on category similarity

### Conclusion
- Genre feature provides strong but coarse similarity
- Effective for grouping items by category
- Lacks fine-grained contextual understanding


### Final Feature Hierarchy

Feature       | Behavior                  | Quality
-------------|---------------------------|---------
Title        | keyword overlap           | Weak
Genre        | category matching         | Medium
Description  | contextual similarity     | Strong


---

## 🧪 Experiment — Combined Feature System

### Change
- Combined title, genre, and description into single feature

### Input
- "Inception"

### Observation
- Non-zero similarity scores (~0.13–0.15)
- Recommendations include sci-fi, thriller, and concept-based films
- Results more relevant compared to individual features

### Analysis
- Description drives semantic similarity
- Genre ensures category alignment
- Title provides minor keyword support

### Conclusion
- Combined features produce more balanced and meaningful recommendations
- Reduces weaknesses of individual features
- Improves overall system stability

### Feature Contribution

Feature       | Role
-------------|-------------------------
Title        | weak signal booster
Genre        | category anchor
Description  | main semantic driver

**Better features > better models**
----
---



## Date: 31 March 2026

-----

## Objective

Implement feature weighting in a TF-IDF based recommendation system.

-----

## Work Done

### Pipeline Refactoring

Refactored pipeline into modular components:

- `data_loader`
- `feature_builder`
- `vectorizer`
- `similarity`
- `recommender`

### Vector Architecture

Transitioned from a single `combined_text` vector to separate vectors:

- `title`
- `genre`
- `description`

### Feature Weighting Implementation

```python
final_matrix = hstack([
    w_title * title_vec,
    w_genre * genre_vec,
    w_desc  * desc_vec
])
```

-----

## Issues & Fixes

### 1. Inconsistent Shapes Error

- **Cause:** Tried adding vectors from different vocabularies
- **Fix:** Used `hstack` for concatenation instead of addition

### 2. Index Handling Bug

- **Error:** `'int' object has no attribute 'empty'`
- **Fix:** Corrected `find_index()` logic

### 3. File Path Issue

- **Fix:** Corrected dataset loading path

-----

## Key Learnings

- Separate vectorization creates independent feature spaces
- Feature weighting must be applied via concatenation, not addition
- Sparse matrix operations require shape alignment
- Debugging requires checking types and data flow at each stage

-----

## System Status

|Component              |Status              |
|-----------------------|--------------------|
|Feature-weighted system|Implemented         |
|System runtime         |Passing             |
|Output quality         |Noisy — needs tuning|

-----

## Next Steps

Run controlled experiments on feature weight configurations:

```
(w_title, w_genre, w_desc)

(1, 1, 1)
(2, 2, 1)
(3, 1, 1)
(1, 3, 1)
```

-----

## Summary

Shifted from a single TF-IDF representation to a weighted multi-feature vector system. Resolved dimensional mismatches and index handling bugs along the way. Next focus is weight tuning via controlled experiments.


## Date: 1 April 2026

---

## 🎯 Objective
Evaluate impact of feature weighting on recommendation quality.

---

## 🧪 Experiments Conducted

Test Titles:
- Inception
- Bird Box

Weight Configurations:
- A → (1,1,1)
- B → (2,2,1)
- C → (3,1,1)
- D → (1,3,1)

---

## 📊 Results

### 🎬 Bird Box

| Weights | Observation |
|--------|------------|
| (1,1,1) | Mixed results, moderate noise |
| (2,2,1) | Slight improvement, still noisy |
| (3,1,1) | Poor — title keyword “bird” dominates |
| (1,3,1) | Strong genre clustering, more relevant |

---

### 🎬 Inception

| Weights | Observation |
|--------|------------|
| (1,1,1) | Noisy results (“next”, “9”) |
| (2,2,1) | Improved, includes sci-fi movies |
| (3,1,1) | Weak, unstable recommendations |
| (1,3,1) | Best — consistent sci-fi matches |

---

## 🧠 Key Insights

- Title-heavy weighting causes keyword overfitting  
- Genre provides strongest and most stable signal  
- Balanced weights improve stability but not optimal  
- Description signal currently underutilized  

---

## ✅ Final Decision

Selected weights:(1,3,1)

Reason:
- Best balance of relevance and stability  
- Reduces noise compared to baseline  
- Produces consistent genre-aligned recommendations  

---

## ⚠️ Observed Limitation

- Presence of noisy recommendations (e.g., “next”, “9”)  
- Indicates weak filtering in TF-IDF representation  

---

## 📊 System Status

✔ Feature weighting implemented  
✔ Experiments completed  
✔ Best configuration selected  
⚠ Output quality still needs refinement  

---

## 🚀 Next Step

Refine TF-IDF:
- remove stopwords  
- limit vocabulary  
- reduce noise  

---

## ⚡ Summary

Feature weighting improves recommendation quality, with genre emerging as the dominant signal, but TF-IDF noise still limits performance.

---


## Date: 2 April 2026
---

## 🎯 Objective
Improve recommendation quality by refining TF-IDF representation and validating configurations.

---

## ✅ Work Done

### 1. TF-IDF Refinement

- Added stopwords removal:
  - `stop_words='english'`
- Limited vocabulary size:
  - `max_features=5000`

---

### 2. Experiments Conducted

Tested multiple TF-IDF configurations:

| Experiment | Configuration | Observation |
|-----------|-------------|------------|
| A | stop_words | Reduced basic noise, but weak results |
| B | stop_words + max_features | Significant improvement in relevance |
| C | + ngrams | Increased sparsity, unstable results |
| D | + max_df | No significant improvement |

---

### 3. Feature Weight Validation

Tested weight combinations:

| Weights (title, genre, description) | Observation |
|-----------------------------------|------------|
| (1,1,1) | Balanced but weak signal |
| (2,2,1) | Over-amplified title/genre |
| (3,1,1) | Title bias increased |
| (1,3,1) | Best performance (genre dominant) |
| (0.5,3,1) | No meaningful improvement |

---

### 4. Generalization Testing

Validated system on multiple inputs:

- Inception ✔  
- Bird Box ✔  

Observations:
- Consistent sci-fi / dystopian clustering
- Reduced random/noisy outputs
- Stable ranking across inputs

---

## 🧠 Key Learnings

- Feature representation has more impact than model complexity
- stop_words removes common noise
- max_features removes weak/rare signals
- ngrams can hurt performance on small datasets
- Not all hyperparameters improve results
- Empirical validation is required for tuning decisions

---

## 📊 Final Configuration

```python
TfidfVectorizer(
    stop_words='english',
    max_features=5000
)
