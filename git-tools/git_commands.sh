#!/bin/bash

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
    if [ -z "$1" ]; then
        echo "Por favor, forneça o hash do commit"
        return 1
    fi
    git reset --hard $1
    echo "Revertido para o commit $1"
}

# Função para reset soft (mantém alterações no working directory)
soft_reset_to_commit() {
    if [ -z "$1" ]; then
        echo "Por favor, forneça o hash do commit"
        return 1
    fi
    git reset --soft $1
    echo "Reset soft realizado para o commit $1"
}

# Função para limpar arquivos não rastreados
clean_untracked() {
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
    git reset --soft HEAD~1
    echo "Último commit desfeito. Alterações mantidas no working directory"
}
