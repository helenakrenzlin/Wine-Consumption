# 🍷 Wine Market Intelligence: Merging Expert & Consumer Data

## 📖 Introduction

This project aims to bridge the gap between **Expert Ratings** (sourced from professional APIs) and **Consumer Sentiment** (extracted from a large-scale wine dataset). By identifying patterns in pricing, variety, and geography, this analysis provides a 360-degree view of the global wine market and the socio-economic drivers behind wine valuation.

---

## 📊 Data Overview & Sources

The analysis integrates two primary data streams to create a unified "master" dataset:

- **Primary Dataset (130k rows):** A comprehensive collection of wine reviews, including variety, province, and taster information.
- **Secondary API Data (7k rows):** Enriched metadata fetched from professional wine endpoints (Red, White, Rosé, and Sparkling) containing expert ratings, review counts, and high-resolution image links.
- **Key Challenge:** Merging was performed using a **Fuzzy Logic** approach (Winery + Country) to resolve naming inconsistencies and character encoding differences between the two disparate sources.

---

## ❓ Research Hypotheses & Conclusions

### **Hypothesis 1:Higher priced wines have the highest score ratings**

> _“Does price dictate quality in the global market?”_

- **Conclusion:** Not confirmed - ur regression analysis shows a negligible correlation between price and score. The data proves that price is a poor predictor of quality, as high-scoring "Hidden Gems" exist at nearly every price tier.

### **Hypothesis 2: Market Visibility & Pricing**

> _“Wine-producing countries with the highest number of reviews/ratings tend to sell more expensive wines, indicating that market demand and visibility influence price levels.”_

- **Conclusion 2.1:(Volume vs. Price):** Counter-intuitive. There is a slight negative correlation. Countries with the highest review volume (like the USA) actually maintain a lower average price point, indicating a focus on mass-market accessibility over scarcity-based pricing.
- **Conclusion 2.2 (Score vs. Price):** No Significant Link. Average scores do not scale linearly with average prices. Scoring appears to be driven by other variables (e.g. vintage, technique) not captured by price tags alone.

### **Hypothesis 3: Tradition vs. Perceived Quality**

> _“European wine-producing countries have higher average ratings than other regions, suggesting that historical winemaking tradition positively influences perceived quality.”_

- **Conclusion:** European wines in this dataset actually trended slightly lower in average scores compared to certain New World regions. However, this is heavily influenced by the massive volume of USA-based reviews, which may introduce a regional advantage in the data.

## 🛠 Methodology

### 1. Data Cleaning & Preparation

- **Surgical Null Removal:** Dropped 63 missing values for `Province` and 1 for `Variety` to ensure geographical analysis was 100% accurate.
- **Handling Missing Data:** Addressed 84,329 missing values in the API merge by filling with average price/point values.
- **Standardization:** Used `.str.title()` and `.rename()` to ensure all 130k records follow a consistent, database-ready naming convention.

### 2. Analysis

- **Fuzzy Matching:** Utilized `difflib` with a 0.6 similarity cutoff to bridge the gap between inconsistent winery names across datasets.
- **Granular Categorization:** Re-mapped 500+ unique `Varieties` into 5 clean `Wine_Categories` (Red, White, Rosé, Sparkling, Dessert) using custom keyword-based logic.

### 3. Visualization

- **Regression Analysis:** Utilized scatter plots with trend lines to visualize the (lack of) relationship between price and quality.
- **Comparative Distribution:** Employed Box Plots and Dual-Axis Bar/Line charts to contrast "Old World" vs. "New World" performance.

---

## 💡 Main Findings & Insights

- **The "Value" Sweet Spot:** Argentina and Chile emerged as the leaders in "Value-to-Quality" ratios, offering premium quality at mid-tier prices.
- - **Geographic Bias:** Professional ratings were more densely populated for French and Italian wineries compared to New World regions(excluding USA), indicating a lingering "traditionalist" bias in expert scoring.
- **US Dominance:** The volume of US winery reviews creates a significant statistical weight that must be normalized to compare other regions fairly.

---

## 🚀 Further Questions & Next Steps

- **Sentiment Analysis:** Further investigate the US review volume dominance. We plan to normalize these values to compare the "top-reviewed" European countries against US counterpart on a level playing field.
- **Macro-Consumption Analysis:** Integrate global wine consumption data (per capita) to determine if high-consuming nations (like Portugal or France) are more "price-sensitive" or "quality-driven" compared to emerging markets.
- **Vintage & Climate Impact:** Extract "Year" from the Title strings using Regex to analyze how aging and specific harvest years (vintages) correlate with both expert scores and market price.
- **Characteristic Mapping (NLP):** Perform Natural Language Processing (NLP) on the raw review descriptions to extract "Characteristic Tags" (e.g., tannic, oaky, fruity, acidic). This will allow us to see which flavor profiles command the highest price premiums.

---

## 🔗 Links
- **Data Source 1:** * [**Kaggle Wine Reviews Dataset**](https://www.kaggle.com/datasets/zynicide/wine-reviews) — *Primary source for 130k consumer reviews.*
- **Data Source 2:** [**Wine APIs**] (https://sampleapis.com/api-list/wines)
- **Link to Presentation:** https://prezi.com/p/mzj917xxyccb/plan-de-marketing-global-para-bodegas/
