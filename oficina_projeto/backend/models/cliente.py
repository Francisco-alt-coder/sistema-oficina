class Cliente:
    def __init__(self, nome, cpf, telefone, endereco, email):
        self.nome = nome
        self.cpf = cpf
        self.telefone = telefone
        self.endereco = endereco
        self.email = email
        self.id = None # ID será atribuido quando o cadastro do cliente for salvo

        def __str__(self):
            return f"Cliente: {self.nome}, CPF: {self.cpf}, Telefone: {self.telefone}, Endereço: {self.endereco}, Email: {self.email}"
    
        def to_dict(self):
            return {
                "id": self.id,
                "nome": self.nome,
                "cpf": self.cpf,
                "telefone": self.telefone,
                "endereco": self.endereco,
                "email": self.email
            }

         def from_dict(data):
            return Cliente(
                nome=data.get("nome"),
                cpf=data.get("cpf"),
                telefone=data.get("telefone"),
                endereco=data.get("endereco"),
                email=data.get("email")
            )
        
        def update(self, nome=None, cpf=None, telefone=None, endereco=None, email=None):
            if nome:
                self.nome = nome
            if cpf:
                self.cpf = cpf
            if telefone:
                self.telefone = telefone
            if endereco:
                self.endereco = endereco
            if email:
                self.email = email
            
            def delete(self):
                # Lógica para deletar o cliente 
                if self.id:
                if self.id in ClienteRepository.clientes:
                    del ClienteRepository.clientes[self.id]
                else:
                    print("Cliente não encontrado para deletar.")
                    print("Cliente deletado com sucesso.")
                pass
            def save(self):
                # Lógica para salvar o cliente 
                if self.id is None:
                    self.id = ClienteRepository.get_next_id()
                    ClienteRepository.clientes[self.id] = self
                else:
                    ClienteRepository.clientes[self.id] = self
                print("Cliente cadastrado com sucesso "if self.id is None else "Cliente atualizado com sucesso ")
                print("Cliente atualizado com sucesso ")
             
             def get_by_id(cliente_id):
                # Lógica para obter um cliente por ID
                return ClienteRepository.clientes.get(cliente_id)
                
                def get_all():
                    return list(ClienteRepository.clientes.values())
        