                                    Sistema de Gestão para Oficina Mecânica
 Proposta do Sistema
 
 Este projeto tem como objetivo desenvolver um sistema de gerenciamento para uma oficina mecânica, permitindo o controle de clientes, veículos, ordens de serviço e histórico de manutenção.
A aplicação busca resolver problemas comuns em oficinas, como organização de atendimentos, registro de serviços realizados e acompanhamento de clientes.

 Funcionalidades Principais
	Cadastro de clientes
	Cadastro de veículos
	Abertura de ordens de serviço
	Registro de serviços realizados
	Consulta de histórico de manutenção
	Listagem e busca de dados

   Fase De Desenvolvimento
 Fase 1 - Estrutura Inicial
	Configuração do ambiente Node.js com TypeScript
	Criação da estrutura de pastas

 Fase 2 - Implementação das Funcionalidades
	CRUD de clientes
    CRUD de veículos
	CRUD de ordens de serviço
 Fase 3 - Regras de Negócio
	Ass3ociação entre cliente e veículo
	Controle de status da ordem de serviço
     Fase 4 - Testes e Ajustes
	Testes manuais
	Correção de bugs
	Melhorias de performance
    Tecnologias Utilizadas
	Node.js
	TypeScript
	Python

 Passo 1 - Clonar o Repositório
https://github.com/seu-usuario/sistema-oficina-mecanica.git
Integração de Paradigmas de Programação
Este projeto utiliza a integração de múltiplos paradigmas para garantir organização, modularidade e escalabilidade:
 Programação Orientada a Objetos (POO)
	Utilizada nos models e services
	Representação de entidades como:
	Cliente
	Veículo
	Ordem de Serviço
Exemplo:
class Cliente {
  nome: string;
  telefone: string;  }
Programação Funcional
	Uso de funções puras nos serviços
	Manipulação de dados sem efeitos colaterais
	Uso de métodos como map, filter e reduce
Exemplo:
const clientesAtivos = clientes.filter(c => c.ativo);

 Programação Modular
	Separação do sistema em camadas:
	Controllers (entrada de dados)
	Services (regras de negócio)
	Models (estrutura dos dados)
	Routes (definição de endpoints)
Essa abordagem facilita manutenção e reutilização de código.

 Programação Assíncrona
	Uso de async/await para operações com banco de dados
	Evita bloqueio da aplicação
Exemplo:
const clientes = await clienteRepository.findAll();

 Estrutura Arquitetural
O sistema segue o padrão de arquitetura em camadas:
	Controller → Recebe requisições
	Service → Aplica regras de negócio
	Model → Representa os dados
	Repository/Database → Comunicação com o banco
 Considerações Finais
O sistema, simula um cenário que em breve ser realizado em uma oficina mecânica.
A estrutura permite expansão futura, como:
	Interface web
	Sistema de login
	Relatórios gerenciais
