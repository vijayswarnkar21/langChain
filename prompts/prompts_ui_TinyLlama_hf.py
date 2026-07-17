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
book_name = st.selectbox("book name",["The last chapter",
                                       "The house maid",
                                       "The silent patient",
                                       "The Fountain Head",
                                       ])

language = st.selectbox("Lanuage",["English","Hindi"])

lines = st.selectbox("Number of lines",["100", "200"])

prompt = f'Generate summary of "{book_name}" book in {language} in {lines} lines. if the book is banned in India then your output should be "This book is banned in India"'

if st.button('summerize'):
    result = model.invoke(prompt)
    st.write(result.content)