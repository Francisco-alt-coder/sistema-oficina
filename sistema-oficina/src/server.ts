import express from "express";
import cors from "cors";
import routes from "./routes";
import { initDB } from "./database/init";

const app = express();

app.use(cors());
app.use(express.json());
app.use(routes);

app.use((err: Error, _req: express.Request, res: express.Response, _next: express.NextFunction) => {
  console.error("Erro não tratado:", err);
  return res.status(500).json({ message: "Erro interno do servidor" });
});

initDB()
  .then(() => {
    app.listen(3000, () => {
      console.log("Servidor rodando em http://localhost:3000");
    });
  })
  .catch((err: unknown) => {
    console.error("Falha ao inicializar banco de dados:", err);
    process.exit(1);
  });
