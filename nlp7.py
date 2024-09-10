import nltk

# Download the necessary NLTK data files
nltk.download('punkt')  # For tokenization
nltk.download('averaged_perceptron_tagger')  # For POS tagging

# Sample text
text = "The quick brown fox jumps over the lazy dog."

# Tokenize the text into words
words = nltk.word_tokenize(text)

# Perform part-of-speech tagging
pos_tags = nltk.pos_tag(words)

# Print the POS tags
print("Part-of-Speech Tags:")
for word, tag in pos_tags:
    print(f"{word}: {tag}")
