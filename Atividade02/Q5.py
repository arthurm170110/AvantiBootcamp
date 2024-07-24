def ordenar_pelo_nome(lista):
    lista_ordenada = sorted(lista, key=lambda nome: nome[0])
    return lista_ordenada


lista = []

tamanho_lista = int(input("Digite o tamanho da lista: "))

for i in range(tamanho_lista):
    nome = str(input(f"Digite o {i+1}º nome: "))
    idade = int(input(f"Digite a idade de {nome}: "))
    lista.append((nome,idade))

lista_ordenada = ordenar_pelo_nome(lista)

print("Lista de pessoas ordenadas pelo nome: ", lista_ordenada)