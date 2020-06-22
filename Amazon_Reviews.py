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

def stemming_and_lemmizing(text_column, nlp=spacy.load('en_core_web_sm')):
    # Generate stopwords
    stopwords = nlp.Defaults.stop_words
    doc = nlp(text_column)
    # Lemmatize all entries 
    lemmas = [token.lemma_ for token in doc]
    # Extracting only the tokens that aren't stopwords and aren't anything but purely alphabetical
    filtered_lemmas = [lem for lem in lemmas if lem.isalpha() and lem not in stopwords]
    sentences = ' '.join(updated)
    return sentences