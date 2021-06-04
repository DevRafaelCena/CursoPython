"""
split, join , enumerate em python
Split = dividir uma string
Join = juntar uma lista
Enumerate = enumerar elementos da listas - iteraveis
"""
string = "O Brasil é o pais do futebol, o Brasil é penta"

lista = string.split(' ')
lista_2 = string.split(',')
print(lista)
print(lista_2)

for valor in lista:
    print(lista.count(valor))

junto = ' '.join(lista)
print(junto)


#enumerate

for indice,valor in enumerate(lista):
    print(indice, valor, lista[indice])
