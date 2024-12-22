from flask import Flask, request, jsonify
from google.cloud import dialogflow_v2 as dialogflow
import os

app = Flask(__name__)

# Thay thế bằng đường dẫn đến tệp JSON chứa khóa API
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "path/to/your-service-account-file.json"

# Khởi tạo client Dialogflow
dialogflow_client = dialogflow.SessionsClient()
project_id = 'your-project-id'  # Thay thế bằng ID dự án của bạn

@app.route('/chat', methods=['POST'])
def chat():
    session_id = request.remote_addr # Sử dụng địa chỉ IP làm ID phiên tạm thời
    text = request.json.get('text')
    
    session = dialogflow_client.session_path(project_id, session_id)
    
    text_input = dialogflow.TextInput(text=text, language_code='vi') # Thay đổi ngôn ngữ thành tiếng Việt
    query_input = dialogflow.QueryInput(text=text_input)
    
    response = dialogflow_client.detect_intent(session=session, query_input=query_input)
    
    return jsonify({
        'query_text': response.query_result.query_text,
        'intent': response.query_result.intent.display_name,
        'response_text': response.query_result.fulfillment_text
    })

if __name__ == '__main__':
    app.run(port=5000)
