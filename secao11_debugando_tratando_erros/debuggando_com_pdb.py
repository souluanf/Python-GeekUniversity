"""
Debuggando co PDB

PDB -> Python Debugger
# OBS: A utilização do print() para debugger é uma prática ruim

def dividir(a, b):
    print(f'a={a}, b={b}')
    try:
        return int(a) / int(b)
    except(ValueError, ZeroDivisionError) as err:
        return f'Ocorreu um problema: {err}'
print(dividir(4, 7))


# Existem formas mais profissionas de fazer esse 'debug', utilizando o debuger
# Em python, podemos fazer isso em diferentes IDEs, como o PyCharm ou utilizando
# o PDB - Python Debugger

# Exemplo com Pycharm
def dividir(a, b):
    try:
        return int(a) / int(b)
    except(ValueError, ZeroDivisionError) as err:
        return f'Ocorreu um problema: {err}'


print(dividir(4, 7))


# Exemplo com o PDB - Python Debugger
# Para utilizar o Python Debugger precisamos importar a bibliuoteca pdb e então utilizar a função set_trace()
# Comandos básicos PDB
# l (listar onde estamos no código)
# n (próxima linhas)
# p (imprime variáveis)
# c (continua execução - finaliza debug)

import pdb

nome = 'Anjelina'
sobrenome = 'Jolie'
pdb.set_trace()
nome_completo = nome + '___' + sobrenome
curso = 'Programação em Python: Essencial'
final = nome_completo + ' faz curso ' + curso
print(final)

# Exemplo com o PDB - Python Debugger - Exemplo 2
# Para utilizar o Python Debugger precisamos importar a bibliuoteca pdb e então utilizar a função set_trace()
# Comandos básicos PDB
# l (listar onde estamos no código)
# n (próxima linhas)
# p (imprime variáveis)
# c (continua execução - finaliza debug)


nome = 'Anjelina'
sobrenome = 'Jolie'
import pdb;pdb.set_trace()
nome_completo = nome + '___' + sobrenome
curso = 'Programação em Python: Essencial'
final = nome_completo + ' faz curso ' + curso
print(final)

# Por que utilizar este formato?
# O debug é utlizado durante o desenvolvimento. Costumamos utlizar todos os imports de bibliotecas
# no inicio do arquivo. Por isso ao invés de colocarmos o import do pdb no inicio do arquivo
# nós colocamos somente onde vamos debuggar, e ao finalizar já fazemos a remoção

# Exemplo com o PDB - Python Debugger - Exemplo 3
3
# Para utilizar o Python Debugger precisamos importar a bibliuoteca pdb e então utilizar a função set_trace()

# A partir do Python 3.7 não é mais necessário importar a biblioteca pdb, pois o comando de debug foi
# incorporado como função built-in(integrada) chamada breakpoint()

# Comandos básicos PDB
# l (listar onde estamos no código)
# n (próxima linhas)
# p (imprime variáveis)
# c (continua execução - finaliza debug)


nome = 'Anjelina'
sobrenome = 'Jolie'
breakpoint()
nome_completo = nome + '___' + sobrenome
curso = 'Programação em Python: Essencial'
final = nome_completo + ' faz curso ' + curso
print(final)


"""

# Exemplo com o PDB - Python Debugger - Exemplo 3
# Para utilizar o Python Debugger precisamos importar a bibliuoteca pdb e então utilizar a função set_trace()

# A partir do Python 3.7 não é mais necessário importar a biblioteca pdb, pois o comando de debug foi
# incorporado como função built-in(integrada) chamada breakpoint()

# Comandos básicos PDB
# l (listar onde estamos no código)
# n (próxima linhas)
# p (imprime variáveis)
# c (continua execução - finaliza debug)


nome = 'Anjelina'
sobrenome = 'Jolie'
breakpoint()
nome_completo = nome + '___' + sobrenome
curso = 'Programação em Python: Essencial'
final = nome_completo + ' faz curso ' + curso
print(final)