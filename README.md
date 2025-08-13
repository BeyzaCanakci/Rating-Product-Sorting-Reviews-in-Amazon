# Rating Product & Sorting Reviews in Amazon

This project provides an analytical approach to evaluating product ratings and sorting customer reviews for Amazon products. The main script, `Rating_Product_&_Sorting_Reviews_in_Amazon.py`, demonstrates how to analyze product reviews, calculate meaningful product ratings, and sort reviews based on their helpfulness.

## Overview

E-commerce platforms like Amazon rely heavily on customer reviews and ratings to influence purchasing decisions. However, default rating calculations and review sortings may not always reflect the true quality of a product or the usefulness of its reviews. This project aims to:

- Compute a time-based weighted average for product ratings.
- Implement advanced review sorting using up-to-date statistical methods (e.g., Wilson Lower Bound Score).
- Extract insights from review data to help customers make informed decisions.

## Features

- **Time-Based Weighted Average**: Calculates product ratings by giving more weight to recent reviews.
- **Review Helpfulness Scoring**: Sorts reviews based on helpfulness using the Wilson Lower Bound Score, ensuring the most relevant reviews appear first.
- **Data Cleaning & Preprocessing**: Handles missing values and prepares review data for analysis.

## Getting Started

### Prerequisites

- Python 3.x
- Required Python libraries (see below)

### Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/BeyzaCanakci/Rating-Product-Sorting-Reviews-in-Amazon.git
   cd Rating-Product-Sorting-Reviews-in-Amazon
   ```

2. Install dependencies:
   ```bash
   pip install pandas numpy scipy
   ```

### Usage

Run the script:

```bash
python Rating_Product_&_Sorting_Reviews_in_Amazon.py
```

The script will process the sample review dataset, calculate weighted ratings, and output the most useful reviews according to the Wilson Lower Bound method.

## Methods Used

- **Time-Based Weighted Average**: Gives more weight to recent reviews when calculating the average rating.
- **Wilson Lower Bound Score**: Estimates the lower bound of the confidence interval for the proportion of helpful votes, helping to sort reviews by their potential usefulness.

## File Structure

```
├── Rating_Product_&_Sorting_Reviews_in_Amazon.py
├── README.md
└── (Your dataset files, if any)
```

## Example Output

- Average rating (simple and time-based)
- Top 20 most useful reviews (sorted by Wilson Lower Bound Score)

## References

- [Amazon Review Data (Sample Dataset)](https://www.kaggle.com/datasets/datafiniti/amazon-reviews)
- [Wilson Lower Bound Score - Wikipedia](https://en.wikipedia.org/wiki/Binomial_proportion_confidence_interval#Wilson_score_interval)


**Author:** Beyza Canakci  
**Contact:** [GitHub/BeyzaCanakci](https://github.com/BeyzaCanakci)
