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

# 🍷 Wine Market Intelligence: Merging Expert & Consumer Data

## 📖 Introduction
This project aims to bridge the gap between **Expert Ratings** (sourced from professional APIs) and **Consumer Sentiment** (extracted from a large-scale wine dataset). By identifying patterns in pricing, variety, and geography, this analysis provides a 360-degree view of the global wine market and the socio-economic drivers behind wine valuation.

---

## 📊 Data Overview & Sources
The analysis integrates two primary data streams to create a unified "master" dataset:

* **Primary Dataset (130k rows):** A comprehensive collection of wine reviews, including variety, province, and taster information.
* **Secondary API Data (7k rows):** Enriched metadata fetched from professional wine endpoints (Red, White, Rosé, and Sparkling) containing expert ratings, review counts, and high-resolution image links.
* **Key Challenge:** Merging was performed using a **Fuzzy Logic** approach (Winery + Country) to resolve naming inconsistencies and character encoding differences between the two disparate sources.



---

## ❓ Research Hypotheses & Conclusions

### **Hypothesis 1: Price vs. Quality**
> *“Does price dictate quality in the global market?”*
* **Conclusion:** While a positive correlation exists, certain provinces (specifically in the "Old World") offer "Expert-Rated" quality at a significantly lower consumer price point than their "New World" counterparts.

### **Hypothesis 2: Market Visibility & Pricing**
> *“Wine-producing countries with the highest number of reviews/ratings tend to sell more expensive wines, indicating that market demand and visibility influence price levels.”*
* **Conclusion:** [Insert your result here, e.g., Confirmed for France and US, but disproven for high-volume regions like Spain and Chile.]

### **Hypothesis 3: Tradition vs. Perceived Quality**
> *“European wine-producing countries have higher average ratings than other regions, suggesting that historical winemaking tradition positively influences perceived quality.”*
* **Conclusion:** [Insert your result here, e.g., Confirmed; European distributions show higher medians and lower variance in ratings.]

---

## 🛠 Methodology

### 1. Data Cleaning & Preparation
* **Surgical Null Removal:** Dropped 63 missing values for `Province` and 1 for `Variety` to ensure geographical analysis was 100% accurate.
* **Handling Missing Data:** Addressed 84,329 missing values in the API merge by [Insert choice: e.g., filling with median price/points or maintaining as original].
* **Standardization:** Used `.str.title()` and `.rename()` to ensure all 130k records follow a consistent, database-ready naming convention.

### 2. Analysis
* **Fuzzy Matching:** Utilized `difflib` with a 0.6 similarity cutoff to bridge the gap between inconsistent winery names across datasets.
* **Granular Categorization:** Re-mapped 500+ unique `Varieties` into 5 clean `Wine_Categories` (Red, White, Rosé, Sparkling, Dessert) using custom keyword-based logic.

### 3. Visualization
* **Regression Analysis:** Scatter plots with trend lines were used to test the correlation between Visibility (Review Count) and Price.
* **Distribution Analysis:** Box plots were utilized to compare the rating spreads between "Old World" (Europe) and "New World" regions.

---

## 💡 Main Findings & Insights
* **The "Value" Sweet Spot:** Wines from **[Insert Province]** showed the highest "Rating-to-Price" ratio, offering premium quality at mid-tier prices.
* **Match Success:** Successfully matched **35%** of the total records with expert API data, providing a significant sample for high-end market analysis.
* **Geographic Bias:** Professional ratings were more densely populated for French and Italian wineries compared to New World regions, indicating a lingering "traditionalist" bias in expert scoring.

---

## 🚀 Further Questions & Next Steps
* **Sentiment Analysis:** Perform Natural Language Processing (NLP) on the `Description` column to see if "Expert" vocabulary (API) differs significantly from "Consumer" vocabulary.
* **Automated Pipeline:** Transition the current manual CSV download and cleaning process into a fully automated Python script using the Google Drive API.

---

## 🔗 Links
* **Data Source 1:** [Link to Original Dataset]
* **Data Source 2:** [Link to API Documentation]
* **Link to Presentation:**