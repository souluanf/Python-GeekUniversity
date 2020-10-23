""""
Mapas -> Conhecidos em Python como Dicionários

Dicionários em python são representados por chaves

receita = {'jan': 100, 'fev': 120, 'mar': 300}

# Interar sobre dicionários

print(receita)
for chave in receita:
    print(chave)

for chave in receita:
    print(receita[chave])

for chave in receita:
    print(f' Em {chave} recebi R${receita[chave]}')

# Acessando as chaves
print(receita.keys())  # REtorna dicionário de chaves
for chave in receita.keys():
    print(receita[chave])

# Acessando os valores
print(receita.values()) # Retorna dicionário de valores
for valor in receita.values():
    print(valor)

# Desempacotamento de dicionários
print(receita.items())  # Retorna dicionário de Itens
for chave, valor in receita.items():
    print(f'chave = {chave} e valor = {valor}')

# Soma, Máximo, Minimo, Tamanho -> Se os valores forem todos int ou float
print(sum(receita.values()))  # SOMA
print(max(receita.values()))  # MAXIMO
print(min(receita.values()))  # MINIMO
print(len(receita))  # TAMANHO

"""
