from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate

load_dotenv()

model = ChatAnthropic(model='claude-haiku-4-5')

template1 = PromptTemplate(
    template='Write a detailed report on {topic}',
    input_variables=['topic']
)

template2 = PromptTemplate(
    template='Write a 5 line summary on the following text. /n {text}',
    input_variables=['text']
)


prompt1 = template1.invoke({'topic': 'Dictatorship in India'})
result = model.invoke(prompt1)
prompt2 = template2.invoke({'text': result})
result = model.invoke(prompt2)

print(result.content)

