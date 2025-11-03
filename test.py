import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from src.chatbot import BusinessChatbot

def main():
    print("🤖 Testing basic chatbot...")
    chatbot = BusinessChatbot()
    
    # Test without API key first
    test_message = "Olá, como vai?"
    print(f"User: {test_message}")
    
    try:
        response = chatbot.process_message(test_message)
        print(f"Bot: {response}")
    except Exception as e:
        print(f"Error (expected without API key): {e}")

if __name__ == "__main__":
    main()