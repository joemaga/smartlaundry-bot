import os
from flask import Flask
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

if __name__ == '__main__':
    print("🚀 Starting Cloud Server...")
    app.run(host='0.0.0.0', port=5000, debug=True)