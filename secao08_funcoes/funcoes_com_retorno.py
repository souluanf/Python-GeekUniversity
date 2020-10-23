"""
Funcções com retorno

# Em python quando uma funão não tem retorno é NOnw
"""


# Exemplo de Função
def quadrado_de_7():
    return 7 * 7


# Criamos uma variável para receber o retorno
ret = quadrado_de_7()
print(f'Retorno: {ret}')
print(f'Retorno: {quadrado_de_7() + 1}')


# Exemplo2

def nova_funcao():
    variavel = False
    if variavel:
        return 4
    elif variavel is None:
        return 3.2
    return 'b'


def outra_funcao():
    return 2, 3, 4, 5


from random import random


def jogar_moeda():
    # Gera um numero pseudo-randomico entre 0 e 1
    valor = random()
    if valor > 0.5:
        return 'Cara'
    return 'Coroa'


print(jogar_moeda())
