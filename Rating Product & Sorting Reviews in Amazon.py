###################################################
# PROJECT: Rating Product & Sorting Reviews in Amazon
###################################################

###################################################
# Business Problem
###################################################
# One of the most important problems in e-commerce is calculating
# the ratings given to products after purchase in the most accurate way.
# Solving this problem means more customer satisfaction for the e-commerce site,
# better visibility for the seller, and a smooth shopping experience for the buyer.
#
# Another problem is ranking the reviews given to products correctly.
# Misleading reviews being ranked higher can directly affect the sales of a product,
# leading to both financial loss and loss of customers.
#
# Solving these two core problems will allow e-commerce sites and sellers to
# increase their sales, while customers will be able to complete their purchasing
# journey without problems.

###################################################
# Dataset Story
###################################################
# The dataset contains Amazon product data, including product categories
# and various metadata. It contains the ratings and reviews for the most-reviewed
# product in the electronics category.
#
# Variables:
# reviewerID: User ID
# asin: Product ID
# reviewerName: User Name
# helpful: Helpfulness rating of the review
# reviewText: Review text
# overall: Product rating
# summary: Review summary
# unixReviewTime: Review time (Unix timestamp)
# reviewTime: Review time (raw format)
# day_diff: Days since the review was written
# helpful_yes: Number of times the review was marked helpful
# total_vote: Total number of votes the review received

###################################################
# TASK 1: Calculate Average Rating According to Recent Reviews
# and Compare With Existing Average Rating
###################################################
# Step 1: Read the dataset and calculate the product’s average rating.
import pandas as pd
import math
import scipy.stats as st

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.width', 500)
pd.set_option('display.expand_frame_repr', False)
pd.set_option('display.float_format', lambda x: '%.5f' % x)
df = pd.read_csv("/Users/beyzacanakci/Desktop/miuul/Rating Product&SortingReviewsinAmazon/amazon_review.csv")
df.head()
df_mean = df["overall"].mean()
print("Current Average Rating:", df_mean)


# Step 2: Calculate the time-based weighted average rating.
df["reviewTime"] = pd.to_datetime(df["reviewTime"])
current_date = pd.to_datetime("2014-12-08")
df["days"] = (current_date - df["reviewTime"]).dt.days

def time_based_weighted_average_rating(dataframe, w1=28, w2=26, w3=24, w4=22):
    return (
        dataframe.loc[dataframe["days"] <= 30, "overall"].mean() * w1 / 100 +
        dataframe.loc[(dataframe["days"] > 30) & (dataframe["days"] <= 90), "overall"].mean() * w2 / 100 +
        dataframe.loc[(dataframe["days"] > 90) & (dataframe["days"] <= 180), "overall"].mean() * w3 / 100 +
        dataframe.loc[dataframe["days"] > 180, "overall"].mean() * w4 / 100
    )

print("Time-Based Weighted Average Rating:", time_based_weighted_average_rating(df))
print("Alternative Weights:", time_based_weighted_average_rating(df, 30, 26, 22, 22))

###################################################
# TASK 2: Determine the 20 Reviews to Display
# on the Product Detail Page

###################################################
# Step 1: Create the helpful_no variable.
df["helpful_no"] = df["total_vote"] - df["helpful_yes"]

# Step 2: Calculate score_pos_neg_diff, score_average_rating,
# and wilson_lower_bound scores, and add them to the dataset.
def score_pos_neg_diff(helpful_yes, helpful_no):
    return helpful_yes - helpful_no

def score_average_rating(helpful_yes, helpful_no):
    if helpful_yes + helpful_no == 0:
        return 0
    return helpful_yes / (helpful_yes + helpful_no)

def wilson_lower_bound(helpful_yes, helpful_no, confidence=0.95):
    """
    Calculate Wilson Lower Bound Score.
    The lower bound of the confidence interval for the Bernoulli parameter p is accepted as the WLB score.
    This score is used for product ranking.
    If scores are between 1–5, 1–3 can be marked as negative and 4–5 as positive to fit Bernoulli, 
    but this brings some issues. For better results, Bayesian Average Rating can be used.
    """
    n = helpful_yes + helpful_no
    if n == 0:
        return 0
    z = st.norm.ppf(1 - (1 - confidence) / 2)
    phat = 1.0 * helpful_yes / n
    return (phat + z * z / (2 * n) - z * math.sqrt((phat * (1 - phat) + z * z / (4 * n)) / n)) / (1 + z * z / n)
wilson_lower_bound(250,200)
# Apply functions to dataset
df["score_pos_neg_diff"] = df.apply(lambda x: score_pos_neg_diff(x["helpful_yes"], x["helpful_no"]), axis=1)
df["score_average_rating"] = df.apply(lambda x: score_average_rating(x["helpful_yes"], x["helpful_no"]), axis=1)
df["wilson_lower_bound"] = df.apply(lambda x: wilson_lower_bound(x["helpful_yes"], x["helpful_no"]), axis=1)

# Step 3: Select and display the top 20 reviews
# according to the wilson_lower_bound score.
top_20_reviews = df.sort_values("wilson_lower_bound", ascending=False).head(20)
print(top_20_reviews[["reviewText", "helpful_yes", "helpful_no", "wilson_lower_bound"]])
