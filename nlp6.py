import random
import re
from collections import defaultdict, Counter
def preprocess_text(text):
    words = re.findall(r'\b\w+\b', text.lower())
    return words
def build_bigram_model(words):
    bigram_model = defaultdict(Counter)
    for i in range(len(words) - 1):
        current_word = words[i]
        next_word = words[i + 1]
        bigram_model[current_word][next_word] += 1
    return bigram_model
def generate_text(bigram_model, start_word, num_words):
    current_word = start_word
    generated_text = [current_word]

    for _ in range(num_words - 1):
        next_words = bigram_model[current_word]
        if not next_words:
            break
        next_word = random.choices(list(next_words.keys()), list(next_words.values()))[0]
        generated_text.append(next_word)
        current_word = next_word

    return ' '.join(generated_text)
if __name__ == "__main__":
    sample_text = """
    In the beginning God created the heaven and the earth. And the earth was without form, and void; 
    and darkness was upon the face of the deep. And the Spirit of God moved upon the face of the waters. 
    And God said, Let there be light: and there was light.
    """

    words = preprocess_text(sample_text)
    bigram_model = build_bigram_model(words)
    start_word = random.choice(words)
    generated_text = generate_text(bigram_model, start_word, 50)
    print(generated_text)
