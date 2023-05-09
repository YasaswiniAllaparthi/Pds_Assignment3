import pandas as pd
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Only one NLTK stop word can be downloaded.
nltk.download('stopwords')

# Use the CSV file to populate a pandas DataFrame.
df=pd.read_csv('C:/Users/Chinnari/Desktop/Assignment-3/data_raw/Corona_NLP_test.csv')

# Extract the "OriginalTweet" column as a text corpus.
corpus = df['OriginalTweet']

# Set up the NLTK stop words
stop_words = set(stopwords.words('english'))

# At starting, create a blank list to store tokens without stop words.
filtered_tokens = []

# Iteratively remove stop words from each tweet in the corpus.
for tweet in corpus:
   # Tokenize the tweet with NLTK's word_tokenize.
  tweet_tokens = word_tokenize(tweet)

# Remove all stop words from the current tweet's tokens.
filtered_tokens.extend([token for token in tweet_tokens if token.lower() not in stop_words])

# Print the filtered tokens
print(filtered_tokens)
