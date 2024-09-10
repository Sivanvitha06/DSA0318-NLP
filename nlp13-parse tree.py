import nltk
from nltk import CFG
from nltk.parse.chart import ChartParser
grammar = CFG.fromstring("""
    S -> NP VP
    NP -> Det N | Det N PP
    VP -> V NP | V NP PP
    PP -> P NP
    Det -> 'the' | 'a'
    N -> 'cat' | 'dog' | 'telescope' | 'park'
    V -> 'saw' | 'chased'
    P -> 'in' | 'with'
""")
sentence = "the cat saw a dog".split()
parser = ChartParser(grammar)
for tree in parser.parse(sentence):
    print(tree)
    tree.pretty_print() 
    tree.draw()  
