"""
Entendendo o args
    - É um aprâmetro como outro qualqwuer. Isso significa que vc poderá chamar de qualquer coisa,
desde que comece com asterisco

Exemplo:
*xis

Mas por convenção, utilizamos *args para defini-lo

MAs o que é o *args?
O parâmetro args utilizado em uma função coloca os valores extras informados como entrada em uma tupla. Então desde já
lembre-se que tulpas são imutáveis

#Exemplos
def soma_todos_numeros(num1=1, num2=2, num3=3):
    return num1 + num2 + num3


print(soma_todos_numeros(4, 6, 9))

# print(soma_todos_numeros(4, 6)) # TypeError por excesso de argumentos



# Entendendo o *args

# Exmplo 1 -> For na tupla
def soma_todos_numeros(*args):
    total = 0
    for numero in args:
        total += numero
    return total


# Exemplo 2 -> Método sum de tupla
def soma_todos_numeros2(*args):
    return sum(args)


print(soma_todos_numeros(1, 200, 3, 4))
"""


# Outro exemplo de utilização de args

def verifica_info(*args):
    if 'Geek' in args and 'University' in args:
        return 'Bem-vindo Geek'
    return 'Eu não tenho certeza de quem você é...'


print(verifica_info())
print(verifica_info(1, True, 'University', 'Geek'))
print(verifica_info(1, 'University', 3.45))
