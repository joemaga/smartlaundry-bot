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

@app.route('/webhook/whatsapp', methods=['POST'])
def whatsapp_webhook():
    try:
        print("🔄 Webhook triggered!")
        
        chatbot = BusinessChatbot()
        incoming_msg = request.values.get('Body', '').strip()
        from_number = request.values.get('From', '')
        
        print(f"📱 Message from {from_number}: '{incoming_msg}'")
        print(f"📊 All form data: {dict(request.values)}")
        
        if not incoming_msg:
            print("❌ Empty message received")
            empty_response = str(MessagingResponse())
            print(f"📤 Sending empty response: {empty_response}")
            return empty_response, 200, {'Content-Type': 'text/xml'}
        
        response_text = chatbot.process_message(incoming_msg)
        print(f"🤖 Bot response: '{response_text}'")
        
        twiml_response = MessagingResponse()
        twiml_response.message(response_text)
        final_response = str(twiml_response)
        
        print(f"📤 Sending TwiML response: {final_response}")
        return final_response, 200, {'Content-Type': 'text/xml'}
        
    except Exception as e:
        print(f"❌ Webhook error: {e}")
        import traceback
        print(f"🔍 Full traceback: {traceback.format_exc()}")
        
        twiml_response = MessagingResponse()
        twiml_response.message("Desculpe, ocorreu um erro.")
        return str(twiml_response), 200, {'Content-Type': 'text/xml'}

# Use the port Render provides
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 10000))
    app.run(host='0.0.0.0', port=port, debug=False)