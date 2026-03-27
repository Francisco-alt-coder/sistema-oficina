import express from "express";
import cors from "cors";
import routes from "./routes";
import { initDB } from "./database/init";

const app = express();

app.use(cors());
app.use(express.json());
app.use(routes);

initDB().then(() => {
  app.listen(3000, () => {
    console.log("Servidor rodando em http://localhost:3000");
  });
});
