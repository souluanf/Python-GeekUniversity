"""
Funções de Maior Grandeza - Heigher Order Functions - HOF

O que significa ?

- Qunando uma linguagem de pogramação suporta HOF, indica que podemos ter funções
que retornam outras funções com resultado ou mesmo podemos passar funções
como argumentos para outras funções, e até msmo criar variáveiz do tipo de funções
nos nossos programas,.

OBS: Na seção de funções, nós utilizamos isso.

Em Python, as funções são Cidadão de Primeira Classe, First Class Citizen

# Exemplo definindo funções

def soma(a, b):
    return a + b


def diminuir(a, b):
    return a - b


def multiplicar(a, b):
    return a * b


def dividir(a, b):
    return a / b


def calcular(num1, num2, funcao):
    return funcao(num1, num2)


# Testando as funções
print(calcular(4, 2, soma))

print(calcular(4, 3, diminuir))

print(calcular(4, 3, multiplicar))

print(calcular(4, 3, dividir))


# Nested Function - Funções Aninhadas

# Em Python podemos ter funções dentro de funções, que são conhecidas por Nested Functions
# ou também Inner Functons (Funcções Internas)

# Exemplos

from random import choice


def cumprimento(pessoa):
    def humor():
        return choice(('E ai, ', 'Suma daqui, ', 'Gosto muito de você, '))
    return humor() + pessoa


# Testando
print(cumprimento('Marcella'))


# Retornando funções de outras funções

from random import choice


def faz_me_rir():
    def rir():
        return choice(('hahahahahaaha', 'kkkkkkkkkkkk', 'yayayayayayayaya'))

    return rir


# Testando
rindo = faz_me_rir()
print(rindo())


"""

# Inner  Functions ( Funções Internas/ Nested Functions) podem acessar o escopo de funções mais externas

from random import choice


def faz_me_rir_novamente(pessoa):
    def dando_risada():
        risada = choice(('hahahahahaha', 'kkkkkkkkkkkk', 'yayayayayaya', 'lolololololo', 'ksoskpsokspo'))
        return f'{risada} {pessoa}'

    return dando_risada


# Testando

rindo = faz_me_rir_novamente('Fernanda')
print(rindo())
print(rindo())
print(rindo())
