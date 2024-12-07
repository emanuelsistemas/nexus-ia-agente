#!/bin/bash

# Obtém a data e hora atual no formato brasileiro
DATA_HORA=$(date '+%d/%m/%Y %H:%M:%S')

# Adiciona todas as alterações
git add .

# Faz o commit com a data/hora
git commit -m "Commit automático - $DATA_HORA" --no-verify

# Faz o push
git push origin HEAD
