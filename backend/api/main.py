from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import sys
import os

# Adicionar o diretório raiz ao PYTHONPATH
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

from backend.models.base import ChatRequest, ChatResponse
from backend.core.assistant import assistant
from backend.core.memory import memory
import uuid
from typing import List, Dict, Any

app = FastAPI(title="Nexus IA")

# Configurar CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    try:
        # Gerar ou usar ID da conversa existente
        conversation_id = request.conversation_id or str(uuid.uuid4())

        # Obter resposta do assistente
        response = await assistant.chat(
            message=request.message,
            conversation_id=conversation_id,
            context=request.context
        )

        # Salvar conversa na memória
        memory.save_conversation(
            conversation_id=conversation_id,
            messages=[
                {"role": "user", "content": request.message},
                {"role": "assistant", "content": response}
            ],
            metadata=request.context or {}
        )

        return ChatResponse(
            message=response,
            conversation_id=conversation_id,
            metadata={"status": "success"}
        )

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/conversations/{conversation_id}")
async def get_conversation(conversation_id: str):
    try:
        messages = memory.get_conversation(conversation_id)
        return {"conversation_id": conversation_id, "messages": messages}
    except Exception as e:
        raise HTTPException(status_code=404, detail=f"Conversa não encontrada: {str(e)}")

@app.get("/search")
async def search_conversations(query: str, limit: int = 5):
    try:
        results = memory.search_similar(query, limit)
        return {"results": results}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
