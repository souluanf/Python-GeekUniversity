"""
Leitura de Arquivos

Para ler o conteúdo de um arquivo de um arquivo em Pyton, utilizamos a função integrada open(),
que literalmente significa 'abrir'.

open() -> Na forma mais simples de forma de utilização nós passamos apenas um parâmetro
de entrada, que neste caso é o caminho o arquivo a ser lido. Essa função retorna
um _io.TextIOWrapper e é com ele que trabalhamos então.

# OBS: Por padrão, a função open() abre o arquivo para leitura.
Este arquivo deve existir, ou então teremos o erro FileNotFoundError

<_io.TextIOWrapper name='exemplo.txt' mode='r' encoding='UTF-8'>

mode r - > Mode de Leitura. r -> red() -> ler

"""

arquivo = open('arquivos_txt/texto.txt')
# print(arquivo)
# print(type(arquivo))

# Para ler o conteúdo de uma rquivo , após sua abertura, devemos utilizar a função read()

ret = arquivo.read()
print(type(ret))


print(ret)

# O Python utiliza um recurso para trabalhar com arquivos chamado de cursor. Esse cursor
# funciona como cursor quando estamos escrevendo

# A função read() lê todo o conteúdo do arquivo
