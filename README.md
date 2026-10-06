# Trabalho Prático 02 — Sistema de Gerenciamento de uma Locadora de Veículos

**Curso:** Análise e Desenvolvimento de Sistemas  
**Disciplina:** Coding  
**Turma:** Bloco II (2026.2)

## 1. Identificação das classes
1. Veiculo
2. Carro
3. Moto
4. Caminhao
5. Cliente
6. PessoaFisica
7. PessoaJuridica
8. ContratoLocacao
9. Condutor
10. Manutencao

## 2. Atributos e métodos

### Veiculo
Atributos: placa, modelo, ano, valor_diaria  
Métodos: calcular_diaria(), exibir_dados()

### Carro
Atributos: placa, modelo, ano, valor_diaria, quantidade_portas  
Métodos: calcular_diaria(), exibir_dados()

### Moto
Atributos: placa, modelo, ano, valor_diaria, cilindradas  
Métodos: calcular_diaria(), exibir_dados()

### Caminhao
Atributos: placa, modelo, ano, valor_diaria, capacidade_carga  
Métodos: calcular_diaria(), exibir_dados()

### Cliente
Atributos: nome_razao_social, documento, telefone  
Métodos: atualizar_telefone(), exibir_dados()

### PessoaFisica
Atributos: nome, cpf, telefone  
Métodos: atualizar_telefone(), exibir_dados()

### PessoaJuridica
Atributos: razao_social, cnpj, telefone  
Métodos: atualizar_telefone(), exibir_dados()

### ContratoLocacao
Atributos: data_inicio, data_termino_prevista, valor_total, status  
Métodos: finalizar(), cancelar()

### Condutor
Atributos: nome, numero_cnh, categoria_cnh  
Métodos: atualizar_cnh(), exibir_dados()

### Manutencao
Atributos: data, tipo_servico, custo  
Métodos: registrar(), exibir_dados()

## 3. Herança

Veiculo é a superclasse de Carro, Moto e Caminhao, pois os três compartilham placa, modelo, ano e valor da diária.

Cliente é a superclasse de PessoaFisica e PessoaJuridica, pois ambos representam tipos de clientes e compartilham informações básicas de cadastro.

## 4. Relacionamentos

- Veiculo → Carro/Moto/Caminhao: generalização/herança.
- Cliente → PessoaFisica/PessoaJuridica: generalização/herança.
- Cliente — ContratoLocacao: associação. O contrato está vinculado a exatamente um cliente.
- Veiculo — ContratoLocacao: associação. O contrato utiliza um veículo específico; o veículo existe independentemente do contrato.
- ContratoLocacao — Condutor: composição. O condutor só existe associado ao contrato e deixa de ter motivo para existir isoladamente se o contrato for excluído.
- Veiculo — Manutencao: agregação. Um veículo pode ter diversas manutenções e cada manutenção pertence a um único veículo.

## 5. Implementação parcial

Foi escolhida a relação de composição entre ContratoLocacao e Condutor.

O arquivo main.py demonstra como ContratoLocacao recebe uma instância de Condutor e mantém essa relação.

Para executar: python main.py.
