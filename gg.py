import google.generativeai as palm

# Khởi tạo với API Key của bạn
palm.configure(api_key="AIzaSyDjI-t8qy06KGh2d46TmHTen3S24hB35jE")

# Ví dụ về việc tạo phản hồi từ chat bot
def chat_with_palm(prompt):
    response = palm.chat(prompt)
    return response

# Ví dụ sử dụng
if __name__ == "__main__":
    prompt = "Hi, how can I assist you today?"
    response = chat_with_palm(prompt)
    print("Bot:", response)
