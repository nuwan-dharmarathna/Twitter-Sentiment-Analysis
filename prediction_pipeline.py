# import tensorflow as tf
import numpy as np
import pandas as pd
import re
import string
import pickle

import re
import nltk

# nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
  
# open vocab.txt as tokens
with open('./artifacts/vocab.txt', 'r') as file:
  tokens = file.read().splitlines()
  
print("vocab read sucessfully!")

# load the model
# model = tf.keras.models.load_model('senti_model.h5')

# load model
with open('model.pickle', 'rb') as f:
    model = pickle.load(f)

# vectorization
from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer(vocabulary=tokens)
  
# Text preprocessing
def preprocessing(sent):

  def remove_links(text):
    text = re.sub(r'http\S+', '', text)
    return text

  review = sent.lower() #Convert all letters to the lowercase
  review = remove_links(review)  # Remove links from the text
  review = re.sub('[^a-zA-Z]', ' ', review) #Remove all punchuation marks, numbers except a-z and A-Z
  review = review.split() # Before stemming, should do split it
  ps = PorterStemmer()
  all_stopwords = stopwords.words('english')
  all_stopwords.remove('not')
  review = [ps.stem(word) for word in review if not word in set(all_stopwords)]
  review = ' '.join(review)
  return [review]

# vectoried the pre-processed text

import numpy as np

def get_prediction(text):
  preprocessed_txt = preprocessing(text)
  vectorized_txt = cv.transform(preprocessed_txt)

  result = model.predict(vectorized_txt)
  
  print(result)
  
  # Since it's binary classification, you can round the prediction to get the class label (0 or 1)
  # predicted_class = np.round(result).astype(int)[0][0]

  if result == 1:
    return "Positive Comment"
  else:
    return "Negative Comment"


# # New test value
# test = "Fuck you"


# res = get_prediction(test)

# print(res)