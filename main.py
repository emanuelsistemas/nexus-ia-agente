from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from backend.models.base import ChatRequest, ChatResponse
from backend.core.assistant import assistant
from backend.core.memory import memory
import uvicorn
import uuid
from typing import List, Dict, Any
from dotenv import load_dotenv
import os

load_dotenv()

app = FastAPI(title="Nexus IA")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "Nexus IA API"}

@app.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    try:
        conversation_id = request.conversation_id or str(uuid.uuid4())
        response = await assistant.chat(
            message=request.message,
            conversation_id=conversation_id,
            context=request.context
        )

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
        print(f"Erro no chat: {str(e)}")
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
    uvicorn.run(
        "main:app",
        host=os.getenv("HOST", "0.0.0.0"),
        port=int(os.getenv("PORT", 8000)),
        reload=True
    )
