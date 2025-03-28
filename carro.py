class Carro:
    def __init__(self, marca, modelo, ano, cor):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.cor = cor
        self.velocidade = 0

    def acelerar(self, incremento):
        self.velocidade += incremento
        print(f"O carro acelerou para {self.velocidade} km/h.")

    def frear(self, decremento):
        self.velocidade -= decremento
        if self.velocidade < 0:
            self.velocidade = 0
        print(f"O carro freou para {self.velocidade} km/h.")

    def exibir_informacoes(self):
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Ano: {self.ano}")
        print(f"Cor: {self.cor}")
        print(f"Velocidade atual: {self.velocidade} km/h")

# Função para criar um carro com dados do usuário
def criar_carro_usuario():
    marca = input("Digite a marca do carro: ")
    modelo = input("Digite o modelo do carro: ")
    ano = int(input("Digite o ano do carro: "))
    cor = input("Digite a cor do carro: ")
    return Carro(marca, modelo, ano, cor)

# Exemplo de uso
meu_carro = criar_carro_usuario()
meu_carro.exibir_informacoes()

meu_carro.acelerar(30)
meu_carro.frear(10)

meu_carro.exibir_informacoes()