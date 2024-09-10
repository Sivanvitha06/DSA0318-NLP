import spacy
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split
nlp = spacy.load('en_core_web_sm')
dialogs = [
    ("Can you tell me the time?", "question"),
    ("I need to schedule a meeting.", "request"),
    ("Please turn off the lights.", "command"),
    ("I am going to the store.", "statement"),
    ("How are you doing today?", "question"),
    ("Let's have lunch tomorrow.", "request"),
    ("Close the door, please.", "command"),
    ("I like to read books.", "statement"),
]
texts, labels = zip(*dialogs)
pipeline = Pipeline([
    ('vectorizer', CountVectorizer()), 
    ('classifier', MultinomialNB())      
])
X_train, X_test, y_train, y_test = train_test_split(texts, labels, test_size=0.2, random_state=42)

pipeline.fit(X_train, y_train)
def predict_dialog_act(text):
    return pipeline.predict([text])[0]
test_texts = [
    "Can you help me with this task?",
    "I would like to book a flight.",
    "Turn up the volume.",
    "The weather is nice today.",
]
for text in test_texts:
    print(f"Text: {text}")
    print(f"Predicted Dialog Act: {predict_dialog_act(text)}")
    print()

