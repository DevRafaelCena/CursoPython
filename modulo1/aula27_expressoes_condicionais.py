nome = input('Qual o seu nome? ')

if nome:
    print(nome)
else:
    print("Voce nao digitou nada")

#com o operador or
print(nome or 'Voce não digitou nada!')

a = 0
b = None
c = False
e = []
f = {}
g = 'Luis'
h = 22

variavel = a or b or c or e or f or g or 22

print(variavel)