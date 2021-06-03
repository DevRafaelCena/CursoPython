num1 = input("digite um numero ")
num2 = input('digite outro numero ')

# isnumeric isdigit isdecimal
# https://docs.python.org/3/library/stdtypes.html
# https://github.com/luizomf/check-numbers-python/blob/master/chk_numbers.py
if num1.isdigit() and num2.isdigit():
    num1 = int(num1)
    num2 = int(num2)

    print(num1+num2)
else:
    print("Impossivel converter , deve ser informado numeros")

