# Aliases para comandos Git
alias ac='/root/project/nexus/nexus-ia/v1/git-tools/auto_commit.sh'

# Carrega as funções do script git_commands.sh
source /root/project/nexus/nexus-ia/v1/git-tools/git_commands.sh

# Restauração completa para um commit específico
alias restore='/root/project/nexus/nexus-ia/v1/git-tools/restore_point.sh'

# Interface gráfica do Git
alias ggui='python3 /root/project/nexus/nexus-ia/v1/git-tools/git_gui.py'

# Git status
alias gs='git_status'

# Git log formatado
alias gl='git_log'

# Git branch
alias gb='git_branch'

# Git checkout com parâmetro
alias gch='git_checkout'

# Criar e mudar para nova branch
alias gcb='git_checkout_new'

# Git diff
alias gd='git_diff'

# Reverter para commit específico
alias grh='revert_to_commit'

# Reset soft para commit específico
alias grs='soft_reset_to_commit'

# Reverter último commit
alias grh-last='revert_last_commit'

# Limpar arquivos não rastreados
alias gclean='clean_untracked'

# Desfazer último commit mantendo alterações
alias gundo='undo_last_commit'

# Ajuda
alias ghelp='show_help'
