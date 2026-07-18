from langchain_anthropic import ChatAnthropic
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage
from dotenv import load_dotenv
load_dotenv()

model = ChatAnthropic(model='claude-haiku-4-5')

chatHistory = [
    SystemMessage(content='You are an owner of this chat application and you do not want to save tokens so you will not produce output of more than 10 line')
]

while True:
    user_input = input('you: ')
    chatHistory.append(HumanMessage(content=user_input))
    if user_input == 'stop':
        break
    result=model.invoke(chatHistory)
    chatHistory.append(AIMessage(content=result.content))
    print('AI: ',result.content)
    