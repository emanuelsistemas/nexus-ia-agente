from pydantic import BaseModel, Field
from typing import Optional, List, Dict, Any
from datetime import datetime

class Message(BaseModel):
    role: str = Field(..., description="Papel do remetente (user/assistant)")
    content: str = Field(..., description="Conteúdo da mensagem")
    timestamp: datetime = Field(default_factory=datetime.now)

class Conversation(BaseModel):
    id: str = Field(..., description="ID único da conversa")
    messages: List[Message] = Field(default_factory=list)
    metadata: Dict[str, Any] = Field(default_factory=dict)
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(default_factory=datetime.now)

class ChatRequest(BaseModel):
    message: str = Field(..., description="Mensagem do usuário")
    conversation_id: Optional[str] = Field(None, description="ID da conversa existente")
    context: Optional[Dict[str, Any]] = Field(None, description="Contexto adicional")

class ChatResponse(BaseModel):
    message: str = Field(..., description="Resposta do assistente")
    conversation_id: str = Field(..., description="ID da conversa")
    metadata: Dict[str, Any] = Field(default_factory=dict)
