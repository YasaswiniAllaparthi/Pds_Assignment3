#Basic necessary Libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os
from nltk.tokenize import word_tokenize

# Read the CSV file into a dataframe

df=pd.read_csv('C:/Users/Chinnari/Desktop/Assignment-3/data_raw/Corona_NLP_test.csv')')

# Check for missing values in each column
missing_values <- colSums(is.na(df))

# Print the missing values count for each columnn
print(missing_values)
#Since there are no missing values the data provided is already clean