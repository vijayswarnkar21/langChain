from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv
import streamlit as st
from langchain_core.prompts import PromptTemplate,load_prompt

load_dotenv()

model = ChatAnthropic(model='claude-haiku-4-5', )

st.header('Reasearch Tool')

book_name = st.selectbox("book name",["The last chapter",
                                       "The house maid",
                                       "The silent patient",
                                       "The Fountain Head",
                                       "The Satanic Verses by Salman Rushdie"
                                       ])

language = st.selectbox("Lanuage",["English","Hindi"])

lines = st.selectbox("Number of lines",["10", "50", "100", "200"])

template = load_prompt('template.json')

if st.button('Summarize'):
    chain = template | model
    result = chain.invoke({
        'book_name':book_name,
        'language':language,
        'lines':lines
    })
    st.write(result.content)