import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QTextEdit, QLineEdit, QPushButton
import google.generativeai as genai
from googletrans import Translator

# Configure the Generative AI API
genai.configure(api_key="AIzaSyAPvjxOI6TXYzG5otTSEK79dWrQJAU4ZQU")

# Initialize the Generative Model
model = genai.GenerativeModel(model_name="gemini-1.5-flash")

# Initialize the Google Translate API
translator = Translator()

class ChatbotUI(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Set up the layout and widgets
        self.setWindowTitle('Bách khoa của lâm')
        self.setGeometry(100, 100, 400, 500)
        
        # Apply improved stylesheet for styling
        self.setStyleSheet("""
            QWidget {
                background-color: #e0f7fa;
            }
            QTextEdit {
                background-color: #ffffff;
                color: #333333;
                font-family: 'Arial';
                font-size: 14px;
                border: 1px solid #ccc;
                padding: 10px;
                border-radius: 10px;
                box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            }
            QLineEdit {
                background-color: #ffffff;
                font-family: 'Arial';
                font-size: 14px;
                border: 1px solid #ccc;
                padding: 10px;
                border-radius: 10px;
                box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            }
            QPushButton {
                background-color: #00bcd4;
                color: white;
                font-family: 'Arial';
                font-size: 14px;
                padding: 10px;
                border: none;
                border-radius: 20px;
                box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
            }
            QPushButton:hover {
                background-color: #0097a7;
            }
            QPushButton:pressed {
                background-color: #00838f;
            }
        """)

        layout = QVBoxLayout()
        
        self.chat_display = QTextEdit(self)
        self.chat_display.setReadOnly(True)
        
        self.input_text = QLineEdit(self)
        self.input_text.setPlaceholderText('Nhập tin..')

        self.send_button = QPushButton('Gửi', self)
        self.send_button.clicked.connect(self.send_message)
        
        layout.addWidget(self.chat_display)
        layout.addWidget(self.input_text)
        layout.addWidget(self.send_button)
        
        self.setLayout(layout)

    def send_message(self):
        user_text = self.input_text.text()
        if user_text.strip() == '':
            return

        # Display user message
        self.chat_display.append(f'You: {user_text}')

        # Translate user input to English
        translated_input = translator.translate(user_text, dest='en').text
        
        # Generate AI response
        try:
            response = model.generate_content(translated_input)
        except Exception as e:
            self.chat_display.append(f'Error: {e}')
            return

        # Translate AI response back to the user's language
        translated_response = translator.translate(response.text, dest='vi').text  # Change 'vi' to the desired language code

        # Display bot response
        self.chat_display.append(f'Bot: {translated_response}')
        
        # Clear the input field
        self.input_text.clear()

def main():
    app = QApplication(sys.argv)
    chatbot_ui = ChatbotUI()
    chatbot_ui.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
