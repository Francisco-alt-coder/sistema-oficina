async function cadastrarCliente() {
    await fetch("http://localhost:5000/clientes", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({ nome: "João", telefone: "99999-9999" })
    });
}

cadastrarCliente();

// cadastroCliente.ts
// Requisição POST robusta com validação, timeout e retries
export interface Cliente {
  nome: string;
  telefone: string;
  email?: string;
}
export class RequestError extends Error {
  public status?: number;
  constructor(message: string, status?: number) {
    super(message);
    this.name = "RequestError";
    this.status = status;
  }
}
const DEFAULT_TIMEOUT_MS = 5000;
const DEFAULT_RETRIES = 2;
function validateCliente(cliente: Cliente) {
  if (!cliente || typeof cliente !== "object") {
    throw new Error("Cliente inválido: deve ser um objeto.");
  }
  if (!cliente.nome || typeof cliente.nome !== "string") {
    throw new Error("Nome inválido: deve ser uma string não vazia.");
  }
  if (!cliente.telefone || typeof cliente.telefone !== "string") {
    throw new Error("Telefone inválido: deve ser uma string não vazia.");
  }
  if (cliente.email && typeof cliente.email !== "string") {
    throw new Error("Email inválido: se fornecido, deve ser uma string.");
  }
}
async function fetchWithTimeout(input: RequestInfo, init: RequestInit, timeout = DEFAULT_TIMEOUT_MS) {
  const controller = new AbortController();
  const id = setTimeout(() => controller.abort(), timeout);
  try {
    const response = await fetch(input, { ...init, signal: controller.signal });
    return response;
  } finally {
    clearTimeout(id);
  }
}
export async function cadastrarCliente(
  cliente: Cliente,
  url = "http://localhost:5000/clientes",
  retries = DEFAULT_RETRIES,
  timeout = DEFAULT_TIMEOUT_MS
): Promise<any> {
  validateCliente(cliente);
  const body = JSON.stringify(cliente);
  const headers = { "Content-Type": "application/json" };
  for (let attempt = 0; attempt <= retries; attempt++) {
    try {
      console.log(`Tentativa ${attempt + 1} de ${retries + 1} - Enviando dados do cliente...`);
      const resposta = await fetchWithTimeout(url, { method: "POST", headers, body }, timeout);
      if (!resposta) {
        throw new RequestError("Nenhuma resposta recebida do servidor.");
      }
      if (!resposta.ok) {
        const text = await resposta.text().catch(() => "");
        throw new RequestError(`Erro na requisição: ${resposta.status} ${resposta.statusText} - ${text}`, resposta.status);
      }
      const dados = await resposta.json().catch(() => null);
      console.log("Cliente cadastrado com sucesso:", dados);
      return dados;
    } catch (erro) {
      const isAbort = (erro instanceof DOMException && erro.name === "AbortError") || (erro as any).name === "AbortError";
      const isLastAttempt = attempt === retries;
      console.error(`Falha na tentativa ${attempt + 1}:`, (erro as Error).message);
      if (isLastAttempt) {
        if (isAbort) {
          throw new RequestError("Requisição abortada por timeout.", 0);
        }
        if (erro instanceof RequestError) {
          throw erro;
        }
        throw new RequestError("Falha ao cadastrar cliente: " + (erro as Error).message);
      }
      const backoff = 200 * Math.pow(2, attempt);
      console.log(`Aguardando ${backoff}ms antes da próxima tentativa...`);
      await new Promise((res) => setTimeout(res, backoff));
    }
  }
}
// Exemplo de uso com dados dinâmicos
async function exemplo() {
  try {
    const novoCliente: Cliente = { nome: "João", telefone: "99999-9999", email: "joao@example.com" };
    await cadastrarCliente(novoCliente);
  } catch (err) {
    console.error("Erro ao cadastrar no exemplo:", (err as Error).message);
  }
}
// Executa o exemplo quando o módulo for executado diretamente
if (typeof require !== "undefined" && (require as any).main === module) {
  exemplo().catch((e) => console.error("Erro não tratado no exemplo:", e));
}

// Export default for convenience
export default cadastrarCliente;

  