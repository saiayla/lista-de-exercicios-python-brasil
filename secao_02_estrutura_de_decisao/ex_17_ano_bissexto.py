"""
Exercício 17 da seção de estrutura de decisão da Python Brasil:
https://wiki.python.org.br/EstruturaDeDecisao

Faça um Programa que peça um número correspondente a um determinado ano e em seguida informe se este ano é ou não
bissexto.
    >>> eh_ano_bissexto(400)
    True
    >>> eh_ano_bissexto(800)
    True
    >>> eh_ano_bissexto(2100)
    False
    >>> eh_ano_bissexto(2004)
    True
    >>> eh_ano_bissexto(2022)
    False

"""

def eh_ano_bissexto(ano: int):
    """Escreva aqui em baixo a sua solução"""
    if ano % 4 == 0:
        if ano % 100 == 0:
            if ano % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False
while True:
    try:
        ano = int(input("Insira um ano: "))
        algarismos = len(str(ano))
        
        if algarismos < 4:
            print("Insira um ano válido!")
        else:
            break
    except ValueError:
        print("Insira um ano válido!")
if eh_ano_bissexto(ano):
    print(f"{ano} é um ano bissexto.")
else:
    print(f"{ano} não é um ano bissexto.")