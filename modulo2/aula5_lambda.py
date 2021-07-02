a = lambda x, y: x * y


print(a(5,2))


lista = [
    ['Produtos 2 ', 23],
    ['Produtos 3 ', 33],
    ['Produtos 1 ', 53],
    ['Produtos 1 ', 13],
    ['Produtos 4 ', 43],
]
print(lista)
lista.sort()
print(lista)

lista.sort(key=lambda item: item[1], reverse=True)
print(lista)