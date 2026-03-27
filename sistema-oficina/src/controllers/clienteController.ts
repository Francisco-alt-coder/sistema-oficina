import { Request, Response } from "express";
import { criarCliente, listarClientes } from "../services/clienteService";

export async function create(req: Request, res: Response) {
  const { nome, telefone } = req.body;
  await criarCliente(nome, telefone);
  res.json({ message: "Cliente criado" });
}

export async function list(req: Request, res: Response) {
  const clientes = await listarClientes();
  res.json(clientes);
}
