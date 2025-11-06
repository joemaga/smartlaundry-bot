import os
from flask import Flask, request, make_response
from twilio.twiml.messaging_response import MessagingResponse
from src.chatbot import BusinessChatbot

app = Flask(__name__)
VERIFY_TOKEN = os.getenv('VERIFY_TOKEN')

@app.route('/')
def home():
    return "🤖 SmartLaundry Cloud Server is Running!"

@app.route('/health')
def health():
    return "OK", 200

@app.route('/webhook', methods=['GET', 'POST'])
def webhook():
    # Handle verification (GET request from Meta)
    if request.method == 'GET':
        mode = request.args.get('hub.mode')
        token = request.args.get('hub.verify_token')
        challenge = request.args.get('hub.challenge')

        if mode == 'subscribe' and token == VERIFY_TOKEN:
            print("✅ Webhook verified successfully!")
            # Return the challenge value directly, not as JSON
            return challenge, 200
        else:
            print("❌ Webhook verification failed!")
            return 'Verification failed', 403

    # Handle incoming WhatsApp messages (POST request from Meta)
    elif request.method == 'POST':
        print("📨 Received a WhatsApp message from Meta!")
        return make_response('EVENT_RECEIVED', 200)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 10000))
    print(f"🚀 Starting Flask app on port {port}")
    app.run(host='0.0.0.0', port=port, debug=False)