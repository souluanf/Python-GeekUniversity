"""
Sistemas de Arquivo e Navegação

Oara fazer uso de manipulação de arquivos do Sistema Operacional, precisamos importar
e fazer us do módulo os.

os -> Operating System - Sistema Operacional

# getcwd() -> pega o current work directory - diretório de trabalho absoluto
# Retorna o caminho absoluto
print(os.getcwd())

# Para mudar o diretório, podemos mudar o diretório o chdir()
os.chdir('..')
print(os.getcwd())

# Checar se diretório é absoluto ou relativo
print(os.path.isabs('/home/luan'))

import os

# Podemos identificar os istema operacional
print(os.name)  # posix(Linux e Mac), nt (Windows)

# Podemos ter mais detalhes no sistema operacional
print(os.uname())

import sys

print(sys.platform)

print(os.getcwd())
res = os.path.join(os.getcwd(), 'geek')

# Veja que o os.path.join() recebe dois parâmetros  , sendo o primeiro o diretório atual e o segundo o
# diretório que será juntado

# Podemos listar os diretórios com listdir()
print(os.listdir('/etc'))

"""

import os

# Podemos listar os  arquivos e diretórios com mais detalhes com scandir()
scanner = os.scandir('/etc')
arquivos = list(scanner)
# print(arquivos)
# print(dir(arquivos[0]))
print(arquivos[0].inode())  # Nome do arquivo
print(arquivos[0].is_dir())  # É um diretório? False
print(arquivos[0].is_symlink())  # É um link simbólico? False
print(arquivos[0].name)  # Nome do arquivo
print(arquivos[0].path)  # Caminho do arquivo
print(arquivos[0].stat())  # Estatísticas

# Quando utilizamos a função scandir() nós precisamos fecha-la,assim quando abrimos um arquivo
scanner.close()
