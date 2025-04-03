class Restaurante:
    def __init__(self):
        # Inicializa o menu e os pedidos
        self.menu = ["Pizza", "Hambúrguer", "Lasanha", "Salada", "Sopa"]
        self.pedidos = []
    
    # Função para adicionar um pedido
    def adicionar_pedido(self, prato, quantidade):
        if prato not in self.menu:
            print(f"O prato {prato} não está no nosso menu.")
        else:
            # Adiciona o pedido com prato e quantidade
            self.pedidos.append({"prato": prato, "quantidade": quantidade})
            print(f"Pedido de {quantidade} {prato}(s) adicionado.")
    
    # Função para ordenar os pedidos por quantidade (Bubble Sort Recursivo)
    def ordenar_pedidos_recursivo(self, n=None):
        if n is None:
            n = len(self.pedidos)
        
        # Caso base: quando a lista tiver tamanho 1 ou menos
        if n == 1:
            return
        
        # Comparação e troca de pedidos
        for i in range(n - 1):
            if self.pedidos[i]["quantidade"] < self.pedidos[i + 1]["quantidade"]:
                # Troca de pedidos
                self.pedidos[i], self.pedidos[i + 1] = self.pedidos[i + 1], self.pedidos[i]
        
        # Chamada recursiva para o próximo nível
        self.ordenar_pedidos_recursivo(n - 1)

    # Função para mostrar o menu do restaurante
    def mostrar_menu(self):
        print("Menu do Restaurante:")
        for prato in self.menu:
            print(f"- {prato}")
    
    # Função para mostrar os pedidos ordenados
    def mostrar_pedidos(self):
        if not self.pedidos:
            print("Não há pedidos.")
            return
        print("\nPedidos recebidos:")
        for pedido in self.pedidos:
            print(f"{pedido['quantidade']} {pedido['prato']}(s)")

# Função principal para interagir com o usuário
def main():
    restaurante = Restaurante()

    # Mostra o menu
    restaurante.mostrar_menu()

    # Recebe pedidos do usuário
    while True:
        prato = input("\nDigite o nome do prato (ou 'sair' para finalizar): ").capitalize()
        if prato.lower() == "sair":
            break
        quantidade = int(input(f"Digite a quantidade de {prato}: "))
        restaurante.adicionar_pedido(prato, quantidade)

    # Ordena os pedidos pela quantidade (Bubble Sort Recursivo)
    restaurante.ordenar_pedidos_recursivo()
    
    # Exibe os pedidos ordenados
    restaurante.mostrar_pedidos()

# Chama a função principal para rodar o programa
if __name__ == "__main__":
    main()
