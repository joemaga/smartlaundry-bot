import os
from flask import Flask, request, Response
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

# Home page
@app.route('/')
def home():
    return "🤖 SmartLaundry Cloud Server is Running!"

# Health check (optional for Render)
@app.route('/health')
def health():
    return "OK", 200

# WhatsApp webhook endpoint
@app.route('/webhook/whatsapp', methods=['POST'])
def whatsapp_webhook():
    try:
        print("🔄 Webhook triggered!")

        # Grab incoming WhatsApp message
        incoming_msg = request.values.get('Body', '').strip()
        from_number = request.values.get('From', '')
        print(f"📱 From: {from_number} | Msg: {incoming_msg}")

        # Create Twilio MessagingResponse
        resp = MessagingResponse()

        # Temporary echo bot for testing
        resp.message(f"Echo: {incoming_msg if incoming_msg else 'I did not receive any text.'}")

        # Log the TwiML XML
        twiml_xml = str(resp)
        print(f"📤 Returning TwiML: {twiml_xml}")

        # Return TwiML using Flask Response with correct content-type
        return Response(twiml_xml, mimetype='text/xml')

    except Exception as e:
        print(f"❌ Webhook error: {e}")
        import traceback
        print(f"🔍 Full traceback: {traceback.format_exc()}")

        # Return a friendly error message to WhatsApp
        resp = MessagingResponse()
        resp.message("⚠️ Sorry, something went wrong.")
        return Response(str(resp), mimetype='text/xml')


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 10000))
    app.run(host='0.0.0.0', port=port, debug=True)
