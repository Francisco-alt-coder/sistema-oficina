# sistema-oficina

API simples para cadastro de clientes, veículos e ordens de serviço de uma oficina.

## Requisitos

- Node.js 18+
- npm

## Como executar

```bash
cd sistema-oficina
npm install
npm run dev
```

A API será iniciada em `http://localhost:3000`.

## Build

```bash
cd sistema-oficina
npm run build
```

## Endpoints

### Clientes

- `POST /clientes`
  - Body:
    ```json
    {
      "nome": "João Silva",
      "telefone": "11999999999"
    }
    ```
- `GET /clientes`

### Veículos

- `POST /veiculos`
  - Body:
    ```json
    {
      "modelo": "Fiat Uno",
      "placa": "ABC-1234",
      "cliente_id": 1
    }
    ```
- `GET /veiculos`

### Ordens

- `POST /ordens`
  - Body:
    ```json
    {
      "descricao": "Troca de óleo",
      "status": "aberta",
      "veiculo_id": 1
    }
    ```
  - Status aceitos: `aberta`, `em_andamento`, `concluida`, `cancelada`
- `GET /ordens`

## Respostas de erro

A API retorna `400` quando os campos obrigatórios não são enviados ou estão inválidos.
