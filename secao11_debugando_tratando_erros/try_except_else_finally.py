"""
Try / Except / Else / Finally

Dica de quando e onde tratar código:

TODA ENTRADA DEVE SER TRATADA!

# Else -> É executado somente se não ocorrer o erro.
try:
    num = int(input('Informe um número: '))
except ValueError:
    print('Valor incorreto.')
else:
    print(f'Você digitou: {num}')

# Finally -> É executado somente se não ocorrer o erro.
try:
    num = int(input('Informe um número: '))
except ValueError:
    print('Você não digitou um valor válido.')
else:
    print(f'Você digitou: {num}')
finally:
    print('Executando o finally')

# OBS: O bloco finally é sempre executado, independente se houve exceção ou não
# O finally geralmente é utilizado geralmente utilizado para fechar ou desalocar recursos

# Exemplo mais complexo ERRADO

def dividir(a, b):
    return a / b


num1 = int(input('informe o primeiro número:'))
try:
    num2 = int(input('informe o segundo número:'))
except ValueError:
    print('O valor precisa ser numérico')

try:
    print(dividir(num1, num2))
except NameError:
    print('Valor incorreto')

# Exemplo mais complexo CORRETO
# OBS: VocÊ é responsável pelas enmtradas das suas funções, entãos trate-as

def dividir(a, b):
    try:
        return int(a) / int(b)
    except ValueError:
        return 'Valor incorreto'
    except ZeroDivisionError:
        return 'Não é possível realizar uma divisão por zero'


num1 = input('informe o primeiro número:')
num2 = input('informe o segundo número:')

print(dividir(num1, num2))

# Exemplo mais complexo Genérico
# OBS: VocÊ é responsável pelas enmtradas das suas funções, entãos trate-as

def dividir(a, b):
    try:
        return int(a) / int(b)
    except:
        return 'Ocorreu um problema'


num1 = input('informe o primeiro número:')
num2 = input('informe o segundo número:')

print(dividir(num1, num2))

"""


# Exemplo mais complexo Semi-Genérico
# OBS: VocÊ é responsável pelas enmtradas das suas funções, entãos trate-as

def dividir(a, b):
    try:
        return int(a) / int(b)
    except(ValueError, ZeroDivisionError) as err:
        return f'Ocorreu um problema: {err}'


num1 = input('informe o primeiro número:')
num2 = input('informe o segundo número:')

print(dividir(num1, num2))
