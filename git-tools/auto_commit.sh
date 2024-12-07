#!/bin/bash

# Obtém a data e hora atual no formato brasileiro
DATA_HORA=$(date '+%d/%m/%Y %H:%M:%S')

# Adiciona todas as alterações
git add .

# Gera um hash único para o commit (baseado no timestamp e conteúdo)
TEMP_HASH=$(echo "$DATA_HORA $(git write-tree)" | git hash-object --stdin)

# Faz o commit com o hash já incluído
git commit -m "Commit automático - $DATA_HORA - Hash: $TEMP_HASH"

# Faz o push
git push origin HEAD
