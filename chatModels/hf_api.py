from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv

load_dotenv()

# To target an exact provider, pass the `provider` argument
Varllm = HuggingFaceEndpoint(
    repo_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task="text-generation",
    provider="featherless-ai"  # <--- Bypasses speed routing and hits Featherless directly!
)

model = ChatHuggingFace(llm=Varllm)

result = model.invoke("What is the capital of India")

print(result.content)