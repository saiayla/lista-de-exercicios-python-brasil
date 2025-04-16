"""
Exercício 07 da seção de estrutura de decisão da Python Brasil:
https://wiki.python.org.br/EstruturaDeDecisao

Faça um Programa que leia três números e mostre o maior e o menor deles.

    >>> calcular_maior_de_3_numeros(2,3, 5)
    Maior: 5
    Menor: 2
    >>> calcular_maior_de_3_numeros(-1, -10, -2)
    Maior: -1
    Menor: -10
    >>> calcular_maior_de_3_numeros(-5, 3, 0)
    Maior: 3
    Menor: -5
    >>> calcular_maior_de_3_numeros(7, -14, 15)
    Maior: 15
    Menor: -14
"""


def calcular_maior_de_3_numeros(x, y, z):
    """Escreva aqui em baixo a sua solução"""
    maior = max(x, y, z)
    menor = min(x, y, z)
    print(f"Maior: {maior}")
    print(f"Menor: {menor}")

while True:
    try:
        x = float(input("Digite o primeiro número: "))
        y = float(input("Digite o segundo número: "))
        z = float(input("Digite o terceiro número: "))
        break
    except ValueError:
        print("Insira um número válido!")
calcular_maior_de_3_numeros(x, y, z)
