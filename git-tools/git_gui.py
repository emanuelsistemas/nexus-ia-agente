import tkinter as tk
from tkinter import ttk, messagebox
import subprocess
import os
from datetime import datetime

class GitRestoreGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Git Restore GUI")
        
        # Configuração da janela principal
        self.root.geometry("800x600")
        
        # Diretório do projeto
        self.project_dir = "/root/project/nexus/nexus-ia/v1"
        self.history_file = os.path.join(self.project_dir, "git-tools/commit_history.txt")
        self.restore_script = os.path.join(self.project_dir, "git-tools/restore_point.sh")
        
        # Frame principal
        main_frame = ttk.Frame(root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Título
        title_label = ttk.Label(main_frame, text="Histórico de Commits", font=('Helvetica', 16, 'bold'))
        title_label.grid(row=0, column=0, columnspan=2, pady=10)
        
        # Criar Treeview para listar commits
        self.tree = ttk.Treeview(main_frame, columns=('Data', 'Hash', 'Ações'), show='headings')
        self.tree.grid(row=1, column=0, columnspan=2, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Configurar colunas
        self.tree.heading('Data', text='Data/Hora')
        self.tree.heading('Hash', text='Hash')
        self.tree.heading('Ações', text='Ações')
        
        self.tree.column('Data', width=200)
        self.tree.column('Hash', width=100)
        self.tree.column('Ações', width=100)
        
        # Adicionar scrollbar
        scrollbar = ttk.Scrollbar(main_frame, orient=tk.VERTICAL, command=self.tree.yview)
        scrollbar.grid(row=1, column=2, sticky=(tk.N, tk.S))
        self.tree.configure(yscrollcommand=scrollbar.set)
        
        # Botão de atualizar
        refresh_btn = ttk.Button(main_frame, text="Atualizar Lista", command=self.load_commits)
        refresh_btn.grid(row=2, column=0, pady=10)
        
        # Carregar commits iniciais
        self.load_commits()
        
        # Configurar evento de clique no botão de restaurar
        self.tree.bind('<Double-1>', self.on_restore_click)
        
    def load_commits(self):
        # Limpar lista atual
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        try:
            with open(self.history_file, 'r') as f:
                commits = f.readlines()
            
            for commit in commits:
                try:
                    # Parse da linha do commit
                    parts = commit.strip().split(']')
                    date_str = parts[0].strip('[')
                    commit_info = parts[1].split('Commit:')[1]
                    hash_part = commit_info.split('-')[0].strip()
                    
                    # Inserir na árvore
                    self.tree.insert('', 'end', values=(date_str, hash_part, 'Restaurar'))
                except Exception as e:
                    print(f"Erro ao processar commit: {e}")
                    
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao carregar commits: {str(e)}")
    
    def restore_commit(self, commit_hash):
        try:
            # Confirmar com o usuário
            if not messagebox.askyesno("Confirmar Restauração", 
                                     f"Tem certeza que deseja restaurar para o commit {commit_hash}?"):
                return
            
            # Executar script de restauração
            result = subprocess.run(
                [self.restore_script, commit_hash],
                capture_output=True,
                text=True
            )
            
            if result.returncode == 0:
                messagebox.showinfo("Sucesso", "Restauração concluída com sucesso!")
            else:
                messagebox.showerror("Erro", f"Erro na restauração: {result.stderr}")
                
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao restaurar: {str(e)}")
    
    def on_restore_click(self, event):
        # Obter item selecionado
        item = self.tree.selection()[0]
        commit_hash = self.tree.item(item)['values'][1]
        self.restore_commit(commit_hash)

def main():
    root = tk.Tk()
    app = GitRestoreGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
