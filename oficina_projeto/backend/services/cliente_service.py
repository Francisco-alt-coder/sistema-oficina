from database.db import conectar

def criar_cliente(cliente):
    conn = conectar()
    cursor = conn.cursor()

    sql = "INSERT INTO cliente (nome, telefone) VALUES (%s, %s)"
    cursor.execute(sql, (cliente.nome, cliente.telefone))

    conn.commit()
    cursor.close()
    conn.close()

    return {"mensagem": "Cliente cadastrado com sucesso"}

   def obter_cliente_por_id(cliente_id):
    conn = conectar()
    cursor = conn.cursor()

    sql = "SELECT id, nome, telefone FROM cliente WHERE id = %s"
    cursor.execute(sql, (cliente_id,))
    result = cursor.fetchone()

    cursor.close()
    conn.close()

    if result:
        return {"id": result[0], "nome": result[1], "telefone": result[2]}
    else:
        return {"mensagem": "Cliente não encontrado"}
    
    def obter_todos_clientes():
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute("SELECT id, nome, telefone FROM cliente")
        results = cursor.fetchall()
        cursor.close()
        conn.close()

        clientes = []
        for result in results:
            clientes.append({"id": result[0], "nome": result[1], "telefone": result[2]})

        return clientes
    
    def atualizar_cliente(cliente_id, cliente):
        conn = conectar()
        cursor = conn.cursor()

        sql = "UPDATE cliente SET nome = %s, telefone = %s WHERE id = %s"
        cursor.execute(sql, (cliente.nome, cliente.telefone, cliente_id))

        conn.commit()
        cursor.close()
        conn.close()

        return {"mensagem": "Cliente atualizado com sucesso"}
    
    def deletar_cliente(cliente_id):
        conn = conectar()
        cursor = conn.cursor()

        sql = "DELETE FROM cliente WHERE id = %s"
        cursor.execute(sql, (cliente_id,))

        conn.commit()
        cursor.close()
        conn.close()

        return {"mensagem": "Cliente deletado com sucesso"}
    
    def  obter_clientes_com_veiculos():
        conn = conectar()
        cursor = conn.cursor()

        sql = """
        SELECT c.id, c.nome, c.telefone, v.id, v.modelo, v.placa
        FROM cliente c
        LEFT JOIN veiculo v ON c.id = v.id_cliente
        """
        cursor.execute(sql)
        results = cursor.fetchall()
        
        cursor.close()
        conn.close()
        clientes = {}
        for result in results:
            cliente_id = result[0]
            if cliente_id not in clientes:
                clientes[cliente_id] = {
                    "id": cliente_id,
                    "nome": result[1],
                    "telefone": result[2],

                }

            if result[3]: # Verifica se o cliente tem um veiculo associado
                if "veiculos" not in cliente_id:
                    cliente = cliente cliente_id
                    cliente["veiculos"] = []
                    cliente["veiculos"].append({
                        "id": result[3],
                        "modelo": result[4],
                        "placa": result[5],
                    })
        return list(clientes.values())

        