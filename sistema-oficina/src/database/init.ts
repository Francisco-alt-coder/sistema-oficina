import { connectDB } from "./db";

export async function initDB() {
  const db = await connectDB();

  await db.exec(`
    CREATE TABLE IF NOT EXISTS clientes (
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      nome TEXT,
      telefone TEXT
    );

    CREATE TABLE IF NOT EXISTS veiculos (
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      modelo TEXT,
      placa TEXT,
      cliente_id INTEGER
    );

    CREATE TABLE IF NOT EXISTS ordens (
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      descricao TEXT,
      status TEXT,
      veiculo_id INTEGER
    );
  `);
}
