import nltk
from nltk.stem import PorterStemmer
nltk.download('punkt')
ps = PorterStemmer()
words = ["running", "jumps", "easily", "flying", "cats", "happiness", "studies"]
stemmed_words = [ps.stem(word) for word in words]
for word, stemmed in zip(words, stemmed_words):
    print(f"Original: {word} --> Stemmed: {stemmed}")
