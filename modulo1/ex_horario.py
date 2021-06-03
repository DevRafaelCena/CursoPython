horario = input("Quer horas são? ")


if horario.isdigit():
    horario = int(horario)
    if 0 < horario < 11:
        print(f"Bom dia são {horario} horas")
    elif 11 < horario < 17:
        print(f"Boa tarde, agora são {horario} horas")
    elif 17 < horario < 24:
        print(f"Boa noite , agora são {horario} horas")
    else:
        print("Horario incorreto!!!!!!")
else:
    print("Digite um valor numerico")
