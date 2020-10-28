"""
Escevendo em Arquivos

# OBS: Ao abrir um arquivo para leitura, não podemos realizar a escrita nele, apenas ler.
Da mesma forma, se abrirmos um arquivo para escrita não podemos lê-lo, somente escrever.

# OBS: Ao abrir um arquivo para escrita, será criado um novo arquivo no sistema

Para escrevermos dados em um arquivo, após abrir o arquivo utilizamos a função write().
Esta função recebe uma strng como parâmetro, caso contrário, teremos TypeError

Abrindo um arquivo com o modo 'w', se o arquivo não existir sewrá criado, se não existir será criado,
se já existir será sobrescrito

# Exemplo de escrita - movo w - write (escrita)

# Forma tradicional de escrever em arquivo (não Pythônica)
arquivo = open('mais.txt', 'w')
arquivo.write('Escrever dados em arquivos é muito fácil.\n')
arquivo.write('Podemos colocar quantas linhas quisermos.\n')
arquivo.write('Esta é a útltima linha.')
arquivo.close()

# Forma Pythônica
with open('exemplo.txt', 'w') as arquivo:
    arquivo.write('Escrever dados em arquivos é muito fácil.\n')
    arquivo.write('Podemos colocar quantas linhas quisermos.\n')
    arquivo.write('Esta é a útltima linha.')


with open('geek.txt', 'w') as arquivo:
    arquivo.write('Geek ' * 1000)


"""

with open('arquivos_txt/frutas.txt', 'w') as arquivo:
    while True:
        fruta = input('Informe uma fruta ou digite sair: ')
        if fruta != 'sair':
            arquivo.write(fruta + '\n')
        else:
            break
