"""
Módulo Collections - Counter(Contador)
Collection -> High Performance Container Datetypes

Counter -> Recebe um interável como parâmetro e cria um objeto do tipo Collection que é parecido com um dicionário,
contendo como chave o elemento da lista passada como parâmetro e como valor a quantidade de ocorrências desse elemento.

from collections import Counter

# Podemos utilizar qualuqer iterável
#Ex 1
lista = [1, 1, 1, 2, 2, 3,3, 3, 1, 1, 2, 2, 1, 4, 4, 4, 5, 5, 5, 3, 45, 46, 47, 48, 42]

res = Counter(lista)

print(type(res))
print(res)
# Para cada elemento da lista, o Counter criou uma chave e colocou como valor a quantidade de ocorrencias

# Ex 2
print(Counter('Luan Fernandes'))

"""

from collections import Counter

# Ex 3
texto = """ Grajaú é um distrito do município de São Paulo, localizado na Zona Sul. 
É administrado pela subprefeitura da Capela do Socorro, dentro da região administrativa da Zona Sul de São Paulo.
Seus limites são os distritos de Pedreira, Grajaú Cidade Dutra, Parelheiros Grajaú e o município de São Bernardo
 do Campo e Diadema Grajaú
"""

palavras = texto.split()
res = Counter(palavras)
print(res)

# Mostrar quais aparecem mais em tops
print(res.most_common(5))
