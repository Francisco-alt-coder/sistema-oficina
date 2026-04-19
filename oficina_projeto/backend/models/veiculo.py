class Veiculo:
    def __init__(self, modelo, placa, id_cliente):
        self.modelo = modelo
        self.placa = placa
        self.id_cliente = id_cliente
        self.id = None # ID será atribuido quando o cadastro do veículo for salvo

        def __str__(self):
            return f"Veículo: {self.modelo}, Placa: {self.placa}, ID do Cliente: {self.id_cliente}, ID: {self.id}"
        
        def to_dict(self):
            return {
                "id": self.id,
                "modelo": self.modelo,
                "placa": self.placa,
                "id_cliente": self.id_cliente
            }
        
        def from_dict(data):
            return Veiculo(
                modelo=data.get("modelo"),
                placa=data.get("placa"),
                id_cliente=data.get("id_cliente")
            )
        
        def update(self, modelo=None, placa=None, id_cliente=None):
            if modelo:
                self.modelo = modelo
            if placa:
                self.placa = placa
            if id_cliente:
                self.id_cliente = id_cliente

                def delete(self):
                    # Lógica para deletar o veículo
                    if self.id:
                        if self.id in VeiculoRepository.veiculos:
                            del VeiculoRepository.veiculos[self.id]
                        else:
                        print("Veículo não encontrado para deletar.")
                        print("Veículo deletado com sucesso.")
                        pass

                    def save(self):
                        # Lógica para salvar o veículo
                        if self.id is None:
                            self.id = VeiculoRepository.get_next_id()
                            VeiculoRepository.veiculos[self.id] = self
                        else:
                            VeiculoRepository.veiculos[self.id] = self
                        print("Veículo cadastrado com sucesso "if self.id is None else "Veículo atualizado com sucesso ")

                    def get_by_id(id):
                        return VeiculoRepository.veiculos.get(id)
                    
                    
                    