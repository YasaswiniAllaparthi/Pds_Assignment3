# Pds_Assignment3
# pip install pandas nltk
import pandas as pd
import os
from nltk.tokenize import word_tokenize

* Insert a CSV file into a pandas DataFrame.
path=os.getcwd()
print(path)
df=pd.read_csv('C:/Users/Chinnari/Desktop/Assignment-3/data_raw/Corona_NLP_test.csv')
corpus = df['OriginalTweet']
tokens = []

* Iteratively tokenize each tweet in the corpus.
for tweet in corpus:
 * Tokenize the tweet with nltk's word_tokenize.
  tweet_tokens = word_tokenize(tweet)

* Tokens from the current tweet should be added to the list.
tokens.extend(tweet_tokens)

* Print the tokens
print(tokens)

# B-bit

* Only one NLTK stop word can be downloaded.
nltk.download('stopwords')

*  Use the CSV file to populate a pandas DataFrame.
df=pd.read_csv('C:/Users/Chinnari/Desktop/Assignment-3/data_raw/Corona_NLP_test.csv')

* Extract the "OriginalTweet" column as a text corpus.
corpus = df['OriginalTweet']

* Set up the NLTK stop words
stop_words = set(stopwords.words('english'))

* At starting, create a blank list to store tokens without stop words.
filtered_tokens = []

* Iteratively remove stop words from each tweet in the corpus.
for tweet in corpus:
   * Tokenize the tweet with NLTK's word_tokenize.
  tweet_tokens = word_tokenize(tweet)

* Remove all stop words from the current tweet's tokens.
filtered_tokens.extend([token for token in tweet_tokens if token.lower() not in stop_words])

* Print the filtered tokens
print(filtered_tokens)


# C-bit

* Use the CSV file to populate a pandas DataFrame.
df=pd.read_csv('C:/Users/Chinnari/Desktop/Assignment-3/data_raw/Corona_NLP_test.csv')

* Construct a text corpus using the "OriginalTweet" column.
corpus = df['OriginalTweet']

* Make a new list to house the tokens.

 *  Iteratively tokenize each tweet in the corpus.
tokens = []
for tweet in corpus:
    * Tokenize the tweet with NLTK's word_tokenize.
  tweet_tokens = word_tokenize(tweet)

*  Add the tokens from the current tweet to the list.
tokens.extend(tweet_tokens)

* Determine the frequency of occurrence of words.
word_frequencies = Counter(tokens)

*  Print the word frequencies
for word, frequency in word_frequencies.items():
  print(f'{word}: {frequency}')

# D-bit

*  Use the CSV file to populate a pandas DataFrame.
df=pd.read_csv('C:/Users/Chinnari/Desktop/Assignment-3/data_raw/Corona_NLP_test.csv')


* Construct a text corpus using the "OriginalTweet" column.
corpus = df['OriginalTweet']

* Join all tweets together into a single string
text = ' '.join(corpus)

* Tokenize the text
tokens = word_tokenize(text)

*  Join the tokens together to form a single string.
processed_text = ' '.join(tokens)

* Build a word cloud
wordcloud = WordCloud(width=800, height=400, background_color='orange').generate(processed_text)

* Plot the word cloud
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.show()
