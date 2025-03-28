class Animal:
    def __init__(self, nome, especie, idade):
        # Atributos básicos do animal
        self.nome = nome
        self.especie = especie
        self.idade = idade

    def emitir_som(self):
        # Método genérico para emitir som, que pode ser sobrecarregado em subclasses
        print(f"{self.nome} está fazendo um som.")

    def dormir(self):
        print(f"{self.nome} está dormindo.")

    def comer(self):
        print(f"{self.nome} está comendo.")

    def __str__(self):
        # Método para representar o objeto como uma string
        return f"{self.nome} é um(a) {self.especie} de {self.idade} anos."

# Exemplo de uso da classe Animal
if __name__ == "__main__":
    # Criando um animal
    cachorro = Animal("Rex", "Cachorro", 5)
    
    # Exibindo informações do animal
    print(cachorro)
    
    # Chamando alguns métodos
    cachorro.emitir_som()
    cachorro.dormir()
    cachorro.comer()
