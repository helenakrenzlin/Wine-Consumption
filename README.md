# 🍷 Wine Market Intelligence: Merging Expert & Consumer Data

## 📖 Introduction
This project aims to bridge the gap between **Expert Ratings** (sourced from professional APIs) and **Consumer Sentiment** (extracted from a large-scale wine dataset). 

---

## 📊 Data Overview & Sources
The analysis integrates two primary data streams to create a unified "master" dataset:

* **Primary Dataset (130k rows):** A comprehensive collection of wine reviews, including variety, province, and taster information.
* **Secondary API Data (7k rows):** Enriched metadata fetched from professional wine endpoints (Red, White, Rosé, and Sparkling) containing expert ratings, review counts, and high-resolution image links.
* **Key Challenge:** Merging was performed using a **Fuzzy Logic** approach (Winery + Country) to resolve naming inconsistencies and character encoding differences between the two disparate sources.



---

## ❓ Research Hypotheses & Conclusions

### **Hypothesis 1:Higher priced wines have the highest score ratings**
> *“Does price dictate quality in the global market?”*
* **Conclusion:** 

### **Hypothesis 2: Market Visibility & Pricing**
> *“Wine-producing countries with the highest number of reviews/ratings tend to sell more expensive wines, indicating that market demand and visibility influence price levels.”*
* **Conclusion:** 

### **Hypothesis 3: Tradition vs. Perceived Quality**
> *“European wine-producing countries have higher average ratings than other regions, suggesting that historical winemaking tradition positively influences perceived quality.”*
* **Conclusion:** 

---

## 🛠 Methodology

### 1. Data Cleaning & Preparation
* **Surgical Null Removal:** Dropped 63 missing values for `Province` and 1 for `Variety` to ensure geographical analysis was 100% accurate.
* **Handling Missing Data:** Addressed 84,329 missing values in the API merge by filling with average rating points
* **Standardization:** Used `.str.title()` and `.rename()` to ensure all 130k records follow a consistent, database-ready naming convention.

### 2. Analysis
* **Fuzzy Matching:** Utilized `difflib` with a 0.6 similarity cutoff to bridge the gap between inconsistent winery names across datasets.
* **Granular Categorization:** Re-mapped 500+ unique `Varieties` into 5 clean `Wine_Categories` (Red, White, Rosé, Sparkling, Dessert) using custom keyword-based logic.

### 3. Visualization
* **Regression Analysis:** 