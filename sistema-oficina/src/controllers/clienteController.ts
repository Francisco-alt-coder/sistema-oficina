import { Request, Response } from "express";
import { criarCliente, listarClientes } from "../services/clienteService";

export async function create(req: Request, res: Response) {
  const { nome, telefone } = req.body;

  if (typeof nome !== "string" || nome.trim().length === 0) {
    return res.status(400).json({ message: "Campo 'nome' é obrigatório" });
  }

  if (typeof telefone !== "string" || telefone.trim().length === 0) {
    return res.status(400).json({ message: "Campo 'telefone' é obrigatório" });
  }

  await criarCliente(nome.trim(), telefone.trim());
  return res.status(201).json({ message: "Cliente criado" });
}

export async function list(_req: Request, res: Response) {
  const clientes = await listarClientes();
  return res.json(clientes);
}
