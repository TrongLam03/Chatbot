import google.generativeai as genai
from googletrans import Translator

# Configure the Generative AI API
genai.configure(api_key="AIzaSyAPvjxOI6TXYzG5otTSEK79dWrQJAU4ZQU")

# Initialize the Generative Model
model = genai.GenerativeModel(model_name="gemini-1.5-flash")

# Initialize the Google Translate API
translator = Translator()

while True:
    text = input("You: ")
    if text.lower() == "exit":
        break
    
    # Translate user input to English
    translated_input = translator.translate(text, dest='en').text
    
    # Generate AI response
    response = model.generate_content(translated_input)
    
    # Translate AI response back to the user's language
    translated_response = translator.translate(response.text, dest='vi').text  # Change 'vi' to the user's language code
    
    print("Bot:", translated_response)
