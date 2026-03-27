import { Request, Response } from "express";
import { criarVeiculo, listarVeiculos } from "../services/veiculoService";

export async function create(req: Request, res: Response) {
  const { modelo, placa, cliente_id } = req.body;

  if (typeof modelo !== "string" || modelo.trim().length === 0) {
    return res.status(400).json({ message: "Campo 'modelo' é obrigatório" });
  }

  if (typeof placa !== "string" || placa.trim().length === 0) {
    return res.status(400).json({ message: "Campo 'placa' é obrigatório" });
  }

  if (!Number.isInteger(cliente_id) || cliente_id <= 0) {
    return res.status(400).json({ message: "Campo 'cliente_id' deve ser um inteiro positivo" });
  }

  await criarVeiculo(modelo.trim(), placa.trim(), cliente_id);
  return res.status(201).json({ message: "Veículo criado" });
}

export async function list(_req: Request, res: Response) {
  const dados = await listarVeiculos();
  return res.json(dados);
}
