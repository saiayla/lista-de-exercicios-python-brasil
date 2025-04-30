"""
Exercício 26 da seção de estrutura de decisão da Python Brasil:
https://wiki.python.org.br/EstruturaDeDecisao

Um posto está vendendo combustíveis com a seguinte tabela de descontos:

    Álcool:
    até 20 litros, desconto de 3% por litro
    acima de 20 litros, desconto de 5% por litro
    Gasolina:
    até 20 litros, desconto de 4% por litro
    acima de 20 litros, desconto de 6% por litro
Escreva um algoritmo que leia o número de litros vendidos,
o tipo de combustível (codificado da seguinte forma: A-álcool, G-gasolina),
calcule e imprima o valor a ser pago pelo cliente sabendo-se que o preço do litro da gasolina é R$ 2,50 o
preço do litro do álcool é R$ 1,90.

Mostre o restultado com duas casas decimais

    >>> calcular_abastecimento(10, 'A')
    '10 litro(s) de álcool custa(m): R$ 19.00. Com 3% de desconto, fica R$ 18.43'
    >>> calcular_abastecimento(20, 'A')
    '20 litro(s) de álcool custa(m): R$ 38.00. Com 3% de desconto, fica R$ 36.86'
    >>> calcular_abastecimento(30, 'A')
    '30 litro(s) de álcool custa(m): R$ 57.00. Com 5% de desconto, fica R$ 54.15'
    >>> calcular_abastecimento(10, 'G')
    '10 litro(s) de gasolina custa(m): R$ 25.00. Com 4% de desconto, fica R$ 24.00'
    >>> calcular_abastecimento(20, 'G')
    '20 litro(s) de gasolina custa(m): R$ 50.00. Com 4% de desconto, fica R$ 48.00'
    >>> calcular_abastecimento(30, 'G')
    '30 litro(s) de gasolina custa(m): R$ 75.00. Com 6% de desconto, fica R$ 70.50'

"""
def calcular_abastecimento(litros_de_combustivel: float, tipo_de_combustivel: str) -> str:
    """Escreva aqui em baixo a sua solução"""
    match(tipo_de_combustivel):
        case 'a'|'A':
            tipo_de_combustivel = 'álcool'
            preco = litros_de_combustivel * 1.9
            if litros_de_combustivel <= 20:
                d = '3%'
                desconto = 1.9 - (0.03 * 1.9)
                preco_desconto = preco - desconto
            elif litros_de_combustivel > 20:
                d = '5%'
                desconto = 1.9 - (0.05 * 1.9)
                preco_desconto = preco - desconto
                
        case 'g'|'G':
            tipo_de_combustivel = 'gasolina'
            preco = litros_de_combustivel * 2.5
            if litros_de_combustivel <= 20:
                d = '4%'
                desconto = 1.9 - (0.04 * 2.5)
                preco_desconto = preco - desconto
            elif litros_de_combustivel > 20:
                d = '6%'
                desconto = 1.9 - (0.06 * 2.5)
                preco_desconto = preco - desconto
        case _:
            print("Entrada inválida!")
                
    print(f"{litros_de_combustivel} litro(s) de {tipo_de_combustivel} custa(m): R$ {preco:.2f}. Com {d} de desconto, fica R$ {preco_desconto:.2f}")
    
while True:
    try:
        litros = int(input("Quantidade de litros vendidos: "))
        break
    except ValueError:
        print("Insira uma quantidade válida!")
        
combustivel = input("Qual o tipo de combustível foi vendido (A-álcool, G-gasolina)? ")
calcular_abastecimento(litros, combustivel)

