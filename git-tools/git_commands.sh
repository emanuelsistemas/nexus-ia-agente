#!/bin/bash

# Define o diretório do projeto
PROJECT_DIR="/root/project/nexus/nexus-ia/v1"

# Função para ir para o diretório do projeto
goto_project() {
    cd $PROJECT_DIR || {
        echo "Erro: Não foi possível acessar o diretório do projeto: $PROJECT_DIR"
        return 1
    }
}

# Função para mostrar o menu de ajuda
show_help() {
    echo "Comandos Git disponíveis:"
    echo "ac              - Auto commit com data/hora e hash"
    echo "gl              - Git log formatado e colorido"
    echo "gs              - Git status"
    echo "gb              - Lista branches"
    echo "gch <branch>    - Muda para a branch especificada"
    echo "gcb <nome>      - Cria e muda para nova branch"
    echo "gd              - Git diff"
    echo "grh <hash>      - Reverte para o commit específico"
    echo "grs <hash>      - Reseta soft para o commit (mantém alterações)"
    echo "grh-last        - Reverte último commit"
    echo "gclean         - Remove arquivos não rastreados"
    echo "gundo          - Desfaz último commit mantendo alterações"
    echo "help           - Mostra esta ajuda"
}

# Função para reverter para um commit específico
revert_to_commit() {
    goto_project
    if [ -z "$1" ]; then
        echo "Por favor, forneça o hash do commit"
        return 1
    fi
    git reset --hard $1
    echo "Revertido para o commit $1"
}

# Função para reset soft (mantém alterações no working directory)
soft_reset_to_commit() {
    goto_project
    if [ -z "$1" ]; then
        echo "Por favor, forneça o hash do commit"
        return 1
    fi
    git reset --soft $1
    echo "Reset soft realizado para o commit $1"
}

# Função para limpar arquivos não rastreados
clean_untracked() {
    goto_project
    read -p "Isso removerá todos os arquivos não rastreados. Continuar? (s/N) " response
    if [[ "$response" =~ ^([sS][iI][mM]|[sS])$ ]]; then
        git clean -fd
        echo "Arquivos não rastreados foram removidos"
    else
        echo "Operação cancelada"
    fi
}

# Função para desfazer último commit mantendo alterações
undo_last_commit() {
    goto_project
    git reset --soft HEAD~1
    echo "Último commit desfeito. Alterações mantidas no working directory"
}

# Git status
git_status() {
    goto_project
    git status
}

# Git log formatado
git_log() {
    goto_project
    git log --graph --pretty=format:"%Cred%h%Creset -%C(yellow)%d%Creset %s %Cgreen(%cr) %C(bold blue)<%an>%Creset" --abbrev-commit
}

# Git branch
git_branch() {
    goto_project
    git branch
}

# Git checkout
git_checkout() {
    goto_project
    if [ -z "$1" ]; then
        echo "Erro: Forneça o nome da branch"
        echo "Uso: gch <branch>"
        return 1
    fi
    git checkout "$1"
}

# Criar e mudar para nova branch
git_checkout_new() {
    goto_project
    if [ -z "$1" ]; then
        echo "Erro: Forneça o nome da nova branch"
        echo "Uso: gcb <nova-branch>"
        return 1
    fi
    git checkout -b "$1"
}

# Git diff
git_diff() {
    goto_project
    git diff
}

# Reverter para commit específico
revert_to_commit() {
    goto_project
    if [ -z "$1" ]; then
        echo "Erro: Forneça o hash do commit"
        echo "Uso: grh <hash>"
        return 1
    fi
    git reset --hard "$1"
}

# Reset soft para commit específico
soft_reset_to_commit() {
    goto_project
    if [ -z "$1" ]; then
        echo "Erro: Forneça o hash do commit"
        echo "Uso: grs <hash>"
        return 1
    fi
    git reset --soft "$1"
}

# Reverter último commit
revert_last_commit() {
    goto_project
    git reset --hard HEAD~1
}

# Limpar arquivos não rastreados
clean_untracked() {
    goto_project
    echo "Isso vai remover todos os arquivos não rastreados!"
    echo "Tem certeza? [s/N]"
    read -r response
    if [[ "$response" =~ ^([sS][iI]|[sS])$ ]]; then
        git clean -fd
    fi
}

# Desfazer último commit mantendo alterações
undo_last_commit() {
    goto_project
    git reset --soft HEAD~1
}
