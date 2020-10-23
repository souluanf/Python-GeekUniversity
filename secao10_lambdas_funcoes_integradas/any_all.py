"""
Any e All

all() -> retorna True se todos os alementos do iterável são verdadeiros ou ainda se o iterável está vazio
any ->

# Exemplo all()

print(all([0, 1, 2, 3, 4]))  # TOdos os númeors são verdadeiros? False
print(all([1, 2, 3, 4]))  # TOdos os númeors são verdadeiros? True
print(all((1, 2, 3, 4)))  # TOdos os númeors são verdadeiros? True
print(all({1, 2, 3, 4}))  # TOdos os númeors são verdadeiros? True
print(all('Luan'))  # TOdos os númeors são verdadeiros? True

nomes = ['Carlos', 'Camila', 'Carla', 'Cassiano', 'Cristina']
print(all(nome[0] == 'C' for nome in nomes))  # Todos nomes começam com 'C'

# OBS: Um iterável vazio convertido em boolean é False, mas o all() entende como True
print(all([letra for letra in 'eio' if letra in 'aeiou']))


any() - > Retorna  True se qualquer elemento do iterável for verdadeiro. Se o iterável estiver vazio, retorna False
"""

print(any([0, 1, 2, 3, 4]))  # True
print(any([0, False, {}, (), []]))  # False

nomes = ['Carlos', 'Camila', 'Carla', 'Cassiano', 'Cristina', 'Vanessa']
print(any(nome[0] == 'C' for nome in nomes))
