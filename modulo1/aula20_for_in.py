"""
for in
Iterando strings com for

Função range(start=0,stop,step=1)
"""

texto = "Python"

for letra in texto:
    print(letra)

# for com contador
for n, letra in enumerate(texto):
    print(n, letra)

# range range(start=0,stop,step=1)
for numero in range(0, 10, 2):
    print(numero)

