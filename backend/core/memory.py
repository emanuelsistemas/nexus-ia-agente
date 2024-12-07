import chromadb
import os
from typing import List, Dict, Any
from datetime import datetime
import json

class Memory:
    def __init__(self):
        persist_dir = os.getenv("CHROMA_PERSISTENCE_DIR", "./database/chroma")
        self.client = chromadb.PersistentClient(path=persist_dir)
        
        # Criar ou obter coleção para conversas
        self.conversations = self.client.get_or_create_collection(
            name="conversations",
            metadata={"description": "Histórico de conversas do assistente"}
        )

    def save_conversation(self, conversation_id: str, messages: List[Dict[str, Any]], metadata: Dict[str, Any] = None):
        """Salva uma conversa no banco de dados"""
        # Preparar documentos para embeddings
        documents = [msg["content"] for msg in messages]
        ids = [f"{conversation_id}_{i}" for i in range(len(messages))]
        
        # Preparar metadados
        base_metadata = metadata or {}
        metadatas = [{
            "role": msg["role"],
            "timestamp": datetime.now().isoformat(),
            "conversation_id": conversation_id,
            **base_metadata
        } for msg in messages]

        # Salvar no ChromaDB
        self.conversations.add(
            documents=documents,
            ids=ids,
            metadatas=metadatas
        )

    def get_conversation(self, conversation_id: str, limit: int = 10) -> List[Dict[str, Any]]:
        """Recupera uma conversa do banco de dados"""
        results = self.conversations.query(
            query_texts=["*"],
            where={"conversation_id": conversation_id},
            n_results=limit
        )

        messages = []
        for i, doc in enumerate(results["documents"][0]):
            messages.append({
                "content": doc,
                "role": results["metadatas"][0][i]["role"],
                "timestamp": results["metadatas"][0][i]["timestamp"]
            })

        return messages

    def search_similar(self, query: str, limit: int = 5) -> List[Dict[str, Any]]:
        """Busca conversas similares baseadas em uma query"""
        results = self.conversations.query(
            query_texts=[query],
            n_results=limit
        )

        return [{
            "content": doc,
            "metadata": meta
        } for doc, meta in zip(results["documents"][0], results["metadatas"][0])]

memory = Memory()
