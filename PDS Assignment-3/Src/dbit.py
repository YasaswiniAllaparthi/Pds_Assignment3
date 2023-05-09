import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from nltk.tokenize import word_tokenize

# Use the CSV file to populate a pandas DataFrame.
df=pd.read_csv('C:/Users/Chinnari/Desktop/Assignment-3/data_raw/Corona_NLP_test.csv')


# Construct a text corpus using the "OriginalTweet" column.
corpus = df['OriginalTweet']

# Join all tweets together into a single string
text = ' '.join(corpus)

# Tokenize the text
tokens = word_tokenize(text)

# Join the tokens together to form a single string.
processed_text = ' '.join(tokens)

# Build a word cloud
wordcloud = WordCloud(width=800, height=400, background_color='orange').generate(processed_text)

# Plot the word cloud
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.show()