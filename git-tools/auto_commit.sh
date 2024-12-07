#!/bin/bash

# Obtém a data e hora atual no formato brasileiro
DATA_HORA=$(date '+%d/%m/%Y %H:%M:%S')

# Adiciona todas as alterações
git add .

# Faz o commit
git commit -m "Commit automático - $DATA_HORA"

# Obtém o hash do último commit
HASH=$(git rev-parse HEAD)

# Atualiza a mensagem do commit com o hash
git commit --amend -m "Commit automático - $DATA_HORA - Hash: $HASH"

# Faz o push
git push origin HEAD --force
