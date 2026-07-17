from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv

load_dotenv()

model = ChatAnthropic(model='claude-haiku-4-5', )


result = model.invoke("capital of India")

print('----------------------------')

print(result.content)
