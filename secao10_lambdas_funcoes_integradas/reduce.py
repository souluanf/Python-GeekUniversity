"""
Reduce

Obs: A partir da versão 3+ do Python,  afunção rereduce() não é mais integrada (built-in).
Agora temos que importar e utilizar esta função a partir do módulo functools

Guido van Rossum: "Utilize a função reduce se você realmente precisa dela. Em todo caso,
                   99% da vezes um loop for é mais legível"

Para entender o reduce()

# Imagine que você te uma coleção de dados:

dados = [a1,a2,a3,..., an]

# E você tem uma função que recebe dois parâmetros:

def funcao(x,y):
    return x * y

Assim como o map() e filter(), a função reduce() recebe dois parâmetros: a função e o iterável.

reduce(funcao,dados)

A função reduce() funciona da seguinte forma:
 Passo1: res1 = f(a1,a2) #Aplica a função nos dois primeiros elementos da coleção e guarda o resultado
 Passo2: res2 = f(res1,a3) # aplica a função passando resultado do passo1 mais o 3º elemento e guarda no res.

 Isso é repetido até o final
 Passo3: res3 = f(res2,a4)
 .
 .
 .
 Passo n: resn = f(resn,an)
Ou seja, em cada passo ele aplica a função passsando como argumento o resultado da aplicação anterior. No final,
reduce() irá retornar o resultado final

Alternativamente, poderíamos ver a função reduce() como:

função(funcao(funcao(a1,a2),a3),a4),...an)
"""

# Como funciona na prática ?
# Vamos utiliozar a função reduce para multiplicar todos os números de uma lista

from functools import reduce

dados = [2, 3, 4, 5, 7, 11, 13, 17, 19, 23, 29]

# Para utilizar reduce() nós precisamos de uma função que receba dois parâmetros
multi = lambda x, y: x * y

res = reduce(multi, dados)
print(res)

# Utilizando um loop normal
res = 1
for n in dados:
    res *= n

print(res)
