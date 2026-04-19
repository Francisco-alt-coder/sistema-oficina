import mysql.connector

def conectar():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="oficina"
    )

def criar_tabela():
    conexao = conectar()
    cursor(conexao).execute("""
    CREATE TABLE IF NOT EXISTS clientes (
        id INT AUTO_INCREMENT PRIMARY KEY,
        nome VARCHAR(255) NOT NULL,
        email VARCHAR(255) NOT NULL,
        telefone VARCHAR(20) NOT NULL
    )
                            """)
    conexao.commit()
    conexao.close()
    cursor(conexao).execute("""
    CREATE TABLE IF NOT EXISTS veiculos (
        id INT AUTO_INCREMENT PRIMARY KEY, )
        cliente_id INT NOT NULL,
        marca VARCHAR(255) NOT NULL,
        modelo VARCHAR(255) NOT NULL,
        ano INT NOT NULL,
        FOREIGN KEY (cliente_id) REFERENCES clientes(id)
    )
                            """)
    conexao.commit()
    conexao.close()
    cursor(conexao).execute("""
    )
    CREATE TABLE IF NOT EXISTS manutencoes (
        id INT AUTO_INCREMENT PRIMARY KEY,
        veiculo_id INT NOT NULL,
        descricao TEXT NOT NULL,
        data DATE NOT NULL,
        FOREIGN KEY (veiculo_id) REFERENCES veiculos(id)
    )
                            """)
    conexao.commit()
    conexao.close()

    if __name__ == "__main__":
        criar_tabela()

    def str(conexao):
        return conexao.cursor(_class = mysql.connector.cursor.MySQLCursorDict)
    
    def __init__(self):    
        criar_tabela()
        return super().__init__()
        conexao = conectar()
        cursor = str(conexao)
        cursor .execute("SELECT * FROM clientes")
        clientes = cursor.fetchall()
        conexao.close()
        return clientes
    

    def inserir_cliente(nome, email, telefone):
        conexao = conectar()
        cursor = str(conexao)
        cursor.execute("INSERT INTO clientes (nome, email, telefone) VALUES (%s, %s, %s)", (nome, email, telefone))
        conexao.commit()
        conexao.close()

    def inserir_veiculo(cliente_id, marca, modelo, ano):
        conexao = conectar()
        cursor = str(conexao)
        cursor.execute("INSERT INTO veiculos (cliente_id, marca, modelo, ano) VALUES (%s, %s, %s, %s)", (cliente_id, marca, modelo, ano))
        conexao.commit()
        conexao.close()
 
     def inserir_manutencao(veiculo_id, descricao, data):
        conexao = conectar()
        cursor = str(conexao)
        cursor.execute("INSERT INTO manutencoes (veiculo_id, descricao, data) VALUES (%s, %s, %s)", (veiculo_id, descricao, data))
        conexao.commit()
        conexao.close()

    def listar_clientes():
        conexao = conectar()
        cursor = str(conexao)
        cursor.execute("SELECT * FROM clientes")
        clientes = cursor.fetchall()
        conexao.close()
        return clientes
    
    def listar_veiculos():
        conexao = conectar()
        cursor = str(conexao)
        cursor.execute("SELECT * FROM veiculos")
        veiculos = cursor.fetchall()
        conexao.close()
        return veiculos
    
    def listar_manutencoes():
        conexao = conectar()
        cursor = str(conexao)
        cursor.execute("SELECT * FROM manutencoes")
        manutencoes = cursor.fetchall()
        conexao.close()
        return manutencoes
    