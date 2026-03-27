import { connectDB } from "../database/db";

export async function criarOrdem(descricao: string, status: string, veiculo_id: number) {
  const db = await connectDB();
  return db.run(
    "INSERT INTO ordens (descricao, status, veiculo_id) VALUES (?, ?, ?)",
    [descricao, status, veiculo_id]
  );
}

export async function listarOrdens() {
  const db = await connectDB();
  return db.all("SELECT * FROM ordens");
}
