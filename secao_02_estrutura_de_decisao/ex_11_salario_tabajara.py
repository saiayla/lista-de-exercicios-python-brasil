"""
Exercício 11 da seção de estrutura de decisão da Python Brasil:
https://wiki.python.org.br/EstruturaDeDecisao

As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para desenvolver o programa que calculará os reajustes.
Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
  salários até R$ 280,00 (incluindo) : aumento de 20%
  salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
  salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
  salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
  o salário antes do reajuste;
  o percentual de aumento aplicado;
  o valor do aumento;
  o novo salário, após o aumento.

Mostrar valores monetários com duas casas decimais.

    >>> calcular_aumento(100)
    Salário atual: R$ 100.00
    Aumento porcentual: 20%
    Valor do aumento: R$ 20.00
    Novo salário: R$ 120.00
    >>> calcular_aumento(300)
    Salário atual: R$ 300.00
    Aumento porcentual: 15%
    Valor do aumento: R$ 45.00
    Novo salário: R$ 345.00
    >>> calcular_aumento(800)
    Salário atual: R$ 800.00
    Aumento porcentual: 10%
    Valor do aumento: R$ 80.00
    Novo salário: R$ 880.00
    >>> calcular_aumento(1600)
    Salário atual: R$ 1600.00
    Aumento porcentual: 5%
    Valor do aumento: R$ 80.00
    Novo salário: R$ 1680.00

"""


def calcular_aumento(salario: float):
    """Escreva aqui em baixo a sua solução"""
    if salario <= 280:
      percentual = 20
      aumento = 0.2 * 280
      novo_salario = salario + aumento
    elif 280 <= salario <= 700:
      percentual = 15
      aumento = 0.15 * 280
      novo_salario = salario + aumento
    elif 700 <= salario <= 1500:
      percentual = 10
      aumento = 0.1 * 280
      novo_salario = salario + aumento
    elif  salario >= 1500:
      percentual = 5
      aumento = 0.05 * 280
      novo_salario = salario + aumento
    print(f"Salário atual: R$ {salario}\nAumento porcentual: {percentual}%\nValor do aumento: R$ {aumento}\nNovo salário: R$ {novo_salario}")
      
while True:
  try:
    salario = float(input("Insira seu salário: R$"))
    break
  except ValueError:
    print("Insira um salário válido!")
calcular_aumento(salario)