from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv

load_dotenv()

model = ChatAnthropic(model='claude-haiku-4-5')

while True:
    user_input = input('you: ')
    if user_input == 'stop':
        break
    result=model.invoke(user_input)
    print('AI: ',result.content)
        
