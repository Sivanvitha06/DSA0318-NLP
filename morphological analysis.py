import nltk
from nltk.stem import PorterStemmer, WordNetLemmatizer
from nltk.corpus import wordnet

# Download the necessary resources
nltk.download('wordnet')
nltk.download('omw-1.4')

# Initialize the Porter Stemmer and WordNet Lemmatizer
stemmer = PorterStemmer()
lemmatizer = WordNetLemmatizer()

# Example words for morphological analysis
words = ["running", "ran", "easily", "fairly", "better", "studies"]

# Perform stemming and lemmatization
for word in words:
    stemmed_word = stemmer.stem(word)
    lemmatized_word = lemmatizer.lemmatize(word)
    
    # For more accurate lemmatization, specify the part of speech (POS) if known
    lemmatized_word_with_pos = lemmatizer.lemmatize(word, pos=wordnet.VERB)
    
    print(f"Original Word: {word}")
    print(f"  Stemmed: {stemmed_word}")
    print(f"  Lemmatized (default): {lemmatized_word}")
    print(f"  Lemmatized (as verb): {lemmatized_word_with_pos}")
    print()
