"""
O bloco try/except

Utilizamos o bloco try/except para tratar os erros que podem ocorrer no nosso código. Previnindo
assim que o programa pare de funcionar e o usuário receba mensagens de erro inesperadas.

A forma geral mais simples é:

try:
    //execuçao problematica
except:
    //o que deve ser feito caso dê problema

# Exemplo 1 - Tratamento de erro genérico

try:
    geek()
except:
    print('Deu algum problema')

# Exemplo 2 - Tratamento de erro genérico

try:
   len(5)
except:
    print('Deu algum problema')

OBS: Tratar erro de forma genérica não é a melhor forma de tratamento de erros. O ideal é sempre tratar
de forma especifica.

# Exemplo 3 - Tratamento erro especifico

try:
    geek()
except NameError:
    print('Você está utilizxando uam função inexistente')

# Exemplo 4 - Tratamento erro especifico

try:
    len(5)
except TypeError:
    print('Você está utilizxando uam função inexistente')

# Exemplo 5 - Tratamento erro especifico com detalhes do erro

try:
    len(5)
except TypeError as err:
    print(f'A aplicação gerou o seguinte erro: {err}')

# Podemos efetuar diverso tratamentos de erros de uam vez
try:
    # len(5)
    geek()
    # print('Luan'[9])
except NameError as erra:
    print(f'Deu NameError: {erra}')
except TypeError as errb:
    print(f'Deu TypeError: {errb}')
except:
    print('Deu um erro diferente')

"""


def pega_valor(dicionario, chave):
    try:
        return dicionario[chave]
    except KeyError:
        return None
    except TypeError:
        return None


dic = {"nome": "Luan"}

print(pega_valor(dic, "game"))
