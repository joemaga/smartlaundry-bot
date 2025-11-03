import os
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route('/')
def home():
    return "🤖 SmartLaundry Cloud Server is Running!"

@app.route('/health')
def health():
    return "OK", 200

@app.route('/webhook/whatsapp', methods=['POST'])
def whatsapp_webhook():
    print("🔄 Webhook triggered!")

    incoming_msg = request.values.get('Body', '').strip()
    from_number = request.values.get('From', '')
    print(f"📱 From: {from_number} | Msg: {incoming_msg}")

    resp = MessagingResponse()
    resp.message(f"Echo: {incoming_msg if incoming_msg else 'I did not receive any text.'}")

    print(f"📤 Returning TwiML: {str(resp)}")
    return str(resp), 200, {'Content-Type': 'text/xml'}

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 10000))
    app.run(host='0.0.0.0', port=port, debug=True)

