import spacy

# Load the spaCy English language model
nlp = spacy.load("en_core_web_sm")

def extract_noun_phrases_and_meanings(text):
    # Process the text using spaCy NLP pipeline
    doc = nlp(text)
    
    noun_phrases = []
    
    # Extract noun phrases using dependency parsing
    for np in doc.noun_chunks:
        # Get the noun phrase and its root word
        noun_phrase = np.text
        root_word = np.root.text
        
        # Extract entity types for meanings, if available
        entity = [ent.label_ for ent in doc.ents if ent.text == noun_phrase]
        meaning = entity[0] if entity else "No named entity found"
        
        noun_phrases.append((noun_phrase, root_word, meaning))
    
    return noun_phrases

# Example sentence
sentence = "Apple is looking at buying a U.K. startup for $1 billion."

# Extract noun phrases and their meanings
noun_phrases = extract_noun_phrases_and_meanings(sentence)

# Display the extracted noun phrases and their semantic meanings
print("Extracted Noun Phrases and Their Meanings:")
for noun_phrase, root_word, meaning in noun_phrases:
    print(f"Noun Phrase: '{noun_phrase}', Root: '{root_word}', Meaning: {meaning}")
