# The mapping From textual data to real valued vector is called feature extraction

#bag of words(BOW):-list of unique words in the text corrups

#term frequency-inverse document frequency(Tf-Idf):-to count the no of times each word appears in a document
#term frequency(tf):- (no of times t appears in document)/(no of terms in the document)
#inverse document frequency(idf):- log(N/n).where N is the no of document and n is the no of document a term t as appeared#
#TF-IDF=TF*IDF

import numpy as np
import pandas as pd
import re
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from sklearn.feature_extraction.text import TfidfVectorizer

news_dataset = pd.read_csv('/content/train.csv')
#separating the data and label
X = news_dataset['content'].values
Y = news_dataset['label'].values

# convert the textual data to Feature Vectors
vectorizer = TfidfVectorizer()
     

vectorizer.fit(X)

X = vectorizer.transform(X)