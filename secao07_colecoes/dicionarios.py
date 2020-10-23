"""
Dicionários:
    Dicionários são coleções do tipo 'chave/valor'
    São representados por chaves {}
    Chave e valor são separados por dois pontos 'chave:valor'
    Tanto chave como valor podem ser de qualquer tipo de dado
    Podemos misturar tipos de dados

Obs: Em algumas linguagens, os dicionários python são conhecidos por mapas

# Criação de dicionários

# Forma 1 - Mais comum
paises = {'br': 'Brasil', 'eua': 'EStados Unidos', 'py': 'Paraguai'}
print(paises)
print(type(paises))

# Forma 2 - menos comum
paises = dict(br='Brasil', eua='EStados Unidos', py='Paraguai')
print(paises)

# Acessando elementos
paises = {'br': 'Brasil', 'eua': 'Estados Unidos', 'py': 'Paraguai'}
# Forma 1 - Acessando via chave, da mesma forma que lista/tupla
print(paises['br'])
# Se tentar pegar algo que nao tem vai dar erro KeyError

# Forma 2 - Acessando via get - Recomendada
print(paises.get('eua'))
print(paises.get('ru'))  # Se não existir, traz None

paises = {'br': 'Brasil', 'eua': 'Estados Unidos', 'py': 'Paraguai', 'ru': 'Russia'}

pais = paises.get('br')

if pais:
    print(f'Encontrei o país: {pais}')
else:
    print('Não encontrei o país')
    print('br' in paises)
print('ru' in paises)

if 'ru' in paises:
    russia = paises['ru']
    print(russia)

# Podemos verificar se determinada chave se encontra em um dicionário
paises = {'br': 'Brasil', 'eua': 'Estados Unidos', 'py': 'Paraguai', 'ru': 'Russia'}
print('br' in paises)
print('ru' in paises)
print('Estados Unidos' in paises)

if 'ru' in paises:
    russia = paises['ru']
    print(russia)

# Podemos utilizar qualquer tipo de dado (int , float, str, boolean), inclusive list, tuple, dict, como chave de dict
# Tuplas são bastante interessantes para serem utiliozadas como chave de dicionários, pois as mesmas são imutaveis

localidades= {
    (35.6895,39.6917):'Escritório em Tókio',
    (40.7128, 74.0060): 'Escritório em New York',
    (37.7749, 122.4194):'Escritório em São Paulo'
}

print(localidades)
print(type(localidades))


# Como adicionar elementos dicionários
receita = {'jan':100, 'fev':120,'mar':300}

print(receita)
print(type(receita))

# Forma 1 - Mais comum
receita['abril'] = 350
print(receita)

# Forma 2
novo_dado = {'mai': 500}
receita.update(novo_dado)
print(receita)

# Atualizando dados dicionário

# Forma 1
receita['mai'] = 550
print(receita)

# Forma 1
receita.update({'mai': 600})
print(receita)
# Conclusão 2: A forma de add novos elementos ou atualizar dados em um dicionário é a mesma.
# Conclusão 2: Em dicionário não podemos ter chaves repetidas

# Remover dados de um dicionário
receita = {'jan': 100, 'fev': 120, 'mar': 300}
print(receita)
# Forma 1
retorno = receita.pop('mar')
print(retorno)
print(receita)
# OBS1: Precisamos sempre informar a chave caso nao encontre o elemento um key error é informado
# OBS2: Ao remeover um objeto, o valor deste objeto é sempre retornável

# Forma 2

del receita['fev']
# Não retorna valor
print(receita)
# Se a chave não existir, será gerada KeyError

# Imagine que você tem um comércio eletrônico, onde temos um carrinho de compras na qual adicionamos produtos

Carrinho de compras
    PRODUTO 2:
        - nome
        - quantidade
        - preço
    PRODUTO 2:
        - nome
        - quantidade
        - preço

# 1 - Poderíamos utilizar uma lista para isso? Sim
carrinho = []
produto1 = ['PlayStation 4', 1, 2300.00]
produto2 = ['God of War 4 4', 1, 150.00]
carrinho.append(produto1)
carrinho.append(produto2)
print(carrinho)
# Teríamos que saber o índice de cada elemento do carrinho

# 2 - Poderíamos utilizar uma tupla pra isso? Sim
produto1 = ('PlayStation 4', 1, 2300.00)
produto2 = ('God of War 44', 1, 150.00)
carrinho = (produto1, produto2)
print(carrinho)
# Teríamos que saber o índice de cada elemento do carrinho

# 3 - Poderíamos utilizar um dicionário pra isso? Sim

carrinho = []
produto1 = {'nome': 'Playstation 4', 'quantidade': 1, 'preco': 2300.00}
produto2 = {'nome': 'God of War 4', 'quantidade': 1, 'preco': 150.00}

carrinho.append(produto1)
carrinho.append(produto2)

print(carrinho)
# Desta forma, podemos adicionar e remover itens e ter informações mais precisas

# Métodos de dicionários
d = dict(a=1, b=2, c=3)

# Limpar o dicionário
print(d.clear())
"""

# Forma não usual de criar dict

outro = {}.fromkeys('a', 'b')
print(outro)

usuario = {}.fromkeys(['nome', 'pontos', 'email', 'profile'], 'desconhecido')
print(usuario)

# O método fromkeys() recebe dois parametros: intervalo e valor
# Ele vai gerar, para cada valor do iterável uma chave e irá atribuir a esta chave um valor informado

veja = {}.fromkeys('teste', 'valor')
print(veja)

range = {}.fromkeys(range(1, 11), 'novo')
print(range)
