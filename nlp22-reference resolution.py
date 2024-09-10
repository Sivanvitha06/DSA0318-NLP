import spacy
def resolve_references(text):
    nlp = spacy.load('en_core_web_sm')
    doc = nlp(text)
    resolved_text = []
    for token in doc:
        if token.pos_ == "PRON": 
            antecedent = None
            for ent in reversed(doc.ents):
                if ent.end < token.i and ent.label_ in ["PERSON", "ORG", "GPE"]:  
                    antecedent = ent
                    break
            
            if antecedent:
                resolved_text.append(antecedent.text)  
            else:
                resolved_text.append(token.text)  
        else:
            resolved_text.append(token.text)  
    return " ".join(resolved_text)
text = "John went to the store. He bought some milk."
resolved = resolve_references(text)
print("Original text: ", text)
print("Resolved text: ", resolved)
