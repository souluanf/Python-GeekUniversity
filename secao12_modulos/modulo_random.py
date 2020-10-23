"""
Módulo random e o que são módulos?

- Em pythom, os módulos nada mais são do que  outros arquivos Python

Módulo Random  -> posssui várias funções para gerações de núemeros pseudo-aleatórios

# Forma 1 - importando todo o módulo (Não recomendado)
import random

# random() - >gera um numero real pseudo-aleatório entre 0-1
# Não confunda a função com o pacote

# Ao realizar todo o módulo , todas as funçõs, atributos, classes e propriedades que estiverem
# dentro do módulo ficarão disóníveis  (ficarão em memória). Caso você saiba quais funções você precisa utilizar
# deste módulo, então  esta não seria a forma ideal de utilização. Nós veremos a forma melhor na forma 2.

print(random.random())

# Forma 2 - Importando uma função especifica do módulo (Forma recomendada)
from random import random

# Estamos importando apenas a função do pacote

for i in range(10):
    print(random())


# uniform ->  Gerar um número real pseudo-aleatório entre os valores estabelecidos
from random import uniform

for i in range(10):
    print(uniform(5, 10))  # 10 não é incluído

# randint -> Gera valores inteiros pseudo-aleatórios entre os valores estabelecidos.
from random import randint

# Gerador de apostas para a mega-sega
for i in range(6):
    print(randint(1, 61), end=', ') # de 1 a 60


# choice() -> Mostra um valor aleatoŕio entre um iterável
from random import choice

jogadas = ['pedra', 'papel', 'tesoura']

print(choice(jogadas))
"""

# shuffle() -> Tem a função de embaralhar dados

from random import shuffle
cartas = ['K', 'Q', 'J', 'A', '2', '3', '4', '5', '6', '7', '8', '9', '10']
print(cartas)
shuffle(cartas)
print(cartas.pop())
