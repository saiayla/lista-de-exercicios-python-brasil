"""
Exercício 18 da seção de estrutura de decisão da Python Brasil:
https://wiki.python.org.br/EstruturaDeDecisao

Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida.

    >>> validar_data('')
    'Data inválida'
    >>> validar_data('1')
    'Data inválida'
    >>> validar_data('1/2/2004')
    'Data válida'
    >>> validar_data('1/02/2004')
    'Data válida'
    >>> validar_data('01/02/2004')
    'Data válida'
    >>> validar_data('30/02/2004')
    'Data inválida'
    >>> validar_data('01/13/2004')
    'Data inválida'

"""
from datetime import datetime

def validar_data(data: str):
    """Escreva aqui em baixo a sua solução"""
    try:
        datetime.strptime(data, "%d/%m/%Y")
        return True
    except ValueError:
        return False

data = input("Insira uma data: ")

if validar_data(data):
    print("Data válida")
else:
    print("Data inválida")