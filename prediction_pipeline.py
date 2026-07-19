import pickle
import re
from pathlib import Path

from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from sklearn.feature_extraction.text import CountVectorizer

ROOT = Path(__file__).resolve().parent

with (ROOT / 'artifacts' / 'vocab.txt').open() as file:
  tokens = file.read().splitlines()

with (ROOT / 'static' / 'model' / 'model.pickle').open('rb') as file:
  model = pickle.load(file)

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

def get_prediction(text):
  preprocessed_txt = preprocessing(text)
  vectorized_txt = cv.transform(preprocessed_txt)

  result = model.predict(vectorized_txt)[0]

  if result == 1:
    return "Positive Comment"
  else:
    return "Negative Comment"
