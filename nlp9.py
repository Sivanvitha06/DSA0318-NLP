import re
sentence = "The quick brown fox jumps over the lazy dog"
patterns = [
    (r'.*ing$', 'VERB'),        
    (r'.*ed$', 'VERB'),         
    (r'.*es$', 'VERB'),         
    (r'.*s$', 'NOUN'),          
    (r'^-?[0-9]+(.[0-9]+)?$', 'NUM'),
    (r'the|a|an', 'DET'),     
    (r'.*', 'NOUN')           
]
words = sentence.lower().split()
tagged_sentence = []
for word in words:
    for pattern, tag in patterns:
        if re.match(pattern, word):
            tagged_sentence.append((word, tag))
            break
print("Tagged Sentence:", tagged_sentence)
