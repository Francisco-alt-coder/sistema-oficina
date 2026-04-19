class OrdemServico:
    def __init__(self, descricao, status, id_veiculo):
        self.descricao = descricao
        self.status = status
        self.id_veiculo = id_veiculo
        self.id = None # ID será atribuido quando a ordem de serviço

        def __str__(self):
            return f"Ordem de serviço: {self.descricao}, Status: {self.status}, ID do Veículo: {self.id_veiculo}"
        
        def __repr__(self):
            return f"OrdemSevico(descricao={self.descricao}, status={self.status}, id_veiculo={self.id_veiculo})"
            
        def __eq__(self, other):
            if isinstance(other, OrdemServico):
                return self.id == other.id
            return False
        
        
        def to_dict(self):
            return {
                "id": self.id,
                "descricao": self.descricao,
                "status": self.status,
                "id_veiculo": self.id_veiculo
            }

        def from_dict(data):
            return OrdemServico(
                descricao=data.get("descricao"),
                status=data.get("status"),
                id_veiculo=data.get("id_veiculo")
            )
        
        def update(self, descricao=None, status=None, id_veiculo=None):
            if descricao:
                self.descricao = descricao
            if status:
                self.status = status
            if id_veiculo:
                self.id_veiculo = id_veiculo
            
            def delete(self):
                # Lógica para deletar a ordem de serviço 
                if self.id:
                    if self.id in OrdemServicoRepository.ordens_servico:
                        del OrdemServicoRepository.ordens_servico[self.id]
                    else:
                        print("Ordem de serviço não encontrada para deletar.")
                        print("Ordem de serviço deletada com sucesso.")
                pass
            def save(self):
                # Lógica para salvar a ordem de serviço 
                if self.id is None:
                    self.id = OrdemServicoRepository.get_next_id()
                    OrdemServicoRepository.ordens_servico[self.id] = self
                else:
                    OrdemServicoRepository.ordens_servico[self.id] = self
                print("Ordem de serviço criada com sucesso "if self.id is None else "Ordem de serviço atualizada com sucesso ")

 class OrdemServicoRepository:
    ordens_servico = {}
    current_id = 1

    @classmethod
    def get_next_id(cls):
        id_atual = cls.current_id
        cls.current_id += 1
        return id_atual
    
    @classmethod
    def listar_ordens_servico(cls):
        return list(cls.ordens_servico.values())
    
    @classmethod
    def buscar_ordem_servico(cls, id):
        return cls.ordens_servico.get(id)
    definir_ordem_servico(cls, ordem_servico)
if ordem_servico and ordem_servico.id:     
    
@classmethod  
def definir_ordem_servico(cls, ordem_servico)
    else:
print("Ordem de serviço inválida para definir.")

def deletar_ordem_servico(cls, id):
    if id in cls.ordens_servico:
        del cls.ordens_servico[id]
        print("Ordem de serviço deletada com sucesso.")
    else:
        print("Ordem de serviço não encontrada para deletar.")
    
def atualizar_ordem_servico(cls, id, descricao=None, status=None, id_veiculo=None):
    ordem_servico = cls.ordens_servico.get(id)
    if ordem_servico:
        ordem_servico.update(descricao, status, id_veiculo)
        print("Ordem de serviço atualizada com sucesso.")
    else:
        print("Ordem de serviço não encontrada para atualizar.")
    
  def criar_ordem_servico(cls, descricao, status, id_veiculo):
    nova_ordem = Ordemservico(descricao, status, id_veiculo)
    nova_ordem.save()
    print("Ordem de serviço criada com sucesso.")
 
   def listar_ordens_servico(cls):
    return list(cls.ordens_servico.values())

    
        