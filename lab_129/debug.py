vetor_inteiros = []

for indice in range(5):
    valor = int(input(f"Digite um valor para a posicao [{indice}]: "))
    vetor_inteiros.append(valor)

for contador, valor in enumerate(vetor_inteiros):
    print(f"posição {contador} = {valor}")

    