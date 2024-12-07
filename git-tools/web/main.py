from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
import subprocess
import os
from datetime import datetime
import pytz

app = FastAPI()

# Monta os arquivos estáticos
app.mount("/static", StaticFiles(directory="static"), name="static")

# Diretório do projeto
PROJECT_DIR = "/root/project/nexus/nexus-ia/v1"
COMMIT_HISTORY_FILE = os.path.join(PROJECT_DIR, "git-tools/commit_history.txt")
RESTORE_SCRIPT = os.path.join(PROJECT_DIR, "git-tools/restore_point.sh")

def parse_commit_line(line):
    """Parseia uma linha do arquivo de histórico de commits."""
    try:
        # Formato: [07/12/2024 10:09:00] Commit: 3532465 - Para restaurar use: git reset --hard 3532465
        parts = line.strip().split("]")
        date_str = parts[0].strip("[")
        
        commit_info = parts[1].split("Commit:")[1]
        hash_part = commit_info.split("-")[0].strip()
        
        # Converte a data para objeto datetime
        date_obj = datetime.strptime(date_str, "%d/%m/%Y %H:%M:%S")
        # Adiciona o timezone de São Paulo
        sp_tz = pytz.timezone("America/Sao_Paulo")
        date_obj = sp_tz.localize(date_obj)
        
        return {
            "date": date_obj.strftime("%d/%m/%Y %H:%M:%S"),
            "hash": hash_part,
            "full_line": line.strip()
        }
    except Exception as e:
        print(f"Erro ao parsear linha: {line}")
        print(f"Erro: {str(e)}")
        return None

@app.get("/")
async def read_root():
    """Retorna a página principal."""
    return FileResponse("static/index.html")

@app.get("/api/commits")
async def get_commits():
    """Retorna a lista de commits do histórico."""
    try:
        with open(COMMIT_HISTORY_FILE, "r") as f:
            lines = f.readlines()
            
        commits = []
        for line in lines:
            commit = parse_commit_line(line)
            if commit:
                commits.append(commit)
        
        return {"commits": commits}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/api/restore/{commit_hash}")
async def restore_commit(commit_hash: str):
    """Restaura o projeto para um commit específico."""
    try:
        # Executa o script de restauração
        result = subprocess.run(
            [RESTORE_SCRIPT, commit_hash],
            capture_output=True,
            text=True
        )
        
        if result.returncode != 0:
            raise HTTPException(
                status_code=500,
                detail=f"Erro ao restaurar: {result.stderr}"
            )
        
        return {
            "message": "Restauração concluída com sucesso",
            "details": result.stdout
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
