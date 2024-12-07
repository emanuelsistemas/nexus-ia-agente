# Documentação do Projeto Nexus IA

## Visão Geral
O Nexus IA é um assistente virtual especializado em desenvolvimento de software, projetado para auxiliar desenvolvedores em suas tarefas diárias. O sistema utiliza a API da Anthropic (Claude) para processamento de linguagem natural e mantém um histórico contextual das conversas usando ChromaDB.

## Estrutura do Projeto
```
/v1
├── backend/           # APIs e lógica do servidor
├── config/           # Configurações do projeto
├── database/         # Armazenamento ChromaDB
├── docs/             # Documentação
├── frontend/         # Interface do usuário
├── logs/             # Arquivos de log
├── .env              # Variáveis de ambiente
├── main.py           # Ponto de entrada da aplicação
└── requirements.txt  # Dependências Python
```

## Componentes Principais

### Backend
- FastAPI para APIs REST
- Integração com Claude (Anthropic) para processamento de linguagem natural
- ChromaDB para armazenamento de conversas e contexto
- Sistema de logging para monitoramento

### Frontend
- Interface web para interação com o usuário
- Sistema de chat em tempo real
- Histórico de conversas

## Configuração do Ambiente
Consulte SETUP.md para instruções detalhadas de instalação e configuração.

## Documentação Adicional
- ARCHITECTURE.md - Detalhes da arquitetura do sistema
- API.md - Documentação das APIs
- DEVELOPMENT.md - Guia para desenvolvimento
- PROGRESS.md - Status atual e próximos passos

## Propósito e Objetivos
1. Fornecer assistência especializada em desenvolvimento
2. Manter contexto das conversas para melhor compreensão
3. Sugerir boas práticas de desenvolvimento
4. Auxiliar na documentação e revisão de código

