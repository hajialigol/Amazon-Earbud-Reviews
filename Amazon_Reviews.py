import pandas as pd
import os
import re
import matplotlib.pyplot as plt
import seaborn as sns

amazon_reviews = pd.read_csv("AllProductReviews.csv")

# Find the amount of words for a given review
def amount_of_words(review):
    word_list = review.split()
    length_of_words = [len(word) for word in word_list]
    amount_of_words = sum(length_of_words)
    return amount_of_words

# Generate the average word length for a given review
def avg_word_length(review):
    word_list = review.split()
    length_of_words = [len(word) for word in word_list]
    number_of_words = len(word_list)
    if number_of_words == 0:
        return None
    else:
        return sum(length_of_words)/number_of_words
