"""
Módulo Collections: Ordered Dict

# EM dicionário, a ordem de inserção dos elemtnos não é garantida
dicionario = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
print(dicionario)

for chave, valor in dicionario.items():
    print(f'chave={chave}:valor={valor}')


# OrderedDisct: É um dicionário que garante a ordem de inserção no dicionário
dicionario = OrderedDict({'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5})
for chave, valor in dicionario.items():
    print(f'chave={chave}:valor={valor}')

# Entrndendo a diferença entre dict e ordereddict

"""
from collections import OrderedDict

# Dicion´´ario Comum
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 2, 'a': 1}
print(dict1 == dict2)  # True-> Já que a ordem dos elementos nao importa para o dict

odict1 = OrderedDict({'a': 1, 'b': 2})
odict2 = OrderedDict({'b': 2, 'a': 1})
print(odict1 == odict2)  # False -> Ordem é importante no OrderedDict
