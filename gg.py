import openai
API_KEY = open(API_KEY ,"  ").read()
openai.api.key= Your API...

chat_log=[]

while True:
    user_messeges=input("Messages")
    if user_messages.lower()== "quit":
        break
    else:]
        chat.log.append({"role": "user": "content": user_message})
        respone = openai.ChatCompeletion.create(
            model= " your model"
            messages= chat_log
        )
        assistant_respone= respone['choice'][0]['messages']['content']
        print("CHAT ", assistant_response.strip("/n)
        chat.log.append({"role": "assistant","content": assistant_response.strip("/n").strip()})
print(respone)
