import { Request, Response } from "express";
import { criarVeiculo, listarVeiculos } from "../services/veiculoService";

export async function create(req: Request, res: Response) {
  const { modelo, placa, cliente_id } = req.body;
  await criarVeiculo(modelo, placa, cliente_id);
  res.json({ message: "Veículo criado" });
}

export async function list(req: Request, res: Response) {
  const dados = await listarVeiculos();
  res.json(dados);
}
