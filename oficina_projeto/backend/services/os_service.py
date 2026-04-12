from database.db import conectar

def criar_os(os):
    conn = conectar()
    cursor = conn.cursor()

    sql = "INSERT INTO ordem_servico (descricao, status, id_veiculo) VALUES (%s, %s, %s)"
    cursor.execute(sql, (os.descricao, os.status, os.id_veiculo))

    conn.commit()
    cursor.close()
    conn.close()

    return {"mensagem": "Ordem de serviço criada"}

def obter_os_por_id(os_id):
    conn = conectar()
    cursor = conn.cursor()

    sql = "SELECT id, descricao, status, id_veiculo FROM ordem_servico WHERE id = %s"
    cursor.execute(sql, (os_id,))
    result = cursor.fetchone()

    cursor.close()
    conn.close()

    if result:
        return {"id": result[0], "descricao": result[1], "status": result[2], "id_veiculo": result[3]}
    else:
        return {"mensagem": "Ordem de serviço não encontrada"}
        
    def obter_todas_os():
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute("SELECT id, descricao, status, id_veiculo FROM ordem_servico")
        results = cursor.fetchall()
        cursor.close()
        conn.close()

        os_list = []
        for result in results:
            os_list.append({"id": result[0], "descricao": result[1], "status": result[2], "id_veiculo": result[3]})
        return os_list
    
    def atualizar_os(os_id, os):
        conn = conectar()
        cursor = conn.cursor()

        sql = "UPDATE ordem_servico SET descricao = %s, status = %s, id_veiculo = %s WHERE id = %s"
        cursor.execute(sql, (os.descricao, os.status, os.id_veiculo, os_id))

        conn.commit()
        cursor.close()
        conn.close()

        return {"mensagem": "Ordem de serviço atualizada com sucesso"}
    
    def deletar_os(os_id):
        conn = conectar()
        cursor = conn.cursor()

        sql = "DELETE FROM ordem_servico WHERE id = %s"
        cursor.execute(sql, (os_id,))

        conn.commit()
        cursor.close()
        conn.close()

        return {"mensagem": "Ordem de serviço deletada com sucesso"}
    
    def obter_os_por_veiculo(id_veiculo):
        conn = conectar()
        cursor = conn.cursor()

        sql = "SELECT id, descricao, status FROM ordem_servico WHERE id_veiculo = %s"
        cursor.execute(sql, (id_veiculo,))
        results = cursor.fetchall()

        cursor.close()
        conn.close()

        os_list = []
        for result in results:
        os_list.append({"id": result[0], "descricao": result[1], "status": result[2]})
        return os_list
    
    def obter_os_por_status(status):
        conn = conectar()
        cursor = conn.cursor()

        sql = "SELECT id, descricao, id_veiculo FROM ordem_servico WHERE status = %s"
        cursor.execute(sql, (status,))
        results = cursor.fetchall()

        cursor.close()
        conn.close()

        os_list = []
        for result in results:
            os_list.append({"id": result[0], "descricao": result[1], "id_veiculo": result[2]})
        return os_list
     
     def obter_os_por_descricao(descricao):
        conn = conectar()
        cursor = conn.cursor()

        sql = "SELECT id, status, id_veiculo FROM ordem_servico WHERE descricao LIKE %s"
        cursor.execute(sql, ('%' + descricao + '%', ))
        results = cursor.fetchall()
        cursor.close()
        conn.close()
        criptografar = []
        for result in results:
            criptografar.append({"id": result[0], "status": result[1], "id_veiculo": result[2]})
            return criptografar
        
        def obter_os_por_cliente(id_cliente):
            conn = conectar()
            cursor = conn.cursor()
            
        sql ="SELECT id, status, id_veiculo FROM ordem_servico WHERE descricao LIKE %s"
        cursor.execute(sql, ('%' + descricao + '%', ))
        results = cursor.fetchall()
        cursor.close()
        conn.close()
        criptografar = []
        for results in results:
            criptografar.append({"id": result[0], "status": result[1], "id_veiculo": result[2]})
          return criptografar
