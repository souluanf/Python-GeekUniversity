"""
Utilizando Lambdas
Conhecidas por Expressoes Lambdas, ou simplesmente Lambdas, são funções sem nome, ou seja,
funções anônimas

# Função em Python
def funcao(x):
    return 3 * x + 1


print(funcao(7))

# Expressao Lambda
lambda x: 3 * x + 1
# Como utilizar a expressao lambda
calc = lambda x: 3 * x + 1

print(calc(7))

# podemos ter expressoes lambdas com multiplas antradas

nome_completo = lambda nome, sobrenome: nome.strip().title() + ' ' + sobrenome.strip().title()
print(nome_completo(' Luan', 'Fernandes'))

# Em funções Python podemos ter nenhuma ou várias entradas.  Em lambdas também

amar = lambda: 'Como não amar python'

uma = lambda x: 3 * x + 1
duas = lambda x, y: (x * y) ** 0.5
tres = lambda x, y, z: 3 / (1 / x + 1 / y + 1 / z)
# n = lambda x1,x2,...,xn: <expresao>


print(amar())
print(uma(6))
print(duas(5, 7))
print(tres(3, 6, 9))

# Se passarmos mais argumentos que parâmetros esperados teremos TypeError

# Exemplo

autores = ['Isaac Asimov', 'Ray Bradbury', 'Robert Heinlein', 'Arthur C. Clarck', 'Frank HErbert', 'Orsor Scott Card',
           'Douglas Adams', 'H.G. Wells', 'Leigh Brackett']

print(autores)

autores.sort(key=lambda sobrenome: sobrenome.split(' ')[-1].lower())

print(autores)

"""


# Função Quadrática
# f(x) = a * x ** 2 + b * x + c

def geradora_funcao_quadratica(a, b, c):
    """Retorna a função f(x) = a * x ** 2 + b * x + c"""
    return lambda x: a * x ** 2 + b * x + c


teste = geradora_funcao_quadratica(2, 3, -5)
print(teste(0))

print(geradora_funcao_quadratica(2, 3, -5)(2))


