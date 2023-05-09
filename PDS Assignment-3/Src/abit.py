# pip install pandas nltk
import pandas as pd
import os
from nltk.tokenize import word_tokenize

# Insert a CSV file into a pandas DataFrame.
path=os.getcwd()
print(path)

df=pd.read_csv('C:/Users/Chinnari/Desktop/Assignment-3/data_raw/Corona_NLP_test.csv')

corpus = df['OriginalTweet']

tokens = []

# Iteratively tokenize each tweet in the corpus.
for tweet in corpus:
  # Tokenize the tweet with nltk's word_tokenize.
  tweet_tokens = word_tokenize(tweet)

# Tokens from the current tweet should be added to the list.
tokens.extend(tweet_tokens)

# Print the tokens
print(tokens)
