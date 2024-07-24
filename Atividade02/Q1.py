def impares(lista):
    lista_impar = []
    for i in lista:
        if i % 2 != 0:
            lista_impar.append(i)
    return lista_impar


lista = []

tamanho_lista = int(input("Digite o tamanho da lista: "))

for i in range(tamanho_lista):
    lista.append(int(input(f"Digite o {i+1}º número: ")))

lista_impar = impares(lista)

print("Lista de números ímpares: ", lista_impar)

