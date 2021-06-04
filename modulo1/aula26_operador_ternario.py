

logged_user = True

if logged_user:
    print("Olá, usuario logado!")
else:
    print("Usuario precisa logar")

#operador ternario

idade = 18
e_maior = (idade >=18)
msg = 'Pode acessar' if(e_maior) else 'Não pode'
print(msg)

if idade >= 18:
    print("pode acessar")
else:
    print('Não pode acessar')