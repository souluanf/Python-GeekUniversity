"""
Módulo Collections - Named Tuple

# Recap Tupla:
tupla = (1, 2, 3)
print(tupla[1])

Named Tuple -> São tuplas deferenciadas onde  especificamos um nome para a mesma e ttabém parâmetros

"""
from collections import namedtuple

# Precisamos definir o nome e parâmetros

# Forma 1 = Declaração da tuple
cachorro1 = namedtuple('cachorro', 'idade raca nome')

# Forma 2 = Declaração da tuple
cachorro2 = namedtuple('cachorro', 'idade, raca, nome')

# Forma 3 = Declaração da tuple (Mais clara)
cachorro3 = namedtuple('cachorro', ['idade', 'raca', 'nome'])

# Usando
ray = cachorro1(idade=2, raca='Chow-Chow', nome='Ray')

# Acessando dados
# Forma 1
print(ray[0])
print(ray[1])
print(ray[2])

# Forma 2

print(ray.idade)
print(ray.raca)
print(ray.nome)

print(ray.index('Chow-Chow'))
print(ray.count('Chow-Chow'))