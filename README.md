# Nexus IA v1

Assistente de desenvolvimento inteligente com capacidades de programação e memória.

## Estrutura do Projeto

```
v1/
├── backend/          # Backend principal
│   ├── api/         # Endpoints da API
│   ├── core/        # Lógica principal
│   ├── models/      # Modelos de dados
│   ├── tests/       # Testes unitários
│   └── utils/       # Funções utilitárias
├── config/          # Configurações do projeto
├── database/        # Arquivos do Chroma DB
├── docs/            # Documentação
├── frontend/        # Frontend
│   ├── public/      # Arquivos estáticos
│   └── src/         # Código fonte React
└── logs/            # Logs da aplicação
```

## Configuração do Ambiente

1. Instalar dependências Python:
```bash
pip install -r requirements.txt
```

2. Configurar variáveis de ambiente:
```bash
cp .env.example .env
# Editar .env com suas configurações
```

3. Iniciar o backend:
```bash
python -m backend.api.main
```

4. Iniciar o frontend:
```bash
cd frontend
npm install
npm start
```

## Documentação

Consulte a pasta `docs/` para documentação detalhada.

## Licença

Proprietário - Todos os direitos reservados
