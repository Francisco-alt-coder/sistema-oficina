import { Request, Response } from "express";
import { criarOrdem, listarOrdens } from "../services/ordemService";

export async function create(req: Request, res: Response) {
  const { descricao, status, veiculo_id } = req.body;
  await criarOrdem(descricao, status, veiculo_id);
  res.json({ message: "Ordem criada" });
}

export async function list(req: Request, res: Response) {
  const dados = await listarOrdens();
  res.json(dados);
}
