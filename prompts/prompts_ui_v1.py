from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
import streamlit as st
from langchain_core.prompts import PromptTemplate,load_prompt
load_dotenv()

# To target an exact provider, pass the `provider` argument
Varllm = HuggingFaceEndpoint(
    repo_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task="text-generation",
    provider="featherless-ai"  # <--- Bypasses speed routing and hits Featherless directly!
)

model = ChatHuggingFace(llm=Varllm)


st.header('Reasearch Tool')
user_input = st.text_input('Enter Prompt')

if st.button('summerize'):
    result = model.invoke(user_input)
    st.write(result.content)