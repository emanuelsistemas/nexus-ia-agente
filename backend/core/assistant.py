from anthropic import Anthropic
from typing import Optional, Dict, Any
import os
from dotenv import load_dotenv

load_dotenv()

class Assistant:
    def __init__(self):
        self.client = Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))
        self.system_prompt = """
Você é um assistente especializado em desenvolvimento de software que:
- Se comunica em português brasileiro
- Guia o usuário de forma amigável e profissional
- Sugere boas práticas de desenvolvimento
- Mantém contexto das conversas anteriores
- Pode sugerir melhorias e correções
- Explica conceitos técnicos de forma clara
"""

    async def chat(self, message: str, conversation_id: Optional[str] = None, context: Optional[Dict[str, Any]] = None) -> str:
        try:
            response = await self.client.messages.create(
                model="claude-3-opus-20240229",
                max_tokens=4096,
                temperature=0.7,
                system=self.system_prompt,
                messages=[{"role": "user", "content": message}]
            )
            return response.content[0].text
        except Exception as e:
            print(f"Erro ao chamar Claude API: {str(e)}")
            raise

    def update_system_prompt(self, new_prompt: str):
        """Atualiza o prompt do sistema"""
        self.system_prompt = new_prompt

assistant = Assistant()
