from transformers import AutoTokenizer, AutoModelForCausalLM

MODEL_PATH = "./model"

print("Loading Qwen model...")

tokenizer = AutoTokenizer.from_pretrained(
    MODEL_PATH,
    local_files_only=True
)

model = AutoModelForCausalLM.from_pretrained(
    MODEL_PATH,
    local_files_only=True,
    dtype="auto"
)

print("Model loaded successfully!")
print("Type 'exit' to quit.\n")

while True:
    question = input("You: Hi! How can I help you today?\n")

    if question.lower() in ["exit", "quit"]:
        print("Bye!")
        break

    # Convert question to model input
    messages = [
        {"role": "user", "content": question}
    ]

    text = tokenizer.apply_chat_template(
        messages,
        tokenize=False,
        add_generation_prompt=True
    )

    inputs = tokenizer(
        text,
        return_tensors="pt"
    )

    # Generate response
    outputs = model.generate(
        **inputs,
        max_new_tokens=200,
        temperature=0.7,
        do_sample=True
    )

    # Remove the original prompt from output
    generated_tokens = outputs[0][inputs["input_ids"].shape[1]:]

    response = tokenizer.decode(
        generated_tokens,
        skip_special_tokens=True
    )

    print(f"AI: {response}\n")