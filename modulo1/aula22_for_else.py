

list = ['Rafael', 'Cena', 'Lucy']

for valor in list:
    print(valor)
    if valor == 'Cena':
        break

for valor in list:
    if valor.lower().startswith('c'):
        break
else:
    print("Não existe ")