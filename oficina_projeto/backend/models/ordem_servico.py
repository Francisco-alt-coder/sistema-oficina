class OrdemServico:
    def __init__(self, descricao, status, id_veiculo):
        self.descricao = descricao
        self.status = status
        self.id_veiculo = id_veiculo
        self.id = None # ID será atribuido quando a ordem de serviço

        def __str__(self):
            return f"Ordem de serviço: {self.descricao}, Status: {self.status}, ID do Veículo: {self.id_veiculo}"
        
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

    