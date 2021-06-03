nome = input("Digite seu nome ")

if 0 < len(nome) <= 4:
    print(f"Seu {nome} nome é curto")
elif 4 < len(nome) < 7:
    print(f"Seu nome {nome} é normal")
else:
    print(f"Seu nome {nome} é muito grande!")