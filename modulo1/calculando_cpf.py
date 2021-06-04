cpf = '394.455.968-11'

cpf_parcial = cpf[0:11].replace('.', '')

print(cpf_parcial)
soma = 0
for p, r in enumerate(range(10, 1, -1)):
    print(f'{int(cpf_parcial[p])} X {r} = {int(cpf_parcial[p])*r}')
    soma = soma + (int(cpf_parcial[p]) * r)
    print(f'Soma total : {soma}')

print(soma)
conta_1 = 11-(soma % 11)
if conta_1 > 9:
    digito1 = 0
else:
    digito1 = conta_1

print(f"Conta 1  = { conta_1}")
cpf_parcial = cpf_parcial + str(digito1)

soma = 0
for p, r in enumerate(range(11, 1, -1)):
    print(f'{int(cpf_parcial[p])} X {r} = {int(cpf_parcial[p])*r}')
    soma = soma + (int(cpf_parcial[p]) * r)
    print(f'Soma total : {soma}')

digito2 = 11 - (soma % 11)
if digito2 > 9:
    digito2 = 0

cpf_parcial = cpf_parcial + str(digito2)
cpf = cpf.replace('.','')
cpf = cpf.replace('-','')
if cpf_parcial == cpf:
    print("CPF VALIDO")
else:
    print("CPF invalido!!!")