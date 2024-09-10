from transformers import pipeline

translator = pipeline("translation_en_to_fr")
english_text = "Hello, how are you doing today?"
french_text = translator(english_text, max_length=40)[0]["translation_text"]

print(f"English Text: {english_text}")
print(f"French Text: {french_text}")
