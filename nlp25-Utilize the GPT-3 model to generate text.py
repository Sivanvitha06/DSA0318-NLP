from transformers import GPT2LMHeadModel, GPT2Tokenizer
model_name = "distilgpt2"
tokenizer = GPT2Tokenizer.from_pretrained(model_name)
model = GPT2LMHeadModel.from_pretrained(model_name)
prompt_text = "Once upon a time,"
input_ids = tokenizer.encode(prompt_text, return_tensors='pt')
output = model.generate(input_ids, max_length=100, num_return_sequences=1, temperature=0.7)
generated_text = tokenizer.decode(output[0], skip_special_tokens=True)
print("Generated Text:\n", generated_text)
