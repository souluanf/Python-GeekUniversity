"""
Assertions (Afirmações)

Em Python utilizamos a palavras reservada 'assert' para realizar simples afirmações
utilizadas nos testes
Utilizamos o 'assert' em uma expressão que queremos checar se é válida ou não.
Se a expressão for verdadeira,  retorna None e caso seja falsa levanta um erro
do tipo AssertionError

# OBS: Nós podemos especificar, opcionalmente, um segundo argumento ou mesmo uma
mensagem de erro personalizada

# OBS: A palabra 'assert' pode ser utilizada em qualquer função ou códgio nosso.
Não precisa ser exlusivamente nos testes.

Se um programa Python for executado com o programa -O, nenhum assertion
será válidado. Ou seja, todas as suas validades já eram
"""


def soma_numero_positivo(a, b):
    assert a > 0 and b > 0, 'Ambos números precisam ser positivos'
    return a + b


ret = soma_numero_positivo(2, 4)  # 6


# ret2 = soma_numero_positivo(2, -2)  # AssertionError

def comer_fast_food(comida):
    assert comida in [
        'pizza',
        'sorvete',
        'doce',
        'batata frita',
        'cachorro quente'
    ], 'A comida precisa ser fast food'
    return f'Eu estou comendo {comida}.'


comida = input('Informe a comida: ')
print(comer_fast_food(comida))

# ALERTA: Cuidado ao utilizar 'assert'
