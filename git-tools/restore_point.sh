#!/bin/bash

# Função para exibir mensagens de status
print_status() {
    echo "----------------------------------------"
    echo "$1"
    echo "----------------------------------------"
}

# Função para restaurar para um commit específico
restore_to_commit() {
    if [ -z "$1" ]; then
        echo "Por favor, forneça o hash do commit"
        return 1
    fi
    
    HASH=$1
    print_status "Iniciando restauração para o commit: $HASH"
    
    # 1. Parar serviços em execução
    print_status "Parando serviços..."
    pkill -f "uvicorn main:app"
    
    # 2. Backup do .env atual
    if [ -f ../.env ]; then
        print_status "Fazendo backup do .env..."
        cp ../.env ../.env.backup
    fi
    
    # 3. Reverter código para o commit específico
    print_status "Revertendo código..."
    git -C .. reset --hard $HASH
    
    # 4. Backup do banco de dados atual
    if [ -d ../database ]; then
        print_status "Fazendo backup do banco de dados..."
        timestamp=$(date +%Y%m%d_%H%M%S)
        mkdir -p ../database_backups
        cp -r ../database ../database_backups/database_$timestamp
    fi
    
    # 5. Recriar ambiente virtual com as dependências corretas
    print_status "Recriando ambiente virtual..."
    cd ..
    rm -rf venv
    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    
    # 6. Limpar cache e arquivos temporários
    print_status "Limpando cache..."
    find . -type d -name "__pycache__" -exec rm -r {} +
    rm -rf .pytest_cache
    
    # 7. Reiniciar serviços
    print_status "Reiniciando serviços..."
    nohup uvicorn main:app --host 0.0.0.0 --port 8000 > server.log 2>&1 &
    
    print_status "Restauração completa!"
    echo "Serviços reiniciados na porta 8000"
    echo "Logs disponíveis em: server.log"
    echo "Backup do .env salvo em: .env.backup"
    echo "Backup do banco de dados salvo em: database_backups/database_$timestamp"
}

# Se o script for chamado diretamente
if [[ "${BASH_SOURCE[0]}" == "${0}" ]]; then
    restore_to_commit "$1"
fi
