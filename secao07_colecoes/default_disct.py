"""
Módulo Collection - Default Dict

dicionario = {'curso': 'Programação em Python Essencial'}
print(dicionario)
print(dicionario['curso'])
print(dicionario['outro'])  # Key error

Default Disct -> Ao criar um dicionário, nós informamos um valor  default, podendo utilizar um lambda pra isso
esse valor será utilizado sempre que não houver um valor definido. Caso tentemos aceassar umaa chave que não existe
essa chave será criada e o valor default será atribuído

OBS: Lambdas são funções sem nome que podem ou não receber parâmetros de entrada e retornar valores
"""

from collections import defaultdict

dicionario = defaultdict(lambda: "-1")
dicionario['curso'] = 'Programação em Python Essencial'
print(dicionario['teste'])  # Keyerror nromalmente, mas neste caso ele atribuí default

