"""
while /else

contadores
acumuladores

se utilizar break + else o else não executa.
o else só executa quando a condição for falsa.


"""
contador = 1
acumulador = 1
while contador <= 10:
    print(contador)
    acumulador = acumulador+contador
    contador +=1
else:
    print(acumulador)




