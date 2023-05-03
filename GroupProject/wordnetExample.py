import nltk
nltk.download('wordnet')
from nltk.corpus import wordnet as wn



# look up  a word using synsets()

print(wn.synsets('soup'))

