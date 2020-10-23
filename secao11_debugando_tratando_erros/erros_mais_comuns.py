"""
Erros mais comuns em Python

ATENÇÂO!!! É importante prestar atenção e aprender a ler as saídas de erros geradas pelas execução
do nosso código

Os Erros mais comuns:

1 - SysntaxError -> Ocorre quando o Python encontra um erro de sintaxe. Ou seja, você escreveu algo que o python
não reconhece como parte da linguagem

# Exemplo SyntaxError
a)
def funcao:
    print('Luan Fernandes')
b)
def = 1

c)
retun

2 - NameError -: Ocorre quando uma variável ou função não foi definida

# Exemplos NameError
a)
print(luan)

b)
teste()

3 - TypeError -> Ocorre quando uma função/operação/ação é aplicada a um tipo errado

Exemplos TypeError

a)
print(len(5))

b)
print('Luan'+[])

4- IndexError -> Ocorre quando tentamos acessar um elemento
Exemplos

a)
lista = ['Luan']
print(lista[2])

b)
lista = ['Luan']
print(lista[0][10])

5- ValueError -> ocorre quando uma função/operação built-in (integrado) recebe um argumento com tipo correto
mas valor inapropiado
Exemplos
a)
print(int('Geek'))

6 - KeyError - ocorre quando tentamos acessar um dict com uma chave que não existe
Exemplos

dic = {}
print(dic['luan'])

7 - AttibuteError -> ocorre quando uma variável não tem um atributo/ função
Exemplos

a)
tupla = (11,2,31,4)
print(tupla.sort())

8 - IdentantionError -> ocorre quando não respietamos a identação do python (4 epaços)
Exemplos
a)
def nova():
print()


"""
