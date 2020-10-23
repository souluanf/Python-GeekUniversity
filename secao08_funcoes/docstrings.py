"""
Documentando funções com docstrings
"""


# Exemplo

def diz_oi():
    """Uma função simples que retonr a string 'OI!' """
    return 'OI!'


def exponencial(numero, potencia=2):
    """
    Função que retorna por padrão o quadrado de 'número' ou o 'número' à potência informada
    :param numero: Número que desejamos gerar o exponencial
    :param potencia: Potência que queremos gerar o exponencial. Por padrão é 2.
    :return: Retorna o exponencial de 'número' por 'potência'
    """
    return numero ** potencia


print(help(exponencial))
