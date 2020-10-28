"""
Sistema de Arquivos - Manipulação

# Descobrindo se um arquivo ou diretório existe

# Arquivo
print(os.path.exists('arquivos_txt/arquivo.txt'))
print(os.path.exists('arquivos_txt/frutas.txt'))

# Diretório
print(os.path.exists('arquivos_txt'))

# Criando arquivos
# Forma 1
open('arquivos_txt/teste.txt', 'w').close()

# Forma 2
open('arquivos_txt/teste.txt', 'a').close()

# Forma 3

with open('arquivos_txt/arquivo-teste.txt','w') as arquivo:
    pass

# Criando arquivos

try:
    os.mknod('arquivos_txt/arquivo-teste4.txt')
except FileExistsError as err:
    print(f"Erro ao criar arquivo: '{err.args[1]}'")

# OBS: Se você estiver utilizando Mac OS, pode haver um erro PermissionError
# OBS: Crinado um arquivo via mkmod() se o arquivo já existir teremos o erro FileExistsError

# Criando diretórios - unicos

#Path relativo
try:
    os.mkdir('arquivos_txt/templates')
except FileExistsError as err:
    print(f"Erro ao criar diretório: '{err.args[1]}'")

#Path Absoluto
try:
    os.mkdir('/home/luan/templates')
except FileExistsError as err:
    print(f"Erro ao criar diretório: '{err.args[1]}'")

# OBS: A função mkdir() cria um diretório se este não existir. Caso exista, teremos FileExistsError

try:
    os.mkdir('/etc/templates')
except PermissionError as err:
    print(f"Erro reportado: '{err.args[1]}'")

# Se não tiver permissão dará PermissionError

# Criando multi-diretórios (árvoe de diretórios
os.makedirs('arquivos_txt/templates/geek/university')

os.makedirs('arquivos_txt/templates2/novo2/outro2', exist_ok=True) # Ignora erros

# Diretórios
os.rename('exemplos/templates2/novo6', 'teste')
# OBS: Se o diretório não existir teremos um FileNotFoundError
# OBS: Se o diretório que queremos renomear não estiver vazio teremos um OSError

# Arquivos
os.rename('exemplos/templates2/novo2/outro2/exemplo.txt', 'exemplos/templates2/novo2/outro2/novo.txt')

# ATENÇÃO: AO deletarmos arquivos ou dietórios eles não vão para a lixeira
# Removendo arquivos
os.remove('exemplos/university.txt')

# OBS: Se você estiver no WIndows e o arquivo que for deletar estiver sendo usado por alguem voce terá um erro
# OBS: Caso arquivo ao exista teremos FileNotFoundError
# OBS: Caso forneça o caminho apena de pasta, terá erro IsADirectoryError

# Removendo diretórios vázios
os.rmdir('exemplos/templates2')

# OBS: Se o diretório não estiver vazio teremos um OSError e se no existir, teremos FileNotFoundError

# Removendo uma árvore de diretórios
for arquivo in os.scandir('exemplos/templates2'):
    print(f'- {arquivo.name}')
    if arquivo.is_file():
        os.remove(arquivo.path)

# Podemos remove uma árvore de diretórios vazios
os.removedirs('exemplos')
# OBS: Se algum dos diretórios contiver arquivos o processo para.

# ATENÇÃO! Ao pagar arquivos com Python eles não vão pra lixeira, les somem

# Importando a biblioteca send2trash
from send2trash import send2trash

send2trash('exemplos/cesta2.txt')  # Vai para a lixeira. Pode ser restaurado
# Se o arquivo não existir teremos OSError

# Trabalhando com arquivos e diretórios temporarios
import os
import tempfile

# Criando um diretório temporario
with tempfile.TemporaryDirectory() as tmp:
    print(f'Criei o diretório temporario em {tmp}')
    with open(os.path.join(tmp, 'arquivo_temporario.txt'), 'w') as arquivo:
        arquivo.write('Geek University.\n')
        input()

# Estamos criando um diretorio temporario, abrindo o mesmo  e dentro dele criando
# um arquivo para escrevermos  um texto. Fo final damos um input apenas para mantermos
# os arquivos temporarios 'vivos' dentro dos blocos with

#OBS: Possivelmente o código acima não irá funciona no Windows

"""

# Trabalhando com arquivos e diretórios temporarios
import os
import tempfile

# Criando um arquivo temporário
with tempfile.TemporaryFile() as tmp:
    tmp.write(b'Geek University\n')
    tmp.seek(0)
    print(tmp.read())

# Em arquivos temporários só conseguimos escrever bits. Por isso utilizamos b''
