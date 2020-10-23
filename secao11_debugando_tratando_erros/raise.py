"""
Levantando os próprios erros com raise

raise -> Lança exceções

OBS:  O raise não é uma função, apenas uma palavra reservada.

Para simplificar, pense em raise, como sendo útil para que possamos criar nossas prórpias exceções e mensagens de erros

A forma geral de utilização é:

raise TipoDoErro('Mensagem de Erro')

# Exemplo real

def colore(texto, cor):
    if type(texto) is not str:
        raise TypeError('texto precisa ser uma string')
    if type(cor) is not str:
        raise TypeError('texto precisa ser uma string')
    print(f"O texto '{texto}' será impresso na cor '{cor}'")

colore('Luan', 'azul')

# Exemplo refatorado

def colore(texto, cor):
    cores = ('verde', 'amarelo', 'azul', 'branco')
    if type(texto) is not str:
        raise TypeError('texto precisa ser uma string')
    if type(cor) is not str:
        raise TypeError('texto precisa ser uma string')
    if cor not in cores:
        raise ValueError(f'A cor precisa ser uma entre {cores}')
    print(f"O texto '{texto}' será impresso na cor '{cor}'")


colore('Luan', 'verde')

OBS: O raise assim como o return, finaliza a função. Ou seja, nada após o raise é executado.

"""


# Exemplo real

def colore(texto, cor):
    cores = ('verde', 'amarelo', 'azul', 'branco')
    if type(texto) is not str:
        raise TypeError('texto precisa ser uma string')
    if type(cor) is not str:
        raise TypeError('texto precisa ser uma string')
    if cor not in cores:
        raise ValueError(f'A cor precisa ser uma entre {cores}')
    print(f"O texto '{texto}' será impresso na cor '{cor}'")


colore('Luan', 'verde')
