import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
    COMPANY_NAME = os.getenv('COMPANY_NAME', 'SmartLaundry Alphaville')
    TWILIO_ACCOUNT_SID = os.getenv('TWILIO_ACCOUNT_SID')
    TWILIO_AUTH_TOKEN = os.getenv('TWILIO_AUTH_TOKEN')
    TWILIO_WHATSAPP_NUMBER = os.getenv('TWILIO_WHATSAPP_NUMBER')
    
    DEFAULT_PARAMETERS = {
        "response_tone": "amigável e profissional", 
        "max_response_length": 300,
        "language": "português brasileiro"
    }