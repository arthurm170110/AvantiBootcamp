def encontrar_segundo_maior(lista):
    maior = lista[0]
    segundo_maior = lista[0]
    for elemento in lista:
        if elemento > maior:
            segundo_maior = maior
            maior = elemento
        elif elemento > segundo_maior:
            segundo_maior = elemento
        
    return segundo_maior


lista = []

tamanho_lista = int(input("Digite o tamanho da lista: "))

for i in range(tamanho_lista):
    lista.append(int(input(f"Digite o {i+1}º número: ")))

segundo_maior = encontrar_segundo_maior(lista)

print("Segundo maior elemento da lista é: ", segundo_maior)