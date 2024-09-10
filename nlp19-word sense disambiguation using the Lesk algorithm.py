from nltk.corpus import wordnet as wn
from nltk.tokenize import word_tokenize

def lesk_algorithm(context_sentence, ambiguous_word):
    # Tokenize the context sentence
    context = set(word_tokenize(context_sentence))
    
    # Get all synsets (senses) for the ambiguous word
    synsets = wn.synsets(ambiguous_word)
    
    if not synsets:
        return None  # If no synsets are found, return None
    
    max_overlap = 0
    best_sense = synsets[0]  # Default to the first sense
    
    for sense in synsets:
        # Get the gloss (definition) and example sentences for the sense
        sense_definition = sense.definition()
        sense_examples = ' '.join(sense.examples())
        
        # Tokenize the sense definition and examples
        sense_tokens = set(word_tokenize(sense_definition + ' ' + sense_examples))
        
        # Compute the overlap between the context and the sense tokens
        overlap = len(context.intersection(sense_tokens))
        
        # Choose the sense with the highest overlap
        if overlap > max_overlap:
            max_overlap = overlap
            best_sense = sense
    
    return best_sense

# Example usage
sentence = "I went to the bank to deposit money."
ambiguous_word = "bank"

sense = lesk_algorithm(sentence, ambiguous_word)
if sense:
    print(f"Best sense for '{ambiguous_word}': {sense.name()}")
    print(f"Definition: {sense.definition()}")
else:
    print(f"No senses found for '{ambiguous_word}'")
