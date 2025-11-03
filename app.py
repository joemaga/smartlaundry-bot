import os
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from src.chatbot import BusinessChatbot

# Create Flask app instance
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
        print("🔄 WEBHOOK TRIGGERED - THIS SHOULD APPEAR IN LOGS!")
        
        chatbot = BusinessChatbot()
        incoming_msg = request.values.get('Body', '').strip()
        from_number = request.values.get('From', '')
        
        print(f"📱 Message from {from_number}: '{incoming_msg}'")
        
        if not incoming_msg:
            print("❌ Empty message received")
            return str(MessagingResponse()), 200, {'Content-Type': 'text/xml'}
        
        response_text = chatbot.process_message(incoming_msg)
        print(f"🤖 Bot response: '{response_text}'")
        
        twiml_response = MessagingResponse()
        twiml_response.message(response_text)
        final_response = str(twiml_response)
        
        print(f"📤 Sending TwiML: {final_response}")
        return final_response, 200, {'Content-Type': 'text/xml'}
        
    except Exception as e:
        print(f"❌ ERROR: {e}")
        import traceback
        traceback.print_exc()
        
        twiml_response = MessagingResponse()
        twiml_response.message("Desculpe, ocorreu um erro.")
        return str(twiml_response), 200, {'Content-Type': 'text/xml'}

# Only run if this is the main module
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 10000))
    print(f"🚀 Starting Flask app on port {port}")
    app.run(host='0.0.0.0', port=port, debug=False)