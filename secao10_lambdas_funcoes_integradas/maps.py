"""
Map

Com maps fazemos mapeamento de valores para função.
import math


def area(r):
    # Calcula a áreaa de um circulo com raio 'r'
    # return math.pi * (r ** 2)


raios = [2, 5, 7.1, 0.3, 10, 44]

# Forma comum
areas = []
for r in raios:
    areas.append((area(r)))
print(areas)

# Forma 2 - Map
# Map é uma função que recebe dois parâmetros. O primeiro, a funlão, o segundo um iterável. Retorna um map object
areas = map(area, raios)
print(list(areas))

# Forma 3 - Map com lambda
print(list(map(lambda raio: math.pi * raio ** 2, raios)))

# OBS: Após utilizar a função map(), depois da primeira utilização do resultado ele zera

# para fixar map
# TEmos dados iteráveis:
# dados: a1,a2...,an
# Temos uma função:
# Funcao: f(x)
# Utilizamos a função map(f,dados), onde map irá mapear cada elemento dos dados e aplicar a função
# O map object : f(a1),f(a2),f(...),f(an)
"""
# Mais um exemplo

cidades = [('Berlim', 29), ('Cairo', 36), ('Buenos Aires', 19),
           ('Los Angeles', 26), ('Tokio', 27), ('Nova York', 28), ('Londres', 22)]

print(cidades)
# f = 9/5 * c +32
# Lambda


<<<<<<< HEAD



=======
>>>>>>> a64efccf2e9bdc33226f49ffc47daade6b92a20b
print(list(map(lambda dado: (dado[0], (9 / 5) * dado[1] + 32), cidades)))
