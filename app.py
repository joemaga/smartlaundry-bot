import os
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from src.chatbot import BusinessChatbot

app = Flask(__name__)

@app.route('/')
def home():
    return "🤖 SmartLaundry Cloud Server is Running!"

@app.route('/health')
def health():
    return "OK", 200

@app.route('/test')
def test():
    chatbot = BusinessChatbot()
    response = chatbot.process_message("Olá, teste do servidor na nuvem!")
    return f"Chatbot test: {response}"

@app.route('/webhook/whatsapp', methods=['POST'])
def whatsapp_webhook():
    try:
        chatbot = BusinessChatbot()
        incoming_msg = request.values.get('Body', '').strip()
        from_number = request.values.get('From', '')
        
        print(f"📱 Message from {from_number}: {incoming_msg}")
        
        if not incoming_msg:
            return str(MessagingResponse()), 200, {'Content-Type': 'text/xml'}
        
        response_text = chatbot.process_message(incoming_msg)
        print(f"🤖 Bot response: {response_text}")
        
        twiml_response = MessagingResponse()
        twiml_response.message(response_text)
        return str(twiml_response), 200, {'Content-Type': 'text/xml'}
        
    except Exception as e:
        print(f"❌ Webhook error: {e}")
        twiml_response = MessagingResponse()
        twiml_response.message("Desculpe, ocorreu um erro.")
        return str(twiml_response), 200, {'Content-Type': 'text/xml'}

# Production server - this keeps the app running
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)