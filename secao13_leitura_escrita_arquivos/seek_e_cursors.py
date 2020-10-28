"""
Seek e Cursors

seek() -> É utiliozada para movimentar o cursos pelo arquivo.

arquivo = open('texto.txt')
print(arquivo.read())

# seek() -> A função seek() é tutilizada paraa  movimentação do cursor pelo arquivo.
# Ela recebe um parâmetro que indica onde queremos colocar o cursor
# Movimento o cursor pelo arquivo com a função seek()
arquivo.seek(0)
print(arquivo.read())

arquivo.seek(22)
print(arquivo.read())

arquivo = open('texto.txt')
# readline() -> função que lê o arquivo linha a linha.
ret = arquivo.readline()

print(type(ret))
print(ret.split())

# readlines ()
linhas = arquivo.readlines()
print(len(linhas))

# OBS: QUando abrimos um arquivo coma função open() é criada uma conexão  entre o arquivo
no disco do computador e o nosso programa. Essa conexão é chamada de streaming. Ao finalizar
os trabalhos com o arquivo devemos fechar essa conexão. Por isso utiizamos a funçaõ close()
Passos para se trabalahar com arquivos.


"""
# 1 - abrir
arquivo = open('arquivos_txt/texto.txt')

# 2 - trabalhar
print(arquivo.read())

print(arquivo.closed)  # verifica se o arquivo está aberto ou fechado

# 3 - fechar
arquivo.close()

print(arquivo.closed)

# print(arquivo.read())
# OBS: Se tentarmos manipular um arquivo após seu fecharmomento teremos um value ValueError


# Limitar conteúdo
arquivo = open('arquivos_txt/texto.txt')
print(arquivo.read(20))
