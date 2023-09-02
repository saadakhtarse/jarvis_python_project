#API key

fileopen = open("Data\\API.txt","r")
API = fileopen.read()
fileopen.close()

#importing
import openai
from dotenv import load_dotenv


#coding
openai.api_key = API
load_dotenv()
completion = openai.Completion()

def ReplayBrain(question, chat_log= None):
    FileLog = open("Data\\API.txt","r")
    chat_log_template = FileLog.read()
    FileLog.close()

    if chat_log is None:
        chat_log = chat_log_template
    
    prompt = f'{chat_log}You: {question} \nBuddy: '
    response = completion.create(
        model="code-davinci-002",
        prompt = prompt,
        temperature = 0.5,
        max_tokens = 60,
        top_p = 0.3,
        frequency_penalty = 0.5,
        presence_penalty = 0)
    answer = response.choices[0].test.strip()
    chat_log_template_update = chat_log_template + f"\nYou: {question} \n Buddy: {answer}"
    FileLog = open("DataBase\\chat_log.txt","w")
    FileLog.write(chat_log_template_update)
    FileLog.close()
    return answer


reply = ReplayBrain("How are you?")
print(reply)


