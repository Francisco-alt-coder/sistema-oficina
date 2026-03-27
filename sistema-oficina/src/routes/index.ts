import { Router } from "express";
import * as cliente from "../controllers/clienteController";
import * as veiculo from "../controllers/veiculoController";
import * as ordem from "../controllers/ordemController";

const routes = Router();

routes.post("/clientes", cliente.create);
routes.get("/clientes", cliente.list);

routes.post("/veiculos", veiculo.create);
routes.get("/veiculos", veiculo.list);

routes.post("/ordens", ordem.create);
routes.get("/ordens", ordem.list);

export default routes;
