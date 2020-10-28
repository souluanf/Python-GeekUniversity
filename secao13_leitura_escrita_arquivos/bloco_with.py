"""
Bloco with

Passo para se trabalhar com arquivos

# 1 - Abrimos arquivo
# 2 - Manipulamos arquivo
# 3 - Fechamos arquivo

O bloco with é utilizado para criat um contexto de trabalho onde os recursos utilizados são fechados após o bloco with
"""

# O bloco with - Forma Pythônica de manipular arquivos

with open('arquivos_txt/texto.txt') as arquivo:
    print(arquivo.readlines())
    print(arquivo.closed)

print(arquivo.closed)
