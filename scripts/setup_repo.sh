#!/bin/bash

# Verifica se recebeu a URL do repositório como argumento
if [ -z "$1" ]; then
    echo "Por favor, forneça a URL do repositório GitHub."
    echo "Uso: ./setup_repo.sh <url_do_repositorio>"
    exit 1
fi

REPO_URL=$1

# Inicializa o repositório Git
git init

# Adiciona o repositório remoto
git remote add origin $REPO_URL

# Cria um arquivo README inicial
echo "# Git Automation Scripts" > README.md
echo "Scripts para automatização de commits e pushes" >> README.md
echo "Criado em: $(date '+%d/%m/%Y %H:%M:%S')" >> README.md

# Configura o branch principal como 'main'
git branch -M main

# Adiciona os arquivos
git add .

# Faz o commit inicial
git commit -m "Commit inicial - $(date '+%d/%m/%Y %H:%M:%S')"

# Faz o push inicial
git push -u origin main

echo "Configuração concluída!"
