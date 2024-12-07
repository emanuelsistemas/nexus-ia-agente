#!/bin/bash

# Obtém a data e hora atual no formato brasileiro
DATA_HORA=$(date '+%d/%m/%Y %H:%M:%S')

# Adiciona todas as alterações
git add .

# Cria um commit temporário para obter o hash
TEMP_COMMIT=$(git commit -m "temp" --no-verify)

# Obtém o hash curto do commit temporário
HASH=$(git rev-parse --short HEAD)

# Faz o commit final com o hash na mensagem
git commit --amend -m "Commit automático - $DATA_HORA - Hash: $HASH" --no-verify

# Faz o push
git push origin HEAD --force
