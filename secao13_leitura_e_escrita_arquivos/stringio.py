"""
StringIO

ATENÇÃO: Para ler ou escrever dados em arquivos do sistema operacional o software precisa ter permissão:
    - Permissão de Leitura -> Para ler arquivo
    - Permissão de escrita -> Para escrever arquivo

StringIO -> Utilizado para ler e criar arquivos em memória.
"""

# Primeiro fazemos import
from io import StringIO

mensagem = 'Esta é apenas uma string normal. '

# Podemos criar um arquivo em memória já com uma string inserida ou mesmo vazio para inserir texto depois
arquivo = StringIO(mensagem)
# arquivo = open('arquivo.txt','w')

# Agora tendo o arquivo, podemos utilizar tudo o que já sabemos
print(arquivo.read())

# Escrevendo outros textos
arquivo.write('Outro texto.')

# Podemos inclusive movimentar o cursor
arquivo.seek(0)

print(arquivo.read())
