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
@app.route('/webhook/whatsapp', methods=['POST'])
def whatsapp_webhook():
    try:
        incoming_msg = request.values.get('Body', '').strip()
        from_number = request.values.get('From', '')
        
        print(f"📱 Message from {from_number}: {incoming_msg}")
        
        if not incoming_msg:
            print("❌ Empty message received")
            return str(MessagingResponse()), 200, {'Content-Type': 'text/xml'}
        
        # Process the message
        response_text = chatbot.process_message(incoming_msg)
        print(f"🤖 Bot response: {response_text}")
        
        # Create Twilio response
        twiml_response = MessagingResponse()
        twiml_response.message(response_text)
        
        print(f"📤 Sending TwiML response: {str(twiml_response)}")
        return str(twiml_response), 200, {'Content-Type': 'text/xml'}
        
    except Exception as e:
        print(f"❌ Webhook error: {e}")
        # Return a basic response even on error
        twiml_response = MessagingResponse()
        twiml_response.message("Desculpe, ocorreu um erro. Tente novamente.")
        return str(twiml_response), 200, {'Content-Type': 'text/xml'}