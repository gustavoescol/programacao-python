fila = []

def add_pessoa():
    nome = input('Qual o seu nome: ')

    if len(fila) < 10:
        fila.append (__name__)
        print ("cadastro com sucesso")

   
    elif len(fila) > 10:
        print ("Fila cheia")

    else: print('ta na fila')

def chamada():
    pessoa = fila[0]
    print (f'chamando{pessoa}')
    fila.pop(0)

def exibir():
    print()

def menu():
    while True:
        print('digite 1 para adicionar nome')
        print('digite 2 para chamar')
        print('digite 3 para exibir a lista')

        opcao = int(input (">"))

        if opcao == 1:
         add_pessoa()

        elif opcao == 2:
            chamada()

        else: 
            exibir()

add_pessoa()