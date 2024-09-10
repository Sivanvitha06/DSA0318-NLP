import random
from collections import defaultdict

# Sample tagged corpus: (word, POS tag) pairs
corpus = [
    ('I', 'PRON'), ('love', 'VERB'), ('to', 'PRT'), ('write', 'VERB'),
    ('code', 'NOUN'), ('every', 'ADJ'), ('day', 'NOUN'), ('I', 'PRON'),
    ('love', 'VERB'), ('to', 'PRT'), ('learn', 'VERB'), ('new', 'ADJ'),
    ('things', 'NOUN')
]

# Separate words and tags
words = [word for word, tag in corpus]
tags = [tag for word, tag in corpus]

# Calculate emission probabilities P(word | tag)
emission_probs = defaultdict(lambda: defaultdict(int))
tag_counts = defaultdict(int)

for word, tag in corpus:
    emission_probs[tag][word] += 1
    tag_counts[tag] += 1

# Normalize to get probabilities
for tag in emission_probs:
    total = sum(emission_probs[tag].values())
    for word in emission_probs[tag]:
        emission_probs[tag][word] /= total

# Calculate transition probabilities P(tag_n | tag_(n-1))
transition_probs = defaultdict(lambda: defaultdict(int))
for i in range(1, len(tags)):
    prev_tag = tags[i-1]
    current_tag = tags[i]
    transition_probs[prev_tag][current_tag] += 1

# Normalize transition probabilities
for prev_tag in transition_probs:
    total = sum(transition_probs[prev_tag].values())
    for current_tag in transition_probs[prev_tag]:
        transition_probs[prev_tag][current_tag] /= total

# POS tagging for a sentence
sentence = ['I', 'love', 'to', 'learn', 'code']

# Initialize the first word's possible POS tags randomly based on the tag counts
pos_sequence = [random.choice(list(tag_counts.keys()))]

# For each word in the sentence, choose the most probable POS tag based on the previous tag
for i in range(1, len(sentence)):
    word = sentence[i]
    prev_tag = pos_sequence[i - 1]
    
    # Find the tag with the highest transition and emission probability
    best_tag = max(tag_counts.keys(), key=lambda tag: transition_probs[prev_tag].get(tag, 0) * emission_probs[tag].get(word, 0))
    
    pos_sequence.append(best_tag)

print("Sentence:", ' '.join(sentence))
print("POS Tags:", ' '.join(pos_sequence))
