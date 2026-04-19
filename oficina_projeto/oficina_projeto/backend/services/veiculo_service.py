from database.db import conectar

def criar_veiculo(veiculo):
    conn = conectar()
    cursor = conn.cursor()

    sql = "INSERT INTO veiculo (modelo, placa, id_cliente) VALUES (%s, %s, %s)"
    cursor.execute(sql, (veiculo.modelo, veiculo.placa, veiculo.id_cliente))

    conn.commit()
    cursor.close()
    conn.close()

    return {"mensagem": "Veículo cadastrado com sucesso"}

@dataclass
class Veiculo:
    modelo: str
    placa: str
    id_cliente: int
    cor: Opcional[str] = None
    ano: Opcional[int] = None

class ValidationError(Exception):
    pass
class DatabaseError(Exception):
    pass

def get_cursor(conn):
    cursor = conn.cursor()
    try:
        yield cursor
    finally:
        try:
            cursor.close()
        except Exception:
            logger.debug("Erro ao fechar cursor", exc_info=True)

def validar_veiculo(veiculo: Veiculo) -> None:
    if not veiculo.modelo or not isinstance(veiculo.modelo, str):
        raise ValidationError("Modelo inválido: deve ser uma string não vazia.")
    if not veiculo.placa or not isinstance(veiculo.placa, str):
        raise ValidationError("Placa inválida: deve ser uma string não vazia.")
    if not isinstance(veiculo.id_cliente, int) or veiculo.id_cliente <= 0:
        raise ValidationError("id_cliente inválido: deve ser um inteiro positivo.")
    if veiculo.ano is not None and (veiculo.ano < 1886 or veiculo.ano > 2100):
        raise ValidationError("Ano inválido: fora do intervalo plausível.")

def criar_veiculo(veiculo: Veiculo, retries: int = 2, backoff_base: float = 0.2) -> Dict[str, Any]:
    validar_veiculo(veiculo)
    attempt = 0
    sql = "INSERT INTO veiculo (modelo, placa, id_cliente, cor, ano) VALUES (%s, %s, %s, %s, %s)"
    params = (veiculo.modelo, veiculo.placa, veiculo.id_cliente, veiculo.cor, veiculo.ano)
    while True:
        try:
            conn = conectar()
            with get_cursor(conn) as cursor:
                logger.info("Executando INSERT de veículo para cliente %s", veiculo.id_cliente)
                cursor.execute(sql, params)
                inserted_id = getattr(cursor, "lastrowid", None)
            conn.commit()
            conn.close()
            logger.info("Veículo cadastrado com sucesso. ID: %s", inserted_id)
            return {"mensagem": "Veículo cadastrado com sucesso", "id": inserted_id}
        except ValidationError:
            logger.exception("Validação falhou ao tentar cadastrar veículo.")
            raise
        except Exception as e:
            attempt += 1
            logger.error("Erro ao cadastrar veículo (tentativa %d): %s", attempt, str(e))
            try:
                conn.rollback()
            except Exception:
                logger.debug("Rollback falhou ou conexão já fechada.", exc_info=True)
            try:
                conn.close()
            except Exception:
                pass
            if attempt > retries:
                logger.exception("Número máximo de tentativas atingido. Abortando operação.")
                raise DatabaseError("Falha ao cadastrar veículo após várias tentativas.") from e
            sleep_time = backoff_base * (2 ** (attempt - 1))
            logger.info("Aguardando %.1f segundos antes da próxima tentativa...", sleep_time)
            time.sleep(sleep_time)

def exemplo_uso():
    try:
        novo = Veiculo(modelo="Fiat Uno", placa="ABC1D23", id_cliente=1, cor="Prata", ano=2010)
        resultado = criar_veiculo(novo)
        print(resultado)
    except ValidationError as ve:
        print({"erro": "Validação", "mensagem": str(ve)})
    except DatabaseError as de:
        print({"erro": "Banco de dados", "mensagem": str(de)})
    except Exception as e:
        print({"erro": "Desconhecido", "mensagem": str(e)})
if __name__ == "__main__":
    exemplo_uso()

def veiculo_from_dict(data: Dict[str, Any]) -> Veiculo:
    return Veiculo(modelo=data.get("modelo", ""), placa=data.get("placa", ""), id_cliente=int(data.get("id_cliente", 0)), cor=data.get("cor"), ano=data.get("ano"))

def _teste_unitario_simples():
    sample = {"modelo":"Gol","placa":"XYZ9A99","id_cliente":2,"cor":"Azul","ano":2015}
    v = veiculo_from_dict(sample)
    try: criar_veiculo(v); logger.info("Teste unitário simples executado.")
    except Exception: logger.exception("Teste unitário simples falhou.")