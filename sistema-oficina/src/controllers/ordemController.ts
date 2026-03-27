import { Request, Response } from "express";
import { criarOrdem, listarOrdens } from "../services/ordemService";

const STATUS_VALIDOS = ["aberta", "em_andamento", "concluida", "cancelada"];

export async function create(req: Request, res: Response) {
  const { descricao, status, veiculo_id } = req.body;

  if (typeof descricao !== "string" || descricao.trim().length === 0) {
    return res.status(400).json({ message: "Campo 'descricao' é obrigatório" });
  }

  if (typeof status !== "string" || !STATUS_VALIDOS.includes(status)) {
    return res.status(400).json({
      message: "Campo 'status' inválido. Use: aberta, em_andamento, concluida ou cancelada"
    });
  }

  if (!Number.isInteger(veiculo_id) || veiculo_id <= 0) {
    return res.status(400).json({ message: "Campo 'veiculo_id' deve ser um inteiro positivo" });
  }

  await criarOrdem(descricao.trim(), status, veiculo_id);
  return res.status(201).json({ message: "Ordem criada" });
}

export async function list(_req: Request, res: Response) {
  const dados = await listarOrdens();
  return res.json(dados);
}
