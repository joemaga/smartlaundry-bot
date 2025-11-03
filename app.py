import os
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from src.chatbot import BusinessChatbot

app = Flask(__name__)
chatbot = BusinessChatbot()

@app.route('/')
def home():
    return "🤖 SmartLaundry Cloud Server is Running!"

@app.route('/test')
def test():
    response = chatbot.process_message("Olá, teste do servidor na nuvem!")
    return f"Chatbot test: {response}"

@app.route('/webhook/whatsapp', methods=['POST'])
def whatsapp_webhook():
    incoming_msg = request.values.get('Body', '').strip()
    from_number = request.values.get('From', '')
    
    print(f"📱 Message from {from_number}: {incoming_msg}")
    
    if incoming_msg:
        response_text = chatbot.process_message(incoming_msg)
        print(f"🤖 Bot response: {response_text}")
        
        twiml_response = MessagingResponse()
        twiml_response.message(response_text)
        return str(twiml_response), 200, {'Content-Type': 'text/xml'}
    
    return str(MessagingResponse())

if __name__ == '__main__':
    print("🚀 Starting Cloud Server...")
    app.run(host='0.0.0.0', port=5000, debug=True)