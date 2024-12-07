# Documentação da API

## Endpoints

### POST /chat
Processa mensagens do usuário e retorna respostas do assistente.

#### Request
```json
{
    "message": "string",
    "conversation_id": "string (opcional)",
    "context": {
        "additional_info": "any (opcional)"
    }
}
```

#### Response
```json
{
    "message": "string",
    "conversation_id": "string",
    "metadata": {
        "status": "string",
        "additional_info": "any"
    }
}
```

### GET /conversations/{conversation_id}
Retorna o histórico de uma conversa específica.

#### Response
```json
{
    "conversation_id": "string",
    "messages": [
        {
            "role": "string",
            "content": "string",
            "timestamp": "datetime"
        }
    ]
}
```

## Modelos de Dados

### Message
```python
class Message(BaseModel):
    role: str
    content: str
    timestamp: datetime
```

### Conversation
```python
class Conversation(BaseModel):
    id: str
    messages: List[Message]
    metadata: Dict[str, Any]
    created_at: datetime
    updated_at: datetime
```

### ChatRequest
```python
class ChatRequest(BaseModel):
    message: str
    conversation_id: Optional[str]
    context: Optional[Dict[str, Any]]
```

### ChatResponse
```python
class ChatResponse(BaseModel):
    message: str
    conversation_id: str
    metadata: Dict[str, Any]
```

