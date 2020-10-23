lista = ['a', 'b', 'c', 'd', 'e', 'c', 'a']
lista2 = [2, 87, 3, 5, 11]

if 'e' in lista:
    print('encontrei na posicao {0}'.format(lista.index('e')))

# Ordenar
lista2.sort()
print(lista2)

# Ordenação reversa
lista2.reverse()
print(lista2)

# Contar elementos
print(lista.count('c'))

# Adiconar elementos
lista.append('f')
print(lista)

# Adicionar uma lista (sublista)
lista.append(['g', 'h', 'i'])
print(lista)
if ['g', 'h', 'i'] in lista:
    print('Encontrei')

# Coloca cada elemento da lista como individual
lista.extend('geek')
print(lista)

# Inserir novo elemento na lista informando posição do indice
lista.insert(2, 'Novo Valor')
print(lista)

# Podemos juntar duas listas
lista.extend(lista2)
print(lista)

# Remover ultimo elemento de uma lista
''' POP remove ultimo elemento, mas também o retorna'''
lista5 = list('Geek University')
lista5.pop()
print(lista5)

# Podemos remover um elemento pelo indice
'''Os elementos a direira deste indice serão deslocados a esquerda'''
lista5.pop(2)
print(lista5)
