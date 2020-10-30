"""
Lendo arquivos SCV
CSV - Comma Separated Values - Valors Separados Por Vírgula
Apesar do nome, podemos separar por:
    - Vírgula;
    - Ponto e vírgula;
    - Espaço/Tabulação.


# possível de se trabalhar, mas não é o deal. Trabalhoso
with open('arquivos/lutadores.csv', 'r') as arquivo:
    dados = arquivo.read()
    # print(type(dados))
    dados = dados.split(',')[2:]
    print(dados)

A linguagem Python possui duas formas diferentes para ler dados em arquivos CSV:
    - reader -> Permite que iteremos sobre as linhas do arquivo como listas;
    - DisctReader -> Permite que iteremos sobre as linhas do arquivo CSV como OrderedDicts
"""
# Reader

from csv import reader

with open('arquivos/lutadores.csv') as arquivo:
    leitor_csv = reader(arquivo)
    next(leitor_csv)  # pular cabeçalho
    for linha in leitor_csv:
        # Cada linha é uma lista
        print(f'{linha[0]} nasceu no(a)(s) {linha[1]} e mede {linha[2]} centímetros')

# DictReader

from csv import DictReader

with open('arquivos/lutadores.csv') as arquivo:
    leitor_csv = DictReader(arquivo)
    for linha in leitor_csv:
        # Cada linha é um OrderedDict
        print(f"{linha['Nome']} nasceu no(a)(s) {linha['País']} e mede {linha['Altura (em cm)']} centímetros")

# Com outro separador

with open('arquivos/lutadores.csv') as arquivo:
    leitor_csv = DictReader(arquivo, delimiter=',')
    for linha in leitor_csv:
        # Cada linha é um OrderedDict
        print(f"{linha['Nome']} nasceu no(a)(s) {linha['País']} e mede {linha['Altura (em cm)']} centímetros")
