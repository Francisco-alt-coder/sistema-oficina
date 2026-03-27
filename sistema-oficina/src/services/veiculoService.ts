import { connectDB } from "../database/db";

export async function criarVeiculo(modelo: string, placa: string, cliente_id: number) {
  const db = await connectDB();
  return db.run(
    "INSERT INTO veiculos (modelo, placa, cliente_id) VALUES (?, ?, ?)",
    [modelo, placa, cliente_id]
  );
}

export async function listarVeiculos() {
  const db = await connectDB();
  return db.all("SELECT * FROM veiculos");
}
