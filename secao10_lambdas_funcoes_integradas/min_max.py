"""
Min e Max

max() -> Maior valor em um iteravel ou o maior valor de dois ou mais elementos


# Exemplos max
lista = [1, 8, 4, 99, 129]
print(max(lista))

tupla = (1, 8, 4, 99, 129)
print(max(tupla))

conjunto = {1, 8, 4, 99, 129}
print(max(conjunto))

dicionario = {'a': 1, 'b': 8, 'c': 4, 'd': 99, 'e': 34, 'f': 129}
print(max(dicionario))

dicionario = {'a': 1, 'b': 8, 'c': 4, 'd': 99, 'e': 34, 'f': 129}
print(max(dicionario.values()))

print(max(3, 34))

# Faça um programa que receba dois valores do usuario e mostre o maior
val1 = int(input('Informe o primeiro valor: '))
val2 = int(input('Informe o segundo valor: '))
print(max(val1, val2))

print(max(4, 67, 54))
print(max('a', 'ab', 'abc'))
print(max('a', 'b', 'c', 'd', 'g'))
print(max(3.145, 5.789))

print(max('Geek University'))

min() -> Menor valor em um iteravel ou o menor valor de dois ou mais elementos
# Exemplos min
lista = [1, 8, 4, 99, 129]
print(min(lista))

tupla = (1, 8, 4, 99, 129)
print(min(tupla))

conjunto = {1, 8, 4, 99, 129}
print(min(conjunto))

dicionario = {'a': 1, 'b': 8, 'c': 4, 'd': 99, 'e': 34, 'f': 129}
print(min(dicionario))

dicionario = {'a': 1, 'b': 8, 'c': 4, 'd': 99, 'e': 34, 'f': 129}
print(min(dicionario.values()))

print(min(3, 34))

# Faça um programa que receba dois valores do usuario e mostre o maior
val1 = int(input('Informe o primeiro valor: '))
val2 = int(input('Informe o segundo valor: '))
print(min(val1, val2))

print(min(4, 67, 54))
print(min('a', 'ab', 'abc'))
print(min('a', 'b', 'c', 'd', 'g'))
print(min(3.145, 5.789))

print(min('Geek University'))

# Outro exemplos

nomes = ['Arya', 'Samsom', 'Dora', 'Tim', 'Ollivander']

print(max(nomes))  # Tim
print(min(nomes))  # Arya

print(max(nomes, key=lambda nome: len(nome)))  # Ollivander
print(min(nomes, key=lambda nome: len(nome)))  # Tim

"""

musicas = [
    {"titulo": "Thunderstruck", "tocou": 3},
    {"titulo": "Dead Skin Mask", "tocou": 2},
    {"titulo": "Back in Black", "tocou": 4},
    {"titulo": "Too old to rock'in'roll, too young to die", "tocou": 32},
]

print(max(musicas, key=lambda musica: musica['tocou']))
print(min(musicas, key=lambda musica: musica['tocou']))

# DESAFIO: Imprima somente o título o titulo da música mais e menos tocada
print(max(musicas, key=lambda musica: musica['tocou'])['titulo'])
print(min(musicas, key=lambda musica: musica['tocou'])['titulo'])

# DESAFIO: Como encontrar música mais e menos tocada sem usar max() ou min() e lambda?
max = 0
for musica in musicas:
    if musica['tocou'] > max:
        max = musica['tocou']

for musica in musicas:
    if musica['tocou'] == max:
        print(musica['titulo'])

min = 99999
for musica in musicas:
    if musica['tocou'] < min:
        min = musica['tocou']

for musica in musicas:
    if musica['tocou'] == min:
        print(musica['titulo'])
