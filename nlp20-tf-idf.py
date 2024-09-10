from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

# Sample documents (corpus)
documents = [
    "The sky is blue.",
    "The sun is bright today.",
    "The sun in the sky is bright.",
    "We can see the shining sun, the bright sun."
]

# Create a TF-IDF Vectorizer
vectorizer = TfidfVectorizer()

# Generate the TF-IDF vectors for the documents
tfidf_matrix = vectorizer.fit_transform(documents)

# Function to rank documents based on a query
def rank_documents(query, documents):
    # Transform the query into a TF-IDF vector
    query_vector = vectorizer.transform([query])
    
    # Compute cosine similarity between the query and all documents
    cosine_similarities = cosine_similarity(query_vector, tfidf_matrix).flatten()
    
    # Rank the documents based on similarity scores
    ranked_indices = np.argsort(-cosine_similarities)  # Sort in descending order
    
    # Return the ranked documents with their similarity scores
    ranked_documents = [(documents[i], cosine_similarities[i]) for i in ranked_indices]
    
    return ranked_documents

# Example query
query = "bright sun"

# Rank the documents based on the query
ranked_docs = rank_documents(query, documents)

# Print the ranked documents and their similarity scores
print("Ranked Documents:")
for doc, score in ranked_docs:
    print(f"Document: '{doc}', Similarity Score: {score:.4f}")
