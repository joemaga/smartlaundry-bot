import os
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

# Basic homepage route
@app.route('/')
def home():
    return "🤖 SmartLaundry Cloud Server is Running!"

# Health check (Render uses this sometimes)
@app.route('/health')
def health():
    return "OK", 200

# WhatsApp webhook endpoint
@app.route('/webhook/whatsapp', methods=['POST'])
def whatsapp_webhook():
    print("🔄 Webhook triggered!")

    # Grab the incoming WhatsApp message
    incoming_msg = request.values.get('Body', '_
