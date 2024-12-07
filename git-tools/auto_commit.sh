#!/bin/bash

# Define o diretório do projeto
PROJECT_DIR="/root/project/nexus/nexus-ia/v1"

# Vai para o diretório do projeto
cd $PROJECT_DIR || {
    echo "Erro: Não foi possível acessar o diretório do projeto: $PROJECT_DIR"
    exit 1
}

# Configura o timezone para São Paulo
export TZ="America/Sao_Paulo"

# Obtém a data e hora atual no formato brasileiro
DATA_HORA=$(date '+%d/%m/%Y %H:%M:%S')

# Adiciona todas as alterações
git add .

# Faz o commit com a data/hora
git commit -m "Commit automático - $DATA_HORA" --no-verify

# Obtém o hash do commit que acabamos de criar
HASH=$(git rev-parse --short HEAD)

# Adiciona o registro no arquivo de histórico
TEMP_FILE=$(mktemp)
echo "[$DATA_HORA] Commit: $HASH - Para restaurar use: git reset --hard $HASH" > "$TEMP_FILE"
if [ -f ./git-tools/commit_history.txt ]; then
    cat ./git-tools/commit_history.txt >> "$TEMP_FILE"
fi
mv "$TEMP_FILE" ./git-tools/commit_history.txt

# Adiciona o arquivo de histórico ao commit se foi modificado
git add ./git-tools/commit_history.txt
git commit --amend -m "Commit automático - $DATA_HORA" --no-verify

# Faz o push
git push origin HEAD --force

# Exibe a mensagem de confirmação
echo "Commit realizado com sucesso!"
echo "Hash para restauração: $HASH"
echo "Histórico completo salvo em ./git-tools/commit_history.txt"
echo "----------------------------------------"
echo "Últimos 5 commits do histórico:"
head -n 5 ./git-tools/commit_history.txt
