"""
List Comprehension:
- Nós podemos gerar novas listas com dados processados a partir de
outro iterável.

# Sintaxe:
[dados for dado in iterável]

# Exemplos
numeros = [1, 2, 3, 4, 5]
print(numeros)

res = [numero * 10 for numero in numeros]
print(res)

'''
Para entender melhor o que está acontecendo devemos dividir a expressão em duas partes:
- A primeira parte: for numero in numero
- A segunda parte: numero * 10
'''

res2 = [numero / 2 for numero in numeros]
print(res2)


def funcao(valor):
    return valor * valor


res3 = [funcao(numero) for numero in numeros]
print(res3)

# List Comprehension VS LOOP
# LOOP
numeros_dobrados = []
for numero in [1, 2, 3, 4, 5]:
    numeros_dobrados.append(numero * 2)
print(numeros_dobrados)

# List Comprehension
print([numero * 2 for numero in [1, 2, 3, 4, 5]])

"""
# Outros Exemplos

# 1
nome = 'Luan Fernandes'
print([letra.upper() for letra in nome])

# 2
amigos = ['maria', 'julia', 'pedro', 'guilherme', 'vanessa']


def caixa_alta(nome):
    nome = nome.replace(nome[0], nome[0].upper())
    return nome


print([caixa_alta(amigo) for amigo in amigos])

# Simplificado
print([amigo.title() for amigo in amigos])

# 3
print([numero * 3 for numero in range(1, 11)])

# 4
print([bool(valor) for valor in [0, [], '', True, 1, 3.14]])

# 5
print([str(numero) for numero in [1, 2, 3, 4, 5]])

# Nós podemos adicionar estruturas condicionais lógicas
# Exemplos
# 1
numeros = [1, 2, 3, 4, 5, 6]
pares = [numero for numero in numeros if numero % 2 == 0]
impares = [numero for numero in numeros if numero % 2 != 0]
print(pares)
print(impares)
# Refatorar
# Qualquer numero par  por módulo de 2 é o 0 e o 0 em Python é False. not false = true
pares = [numero for numero in numeros if not numero % 2]
# Qualquer numero par  por módulo de 2 é 1. not false = true
impares = [numero for numero in numeros if numero % 2]

print(pares)
print(impares)

# 2

res = [numero * 2 if numero % 2 == 0 else numero / 2 for numero in numeros]
print(res)
