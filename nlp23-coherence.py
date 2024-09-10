import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from transformers import pipeline
from nltk import sent_tokenize
embedding_model = pipeline("feature-extraction", model="sentence-transformers/paraphrase-MiniLM-L6-v2")
def get_sentence_embeddings(sentences):
    embeddings = []
    for sentence in sentences:
        embedding = embedding_model(sentence)[0]
        embeddings.append(np.mean(embedding, axis=0))  
    return np.array(embeddings)
def calculate_coherence(text):
    sentences = sent_tokenize(text)
    embeddings = get_sentence_embeddings(sentences)
    similarities = []
    for i in range(len(embeddings) - 1):
        similarity = cosine_similarity([embeddings[i]], [embeddings[i + 1]])[0][0]
        similarities.append(similarity)
    if similarities:
        coherence_score = np.mean(similarities)
    else:
        coherence_score = 0  
    return coherence_score, sentences
text = """John went to the store. He bought some milk. The milk was fresh and cold. Afterwards, he went home."""
coherence_score, sentences = calculate_coherence(text)
print(f"Coherence score: {coherence_score:.2f}")
print(f"Sentences: {sentences}")
