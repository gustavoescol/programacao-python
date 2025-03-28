numero = []


for i in range(5):
    numero = int(input(f"Digite o proximo numero: "))
    numero.append(numero)

    numero.sort()

print("Números em ordem decrescente:", numero)
