def primos(lista):
    lista_primo = []
    for i in lista:
        if i > 1:
            for j in range(2, i):
                if i % j == 0:
                    break
            else:
                lista_primo.append(i)
    return lista_primo


lista = []

tamanho_lista = int(input("Digite o tamanho da lista: "))

for i in range(tamanho_lista):
    lista.append(int(input(f"Digite o {i+1}º número: ")))

lista_primo = primos(lista)

print("Lista de números primos: ", lista_primo)