"""
Len, Abs, Sum, Round

# Len

Len ()  -> retona o tamanho de itens de um iteravel
# só pra revisar

print(len('Luan Fernandes'))
print(len([1, 2, 3, 4, 5]))
print(len((1, 2, 3, 4, 5)))
print(len({1, 2, 3, 4, 5}))
print(len({'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}))
print(len(range(0, 10)))

# Por debaixo dos panos, quando utilzamos a função len() o Pyton faz o seguinte:

# Dunder len
print('Luan Fernandes'.__le__())

# Abs

abd () - > Ela retona o valor absoluto de um numero inteiro de um numero ou ral. De forma básica, seria o seu valor real sem sinal.

# Exemplo abs

print(abs(-5))
print(abs(5))
print(abs(3.14))
print(abs(-3.14))

Sum

sum() - > Recebe como parâmetro um iretavel, podendo receber um valor inicial, e retorna a soma total dos elementos, incluindo o valor inicial.
OBS: O valor inicial default =  0

# Exemplo Sum

print(sum([1, 2, 3, 4, 5]))
print(sum([1, 2, 3, 4, 5], 5))

print(sum([3.145, 5.678]))

print(sum((1, 2, 3, 4, 5)))
print(sum({1, 2, 3, 4, 5}))
print(sum({'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}.values()))

# Round

round() ->  Retorna um numero arredondado para n digito de precisão após a casa decimal. Se a precisão não for informada,
  retorna o inteiro mais próximo da entrada.

"""

# Exemplo Round

print(round(10.2))
print(round(10.5))
print(round(10.6))
print(round(1.2121212121, 2))
print(round(1.21999999, 2))
