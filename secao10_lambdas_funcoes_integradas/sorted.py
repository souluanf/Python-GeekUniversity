"""
Sorted

OBS: Não confunda , apesar do nome, com a função sort() que já estudamos em listas. O sort() só funciona com listas.
Podemos utilizar sorted() com qualquer iterável

Como o próprio nome diz, sorted() serve para ordenar.

OBS: O sorted() SEMPRE retorna uma lista com os elementos do iterável ordenados

# Exemplo

numeros = (6, 1, 8, 2)
print(numeros)

print(sorted(numeros))  # Ordenar do menor para o maior

print(numeros)

# Adicionando parâmetros ao sorted()
numeros = [6, 1, 8, 2]
print(numeros)

print(sorted(numeros, reverse=True))  # Do maior para o menor

# Podemos utilizar o sorted() para coisas mais complexas

usuarios = [
    {"username": "samuel", "tweets": ["Eu adoro bolos", "Eu adoro pizzas"]},
    {"username": "carla", "tweets": ["Eu amo meu gato"]},
    {"username": "jeff", "tweets": []},
    {"username": "bobb123", "tweets": [], 'cor': 'amarelo'},
    {"username": "doggo", "tweets": ["Eu gosto de cachorros", "Vou sair hoje"]},
    {"username": "gal", "tweets": [], 'cor': 'amarelo', 'musica': 'rock'},
]

print(usuarios)

# Ordenando pelo username - Ordem alfabética
print(sorted(usuarios, key=lambda usuario: usuario['username']))

# Ordenando pelo número de tweets - Ordem alfabética
print(sorted(usuarios, key=lambda usuario: len(usuario['tweets'])))
"""

# Ultimo exemplo

musicas = [
    {"titulo": "Thunderstruck", "tocou": 3},
    {"titulo": "Dead Skin Mask", "tocou": 2},
    {"titulo": "Back in Black", "tocou": 4},
    {"titulo": "Too old to rock'in'roll, too young to die", "tocou": 32},
]

# Ordena da menos tocada para a mais tocada
print(sorted(musicas, key=lambda musica: musica['tocou']))

# Ordena da mais tocada para a menos tocada
print(sorted(musicas, key=lambda musica: musica['tocou'], reverse=True))
