import nltk
from nltk import CFG
grammar = CFG.fromstring("""
  S -> NP VP
  NP -> Det N | Det Adj N
  VP -> V NP | V
  Det -> 'a' | 'the'
  N -> 'cat' | 'dog' | 'birds' | 'man'
  Adj -> 'big' | 'small'
  V -> 'chases' | 'sees' | 'barks' | 'sing' | 'chase'
""")
parser = nltk.ChartParser(grammar)
def check_sentence_agreement(sentence):
    words = nltk.word_tokenize(sentence)
    try:
        trees = list(parser.parse(words))
        if trees:
            print(f"The sentence '{sentence}' follows the grammar rules.")
            for tree in trees:
                print(tree)
        else:
            print(f"The sentence '{sentence}' does not follow the grammar rules.")
    except ValueError:
        print(f"The sentence '{sentence}' does not follow the grammar rules.")
sentences = [
    "the big cat chases a dog",
    "a dog sing",
    "the birds chase the cat",
    "the man sees a birds"
]
for sentence in sentences:
    check_sentence_agreement(sentence)
