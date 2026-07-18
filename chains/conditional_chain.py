from langchain_anthropic import ChatAnthropic
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableBranch, RunnableParallel, RunnableLambda
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser, PydanticOutputParser
from langchain_core.output_parsers import pydantic
from pydantic import BaseModel, Field
from typing import Literal

load_dotenv()

model = ChatAnthropic(model='claude-haiku-4-5')

parser = StrOutputParser()


# we are usjng Paydatic because we want to force LLM to give response out of only two possiblities that is
# positive or Nagative. As out branching logic completely depende on these two litrals. If do not force LLM in thi # sway, the code will break in case response is not in required format.

class Feedback(BaseModel):
    sentiment: Literal['positive', 'nagative'] = Field(description='give the sentiment of the feedback')

parser2 = PydanticOutputParser(pydantic_object=Feedback)

prompt1 = PromptTemplate(    
    template='Classify the sentiment of follwong text into Postive or Nagative \n {feedback} \n {format_instructions}',
    input_variables=['feedback'],
    partial_variables={'format_instructions': parser2.get_format_instructions()}
)

classifier_chain = prompt1 | model | parser2

prompt2 = PromptTemplate(
    template='Write an appropriate response to this positive feedback \n {feedback}',
    input_variables=['feedback']
)

prompt3 = PromptTemplate(
    template='Write an appropriate response to this negative feedback \n {feedback}',
    input_variables=['feedback']
)

branch_chain = RunnableBranch(
    (lambda X:X.sentiment == 'positive', prompt2 | model | parser),
    (lambda X:X.sentiment == 'nagative', prompt3 | model | parser),
     RunnableLambda(lambda x: "could not find sentiment")
)

chain = classifier_chain | branch_chain

print(chain.invoke({"feedback":"this is a teriable phone"}))

chain.get_graph().print_ascii()




