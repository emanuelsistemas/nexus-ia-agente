#!/usr/bin/env python3
import os
import subprocess
from datetime import datetime

class GitRestoreTUI:
    def __init__(self):
        self.project_dir = "/root/project/nexus/nexus-ia/v1"
        self.history_file = os.path.join(self.project_dir, "git-tools/commit_history.txt")
        self.restore_script = os.path.join(self.project_dir, "git-tools/restore_point.sh")
        
    def clear_screen(self):
        os.system('clear')
        
    def print_header(self):
        print("=" * 80)
        print("Git Restore - Gerenciador de Commits".center(80))
        print("=" * 80)
        print()
        
    def load_commits(self):
        commits = []
        try:
            with open(self.history_file, 'r') as f:
                lines = f.readlines()
                
            for line in lines:
                try:
                    # Parse da linha do commit
                    parts = line.strip().split(']')
                    date_str = parts[0].strip('[')
                    commit_info = parts[1].split('Commit:')[1]
                    hash_part = commit_info.split('-')[0].strip()
                    
                    commits.append({
                        'date': date_str,
                        'hash': hash_part,
                        'full_line': line.strip()
                    })
                except Exception as e:
                    print(f"Erro ao processar commit: {e}")
                    
        except Exception as e:
            print(f"Erro ao carregar commits: {str(e)}")
            
        return commits
    
    def print_commits(self, commits):
        print("\nHistórico de Commits:")
        print("-" * 80)
        print(f"{'Índice':<8} {'Data/Hora':<20} {'Hash':<10}")
        print("-" * 80)
        
        for i, commit in enumerate(commits, 1):
            print(f"{i:<8} {commit['date']:<20} {commit['hash']:<10}")
            
        print("-" * 80)
        
    def restore_commit(self, commit_hash):
        try:
            # Executar script de restauração
            print(f"\nRestaurando para o commit {commit_hash}...")
            result = subprocess.run(
                [self.restore_script, commit_hash],
                capture_output=True,
                text=True
            )
            
            if result.returncode == 0:
                print("\nRestauração concluída com sucesso!")
            else:
                print(f"\nErro na restauração: {result.stderr}")
                
        except Exception as e:
            print(f"\nErro ao restaurar: {str(e)}")
    
    def main_menu(self):
        while True:
            self.clear_screen()
            self.print_header()
            
            commits = self.load_commits()
            self.print_commits(commits)
            
            print("\nOpções:")
            print("1. Restaurar commit")
            print("2. Atualizar lista")
            print("3. Sair")
            
            choice = input("\nEscolha uma opção (1-3): ").strip()
            
            if choice == '1':
                index = input("\nDigite o número do commit que deseja restaurar: ").strip()
                try:
                    index = int(index) - 1
                    if 0 <= index < len(commits):
                        commit = commits[index]
                        confirm = input(f"\nConfirma a restauração para o commit {commit['hash']}? (s/N): ").strip().lower()
                        if confirm == 's':
                            self.restore_commit(commit['hash'])
                            input("\nPressione ENTER para continuar...")
                    else:
                        print("\nÍndice inválido!")
                        input("\nPressione ENTER para continuar...")
                except ValueError:
                    print("\nPor favor, digite um número válido!")
                    input("\nPressione ENTER para continuar...")
                    
            elif choice == '2':
                continue
                
            elif choice == '3':
                print("\nSaindo...")
                break
                
            else:
                print("\nOpção inválida!")
                input("\nPressione ENTER para continuar...")

def main():
    app = GitRestoreTUI()
    app.main_menu()

if __name__ == "__main__":
    main()
