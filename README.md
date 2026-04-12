                                              Sistema De Agendamento De Oficina


1. Proposta do Sistema

Este projeto tem como objetivo desenvolver um sistema para gerenciamento de uma oficina mecânica, permitindo o controle eficiente de clientes, veículos e ordens de serviço.

A aplicação foi construída com foco em:

Organização de dados
Separação de responsabilidades
Escalabilidade
Integração entre tecnologias

O sistema simula um ambiente real de oficina, onde é possível cadastrar clientes, associar veículos e registrar serviços realizados.

2. Equipe Responsável
Francisco Wesley

3. Tecnologias Utilizadas
Tecnologia	Função
Python (Flask)	Backend principal
Node.js (Express)	API intermediária (middleware)
TypeScript	Cliente (consumo da API)

O sistema segue uma arquitetura distribuída em camadas:

Frontend (TypeScript)
        ↓
Backend Python (Regras de negócio)
 
5. Paradigmas de Programação Utilizados
🔹 Programação Orientada a Objetos (POO)

Aplicada no backend em Python:

Classes como Cliente, Veiculo e OrdemServico
Representação das entidades do sistema
🔹 Programação Funcional
Funções nos services (ex: criar_cliente)
Lógica isolada e reutilizável
Evita dependência de estado global
🔹 Programação Modular
Organização em camadas:
models → estrutura dos dados
services → regras de negócio
controllers → rotas
🔹 Programação Assíncrona 
Uso de async/await
Comunicação entre serviços
Modelo event-driven

6. Estrutura do Projeto
oficina/
│
├── backend-python/
│   ├── models/
│   ├── services/
│   ├── database/
│   
├── backend-node/
│
├── frontend/
│   └── app.ts
│
└── README.md

7. Fluxo do Sistema
Cliente é cadastrado
Veículo é vinculado ao cliente
Ordem de serviço é criada para o veículo

8. Funcionalidades Implementadas
Cadastro de clientes
Cadastro de veículos
Criação de ordens de serviço
Integração entre Python e Node.js
Consumo da API via TypeScript

9. Roadmap de Desenvolvimento
 Estrutura inicial do projeto
 Cadastro de clientes
 Cadastro de veículos
 Ordens de serviço
 Autenticação de usuários

10. Integração entre Tecnologias

A comunicação entre os sistemas ocorre via API REST utilizando JSON:

Node.js consome o backend Python
TypeScript consome o Node.js
Tudo desacoplado e escalável

11. Considerações Finais

Este projeto demonstra na prática:

Integração entre múltiplas linguagens
Uso combinado de paradigmas de programação
Organização em arquitetura modular
Separação clara de responsabilidades
