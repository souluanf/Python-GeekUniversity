"""
Trabalhando com Módulos Builtin (módulos integrados, que já vem instalados no python)
________________________
|Python|Módulos Builtin|
------------------------

# Utilizando alias (apelidos) para módulos/ funções
import random as rdm
print(rdm.random())

# Podemos importar todas as funções de um módulos utilizando o *
from random import *
print(random())

# Importando todo o módulo
import random

print(random.random())

# Utilizando alias (apelidos) para módulos/ funções
from random import randint as rdi, random as rdm
print(rdi(5, 89))
print(rdm())

"""
# Costumamos a utilizar para colocar multiplos imports de um mesmo módulo
from random import (
    random,
    randint,
    shuffle,
    choice)

print(random())
print(randint(3, 7))
lista = ['l', 'u', 'a', 'n']
shuffle(lista)
print(lista)
print(choice('luan'))
