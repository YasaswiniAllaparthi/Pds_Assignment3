import pandas as pd
from collections import Counter
from nltk.tokenize import word_tokenize

# Use the CSV file to populate a pandas DataFrame.
df=pd.read_csv('C:/Users/Chinnari/Desktop/Assignment-3/data_raw/Corona_NLP_test.csv')

# Construct a text corpus using the "OriginalTweet" column.
corpus = df['OriginalTweet']

# Make a new list to house the tokens.

 # Iteratively tokenize each tweet in the corpus.
tokens = []
for tweet in corpus:
    # Tokenize the tweet with NLTK's word_tokenize.
  tweet_tokens = word_tokenize(tweet)

# Add the tokens from the current tweet to the list.
tokens.extend(tweet_tokens)

# Determine the frequency of occurrence of words.
word_frequencies = Counter(tokens)

# Print the word frequencies
for word, frequency in word_frequencies.items():
  print(f'{word}: {frequency}')