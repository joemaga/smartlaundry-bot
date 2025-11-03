import openai
from typing import Dict, List, Any
from .config import Config

class BusinessChatbot:
    def __init__(self, company_parameters: Dict[str, Any] = None):
        self.client = openai.OpenAI(api_key=Config.OPENAI_API_KEY)
        self.company_params = company_parameters or Config.DEFAULT_PARAMETERS
        
    def _build_system_prompt(self) -> str:
        return f"""
        Você é um assistente da {Config.COMPANY_NAME}.
        Seja {self.company_params.get('response_tone')}.
        Limite de resposta: {self.company_params.get('max_response_length')} caracteres.
        """
    
    def process_message(self, user_message: str) -> str:
        messages = [
            {"role": "system", "content": self._build_system_prompt()},
            {"role": "user", "content": user_message}
        ]
        
        try:
            response = self.client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=messages,
                max_tokens=300
            )
            return response.choices[0].message.content.strip()
        except Exception as e:
            return "Desculpe, estou com problemas técnicos."