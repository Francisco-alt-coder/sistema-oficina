import { connectDB } from "../database/db";

export async function criarCliente(nome: string, telefone: string) {
  const db = await connectDB();
  return db.run("INSERT INTO clientes (nome, telefone) VALUES (?, ?)", [nome, telefone]);
}

export async function listarClientes() {
  const db = await connectDB();
  return db.all("SELECT * FROM clientes");
}
