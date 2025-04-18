"""
Exercício 18 da seção de estrutura sequencial da Python Brasil:
https://wiki.python.org.br/EstruturaSequencial

Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps),
calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).
Arredonde o tempo em minutos

    >>> from secao_01_estrutura_sequencial import ex_18_tempo_de_download
    >>> numeros =['50', '2500']
    >>> ex_18_tempo_de_download.input = lambda k: numeros.pop()
    >>> ex_18_tempo_de_download.calcular_tempo_de_download()
    O tempo aproximado do Download é: 7 minuto(s)
    >>> numeros =['100', '2500']
    >>> ex_18_tempo_de_download.input = lambda k: numeros.pop()
    >>> ex_18_tempo_de_download.calcular_tempo_de_download()
    O tempo aproximado do Download é: 3 minuto(s)

"""


def calcular_tempo_de_download(mb, mbps):
    """Escreva aqui em baixo a sua solução"""
    tempo = round(mb/mbps)
    print(f"O tempo aproximado do Download é: {tempo} minuto(s)")

while True:
        try:
            mb = float(input("Tamanho do arquivo para download (em MB): "))
            mbps = float(input("velocidade do link de Internet (em Mbps): "))
            break
        except ValueError:
            print("Insira um valor válido!")
calcular_tempo_de_download(mb, mbps)
