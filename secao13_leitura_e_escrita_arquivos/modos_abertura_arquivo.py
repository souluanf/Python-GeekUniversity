"""
https://docs.python.org/3.8/library/functions.html#open

Modos de Abertura de Arquivo

r -> Abre para leitura - padrão
w -> Abre para escrita - sobescreve caso já exista
x -> Abre para escrita somente se o arquivo não existir. Caso o arquivo exista. Ele dará FileExistsError
a -> Abre para escrita, adicionando o conteúdo ao final do arquivo SEMPRE. Nao controlamos o cursor neste modo
r -> Abre para o modo de atualização: Leitura e Escrita

# OBS: Abrindo no modo 'a' -> append, se o arquivo não existir será criado, caso exista, será adicionado ao final
try:
    with open('arquivos_txt/university.txt', 'x') as arquivo:
        arquivo.write('Teste de conteúdo. \n')
except FileExistsError as err:
    print(f'Arquivo já existe: {err}')


# Exemplo A
with open('arquivos_txt/frutas.txt', 'a') as arquivo:
    while True:
        fruta = input('Digite uma fruta ou digite sair: ')
        if fruta != 'sair':
            arquivo.write(fruta + '\n')
        else:
            break


"""

with open('arquivos_txt/outro.txt', 'r+') as arquivo:
    arquivo.seek(0)
    arquivo.write('No topo!\n')
    arquivo.write('Nova linha.\n')
    arquivo.write('Mais uma linha.\n')
