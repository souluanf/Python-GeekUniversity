"""
Reversed

Obs: Não confunda a função reverse() que estudamos nas listas.

A função reverse() só funciona em listas

Já a função reversed() funciona em qualquer iterável.

Sua função é inverter o iterável.

A função reversed() retorna um iteravel chamado List Reverse Iterator
"""

# Exemplos

lista = [1, 2, 3, 4, 5]
res = reversed(lista)
print(res)
print(type(res))

# Podemos connverter o elemento retornado em ua Lista, Tupla ou Conjunto

# Lista
print(list(reversed(lista)))

# Tupla
print(tuple(reversed(lista)))

# OBS: Em conjuntos não definimos a ordem dos elementos
# Conjunto(Set)
print(set(reversed(lista)))

# Podemos iterar sobre o reversed()
for letra in reversed('Luan Fernandes'):
    print(letra, end='')

# Podemosfazer o mesmo sem o uso do for
print('')
print(''.join(list(reversed('Luan Fernandes'))))

# Fazendo isso com slice de strings
print('Luan Fernandes'[::-1])

# Podemos também utilizar o reversed() para fazer um loop for reverso
for n in reversed(range(0, 10)):
    print(n)

# Apesar que podemos fazer isso usando o próprio range()
for n in range(9, -1, -1):
    print(n)
