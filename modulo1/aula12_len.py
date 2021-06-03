usuario = input("Digite seu usuario ")
qtd_caracteres = len(usuario)

print(usuario, qtd_caracteres, type(qtd_caracteres))

if len(usuario) < 6:
    print("O usuario deve ter 6 caracteres ou mais")
else:
    print("cadastrado com sucesso!")



