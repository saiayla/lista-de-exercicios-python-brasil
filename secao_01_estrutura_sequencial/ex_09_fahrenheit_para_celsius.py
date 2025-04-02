"""
Exercício 09 da seção de estrutura sequencial da Python Brasil:
https://wiki.python.org.br/EstruturaSequencial

Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
C = 5 * ((F-32) / 9)
Mostrar apenas valor inteiro da temperatura

    >>> from secao_01_estrutura_sequencial import ex_09_fahrenheit_para_celsius
    >>> ex_09_fahrenheit_para_celsius.input = lambda k: '0'
    >>> ex_09_fahrenheit_para_celsius.transformar_para_celsius()
    Essa temperatura é de -18 Celsius
    >>> ex_09_fahrenheit_para_celsius.input = lambda k: '70'
    >>> ex_09_fahrenheit_para_celsius.transformar_para_celsius()
    Essa temperatura é de 21 Celsius

"""


def transformar_para_celsius(F):
    """Escreva aqui em baixo a sua solução"""
    return  5 * ((F-32) / 9)

while True:
    try:
        F = float(input("Insira a temperatura em Fahrenheit: "))
        break
    except ValueError:
        print("Insira uma temperatura válida!")
C = transformar_para_celsius(F)
print(f"Essa temperatura é de {int(C)} Celsius")