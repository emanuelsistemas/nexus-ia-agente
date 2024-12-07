#!/bin/bash

# Obtém a data e hora atual no formato brasileiro
DATA_HORA=$(date '+%d/%m/%Y %H:%M:%S')

# Adiciona todas as alterações
git add .

# Faz o commit inicial
git commit -m "Commit automático - $DATA_HORA"

# Obtém o hash curto do commit que acabamos de criar
HASH=$(git rev-parse --short HEAD)

# Atualiza a mensagem do commit com o hash curto
git commit --amend -m "Commit automático - $DATA_HORA - Hash: $HASH" --no-verify

# Faz o push
git push origin HEAD --force
