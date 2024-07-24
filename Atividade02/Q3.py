def listar_unicos_elementos(lista1, lista2):
    unicos_elementos = []
    for i in lista1:
        if i not in lista2:
            unicos_elementos.append(i)
    for i in lista2:
        if i not in lista1:
            unicos_elementos.append(i)
    return unicos_elementos


lista1 = []
lista2 = []

tamanho_lista1 = int(input("Digite o tamanho da primeira lista: "))

for i in range(tamanho_lista1):
    lista1.append(int(input(f"Digite o {i+1}º número: ")))

tamanho_lista2 = int(input("Digite o tamanho da segunda lista: "))

for i in range(tamanho_lista2):
    lista2.append(int(input(f"Digite o {i+1}º número: ")))

unicos_elementos = listar_unicos_elementos(lista1, lista2)

print("Elementos únicos das listas é: ", unicos_elementos)