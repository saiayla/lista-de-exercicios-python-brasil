"""
Exercício 09 da seção de estrutura de decisão da Python Brasil:
https://wiki.python.org.br/EstruturaDeDecisao

Faça um Programa que leia três números e mostre-os em ordem decrescente.

    >>> ordenar_decrescente(2, 3, 5)
    5, 3, 2
    >>> ordenar_decrescente(10, 5.55, 7)
    10, 7, 5.55
    >>> ordenar_decrescente(20, 30, 17.62)
    30, 20, 17.62
    >>> ordenar_decrescente(7, 1, 15)
    15, 7, 1

"""

def ordenar_decrescente(x, y, z):
    """Escreva aqui em baixo a sua solução"""
    numeros = [x, y, z]
    numeros.sort(reverse=True)
    print(numeros)
    
while True:
    try:
        x = float(input("Digite o primeiro número: "))
        y = float(input("Digite o segundo número: "))
        z = float(input("Digite o terceiro número: "))
        break
    except ValueError:
        print("Insira um número válido!")
ordenar_decrescente(x, y, z)
