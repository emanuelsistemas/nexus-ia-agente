# Aliases para comandos Git
alias ac='/root/project/nexus/nexus-ia/v1/git-tools/auto_commit.sh'

# Carrega as funções do script git_commands.sh
source /root/project/nexus/nexus-ia/v1/git-tools/git_commands.sh

# Restauração completa para um commit específico
alias restore='/root/project/nexus/nexus-ia/v1/git-tools/restore_point.sh'

# Git status
alias gs='git status'

# Git log formatado
alias gl='git log --graph --pretty=format:"%Cred%h%Creset -%C(yellow)%d%Creset %s %Cgreen(%cr) %C(bold blue)<%an>%Creset" --abbrev-commit'

# Git branch
alias gb='git branch'

# Git checkout com parâmetro
alias gch='git checkout'

# Criar e mudar para nova branch
alias gcb='git checkout -b'

# Git diff
alias gd='git diff'

# Reverter para commit específico
alias grh='revert_to_commit'

# Reset soft para commit específico
alias grs='soft_reset_to_commit'

# Reverter último commit
alias grh-last='git reset --hard HEAD~1'

# Limpar arquivos não rastreados
alias gclean='clean_untracked'

# Desfazer último commit mantendo alterações
alias gundo='undo_last_commit'

# Ajuda
alias ghelp='show_help'
