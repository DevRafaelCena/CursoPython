"""
funcoes
*args **kwargs
"""


def func(*args):
    n1, n2, n3, *n = args
    print(n1, n2, n3, n)


func(1, 2, 3, 4, 5, 6)
