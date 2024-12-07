# Guia de Instalação e Configuração

## Pré-requisitos
- Python 3.8+
- pip (gerenciador de pacotes Python)
- Chave API da Anthropic

## Instalação

1. Clone o repositório:
```bash
git clone [URL_DO_REPOSITORIO]
cd nexus-ia/v1
```

2. Crie e ative o ambiente virtual:
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# ou
venv\Scripts\activate  # Windows
```

3. Instale as dependências:
```bash
pip install -r requirements.txt
```

4. Configure as variáveis de ambiente:
```bash
cp .env.example .env
# Edite .env com suas configurações
```

## Configuração

### Variáveis de Ambiente (.env)
```env
# Ambiente
ENVIRONMENT=development

# API Keys
ANTHROPIC_API_KEY=sua_chave_aqui

# Servidor
HOST=0.0.0.0
PORT=8001

# Banco de Dados
CHROMA_PERSISTENCE_DIR=./database/chroma

# Logs
LOG_LEVEL=INFO
LOG_DIR=./logs
```

## Executando o Projeto

1. Inicie o servidor:
```bash
python main.py
```

2. Acesse a API:
- Documentação: http://localhost:8001/docs
- API: http://localhost:8001/

## Estrutura de Diretórios
Certifique-se que os seguintes diretórios existem e têm permissões corretas:
- /logs - Para arquivos de log
- /database/chroma - Para dados do ChromaDB

## Troubleshooting

### Problemas Comuns

1. Porta em uso:
```bash
# Verifique processos usando a porta
lsof -i :8001
# Mate o processo se necessário
kill -9 PID
```

2. Erros de permissão:
```bash
# Ajuste permissões dos diretórios
chmod -R 755 logs/
chmod -R 755 database/
```

