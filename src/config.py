import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
    COMPANY_NAME = os.getenv('COMPANY_NAME', 'SmartLaundry Alphaville')
    
    DEFAULT_PARAMETERS = {
        "response_tone": "amigável e profissional",
        "max_response_length": 300,
        "language": "português brasileiro"
    }