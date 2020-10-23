def exponencial(numero, potencia=2):
    return numero ** potencia


def mostra_informacao(nome='Geek', instrutor=False):
    if nome == 'Geek' and instrutor:
        return f'Bem-vindo instrutor {nome}'
    elif nome == 'Geek':
        return f'Eu pensei que você fosse instrutor {nome}'
    return f'Olá, {nome}'


print(mostra_informacao('Luan'))
