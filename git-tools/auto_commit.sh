#!/bin/bash

# Obtém a data e hora atual no formato brasileiro
DATA_HORA=$(date '+%d/%m/%Y %H:%M:%S')

# Adiciona todas as alterações
git add .

# Faz o commit com a data/hora
git commit -m "Commit automático - $DATA_HORA" --no-verify

# Obtém o hash do commit que acabamos de criar
HASH=$(git rev-parse --short HEAD)

# Adiciona o registro no arquivo de histórico
echo "[$DATA_HORA] Commit: $HASH - Para restaurar use: git reset --hard $HASH" >> ./commit_history.txt

# Faz o push
git push origin HEAD

# Exibe a mensagem de confirmação
echo "Commit realizado com sucesso!"
echo "Hash para restauração: $HASH"
echo "Este hash foi salvo em ./commit_history.txt"
