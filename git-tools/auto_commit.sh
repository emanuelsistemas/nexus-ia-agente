#!/bin/bash

# Obtém a data e hora atual no formato brasileiro
DATA_HORA=$(date '+%d/%m/%Y %H:%M:%S')

# Adiciona todas as alterações
git add .

# Faz o commit com a data/hora
git commit -m "Commit automático - $DATA_HORA" --no-verify

# Obtém o hash do commit que acabamos de criar
HASH=$(git rev-parse --short HEAD)

# Adiciona o registro no início do arquivo de histórico
TEMP_FILE=$(mktemp)
echo "[$DATA_HORA] Commit: $HASH - Para restaurar use: git reset --hard $HASH" > "$TEMP_FILE"
if [ -f ./commit_history.txt ]; then
    cat ./commit_history.txt >> "$TEMP_FILE"
fi
mv "$TEMP_FILE" ./commit_history.txt

# Adiciona o arquivo de histórico ao commit se foi modificado
git add ./commit_history.txt
git commit --amend -m "Commit automático - $DATA_HORA" --no-verify

# Faz o push
git push origin HEAD --force

# Exibe a mensagem de confirmação
echo "Commit realizado com sucesso!"
echo "Hash para restauração: $HASH"
echo "Histórico completo salvo em ./commit_history.txt"
echo "----------------------------------------"
echo "Últimos 5 commits do histórico:"
head -n 5 ./commit_history.txt
