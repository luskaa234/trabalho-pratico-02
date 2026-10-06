class Veiculo:
    def __init__(self, placa, modelo, ano, valor_diaria):
        self.placa = placa
        self.modelo = modelo
        self.ano = ano
        self.valor_diaria = valor_diaria

    def calcular_diaria(self, quantidade_dias=1):
        return self.valor_diaria * quantidade_dias

    def exibir_dados(self):
        return f"{self.placa} - {self.modelo} - {self.ano} - R$ {self.valor_diaria:.2f}"


class Carro(Veiculo):
    def __init__(self, placa, modelo, ano, valor_diaria, quantidade_portas):
        super().__init__(placa, modelo, ano, valor_diaria)
        self.quantidade_portas = quantidade_portas

    def calcular_diaria(self, quantidade_dias=1):
        return super().calcular_diaria(quantidade_dias)

    def exibir_dados(self):
        return f"Carro: {super().exibir_dados()} - {self.quantidade_portas} portas"


class Moto(Veiculo):
    def __init__(self, placa, modelo, ano, valor_diaria, cilindradas):
        super().__init__(placa, modelo, ano, valor_diaria)
        self.cilindradas = cilindradas

    def calcular_diaria(self, quantidade_dias=1):
        return super().calcular_diaria(quantidade_dias)

    def exibir_dados(self):
        return f"Moto: {super().exibir_dados()} - {self.cilindradas} cc"


class Caminhao(Veiculo):
    def __init__(self, placa, modelo, ano, valor_diaria, capacidade_carga):
        super().__init__(placa, modelo, ano, valor_diaria)
        self.capacidade_carga = capacidade_carga

    def calcular_diaria(self, quantidade_dias=1):
        return super().calcular_diaria(quantidade_dias)

    def exibir_dados(self):
        return f"Caminhão: {super().exibir_dados()} - {self.capacidade_carga} kg"


class Cliente:
    def __init__(self, nome_razao_social, documento, telefone):
        self.nome_razao_social = nome_razao_social
        self.documento = documento
        self.telefone = telefone

    def atualizar_telefone(self, telefone):
        self.telefone = telefone

    def exibir_dados(self):
        return f"{self.nome_razao_social} - {self.documento} - {self.telefone}"


class PessoaFisica(Cliente):
    def __init__(self, nome, cpf, telefone):
        super().__init__(nome, cpf, telefone)
        self.nome = nome
        self.cpf = cpf

    def atualizar_telefone(self, telefone):
        super().atualizar_telefone(telefone)

    def exibir_dados(self):
        return f"Pessoa Física: {self.nome} - CPF: {self.cpf} - {self.telefone}"


class PessoaJuridica(Cliente):
    def __init__(self, razao_social, cnpj, telefone):
        super().__init__(razao_social, cnpj, telefone)
        self.razao_social = razao_social
        self.cnpj = cnpj

    def atualizar_telefone(self, telefone):
        super().atualizar_telefone(telefone)

    def exibir_dados(self):
        return f"Pessoa Jurídica: {self.razao_social} - CNPJ: {self.cnpj} - {self.telefone}"


class Condutor:
    def __init__(self, nome, numero_cnh, categoria_cnh):
        self.nome = nome
        self.numero_cnh = numero_cnh
        self.categoria_cnh = categoria_cnh

    def atualizar_cnh(self, numero_cnh, categoria_cnh):
        self.numero_cnh = numero_cnh
        self.categoria_cnh = categoria_cnh

    def exibir_dados(self):
        return f"{self.nome} - CNH: {self.numero_cnh} - Categoria: {self.categoria_cnh}"


class ContratoLocacao:
    def __init__(self, data_inicio, data_termino_prevista, valor_total, status, cliente, veiculo, condutor):
        self.data_inicio = data_inicio
        self.data_termino_prevista = data_termino_prevista
        self.valor_total = valor_total
        self.status = status
        self.cliente = cliente
        self.veiculo = veiculo
        self.condutor = condutor

    def finalizar(self):
        self.status = "finalizado"

    def cancelar(self):
        self.status = "cancelado"


class Manutencao:
    def __init__(self, data, tipo_servico, custo):
        self.data = data
        self.tipo_servico = tipo_servico
        self.custo = custo

    def registrar(self):
        print(f"Manutenção registrada: {self.tipo_servico}")

    def exibir_dados(self):
        return f"{self.data} - {self.tipo_servico} - R$ {self.custo:.2f}"


if __name__ == "__main__":
    cliente = PessoaFisica("Maria Souza", "000.000.000-00", "(86) 99999-9999")
    veiculo = Carro("ABC1D23", "Sedan", 2025, 150.00, 4)
    condutor = Condutor("João Silva", "12345678900", "B")

    contrato = ContratoLocacao(
        "05/10/2026", "10/10/2026", 750.00, "ativo",
        cliente, veiculo, condutor
    )

    print("Cliente:", contrato.cliente.exibir_dados())
    print("Veículo:", contrato.veiculo.exibir_dados())
    print("Condutor:", contrato.condutor.exibir_dados())
    print("Status:", contrato.status)

    contrato.finalizar()
    print("Status após finalização:", contrato.status)
