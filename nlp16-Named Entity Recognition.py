import spacy
def perform_ner(text):
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(text)
    entities = [(entity.text, entity.label_) for entity in doc.ents]
    return entities
if __name__ == "_main_":
    text = "Apple is looking at buying U.K. startup for $1 billion"
    entities = perform_ner(text)
    print("Named Entities:")
    for entity, label in entities:
        print(f"Entity: {entity}, Label: {label}")
