from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv

load_dotenv()

model = ChatAnthropic(model='claude-haiku-4-5')

# The concept of memory will be in phase 2
memory = []

while True:
    user_input = input('you: ')
    memory.append(user_input)
    if user_input == 'stop':
        break
    # in phase 1 only user_input will be passed
    result=model.invoke(memory)
    memory.append(result.content)
    print('AI: ',result.content)
        
