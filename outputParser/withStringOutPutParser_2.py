# StringOutPutParser helps when we chain output of one invocation 
# to another model invocation and make the code more readable 

from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

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

parser = StrOutputParser()

chain = template1 | model | parser |  template2 | model
result = chain.invoke({'topic':'black hole'})

print(result.content)