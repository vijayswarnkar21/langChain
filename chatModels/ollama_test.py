from langchain_ollama import ChatOllama

# Initialize ChatOllama and point it directly to the working IP address
model = ChatOllama(
    model="qwen2.5:0.5b",
    base_url="http://127.0.0.1:11434",  # <--- Bypasses localhost DNS lookup issues
    temperature=0.7
)

# Test invocation
result = model.invoke("What is the capital of India")

print("\n--- Response ---")
print(result.content)