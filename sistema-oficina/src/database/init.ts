import { connectDB } from "./db";

export async function initDB() {
  const db = await connectDB();
  await db.exec("PRAGMA foreign_keys = ON;");

  await db.exec(`
    CREATE TABLE IF NOT EXISTS clientes (
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      nome TEXT NOT NULL,
      telefone TEXT NOT NULL
    );

    CREATE TABLE IF NOT EXISTS veiculos (
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      modelo TEXT NOT NULL,
      placa TEXT NOT NULL,
      cliente_id INTEGER NOT NULL,
      FOREIGN KEY (cliente_id) REFERENCES clientes(id)
    );

    CREATE TABLE IF NOT EXISTS ordens (
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      descricao TEXT NOT NULL,
      status TEXT NOT NULL,
      veiculo_id INTEGER NOT NULL,
      FOREIGN KEY (veiculo_id) REFERENCES veiculos(id)
    );
  `);
}
