"""
Formatando valores com modificadores

:s = Texto (string)
:d = Inteiros (int)
:f = numeros de ponto flutuante (float)
:.(NÚMERO)f = quantidade de casas decimais (float)
:(CARACTERE)(> ou < ou ^)(QUANTIDADE)(TIPO - s, d ou f)
> = ESQUERDA
< = DIREITA
^ = CENTRO
"""
num1 = 10
num2 = 3
divisao = num1 / num2
print('{:.2f}'.format(divisao))
print(f'{divisao:.3f}')

nome = "Rafael Bezerra"
print(f'{nome:s}')

num_1 = 1
print(f'{num_1:0>10}')

num_2 = 1150
print(f'{num_2:0<10}')


nome2 = 'Rafael cena'
print(nome2.ljust(20, '#'))
print(nome2.lower())
print(nome2.upper())
print(nome2.title())
print(nome2.capitalize())