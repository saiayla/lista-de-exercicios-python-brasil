"""
Exercício 01 da seção de estrutura de decisão da Python Brasil:
https://wiki.python.org.br/EstruturaDeDecisao

Faça um Programa que peça dois números e imprima o maior deles.

    >>> maior_de_dois_numeros(2,3)
    3
    >>> maior_de_dois_numeros(-1,-10)
    -1
    >>> maior_de_dois_numeros(-5,3)
    3
    >>> maior_de_dois_numeros(7,-14)
    7
"""


def maior_de_dois_numeros(x, y):
    """Escreva aqui em baixo a sua solução"""
    if x > y:
        print(x)
    elif y > x:
        print(y)
    else:
        print("Os dois números são iguais.")

while True:
    try:
        x = float(input("Insira um número: "))
        y = float(input("Insira outro número: "))
        break
    except ValueError:
        print("Insira um número válido!")
maior_de_dois_numeros(x, y)