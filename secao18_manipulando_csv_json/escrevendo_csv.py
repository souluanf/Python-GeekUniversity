"""
Escrevendo em arquivos CSV

reader()
writer()

writerow() -> Escreve  uma linha

from csv import writer

# writer() -> Gera um objeto para que possamos escrever em arquuivo CSV. Utilizamos o métodos
# writerow() para escrever cada linha. Esse método recebe uma lista.

with open('arquivos/filmes.csv', 'w') as arquivo:
    escritor_csv = writer(arquivo)
    filme = None
    escritor_csv.writerow(['Titulo', 'Gênero', 'Duração'])
    while filme != 'sair':
        filme = input('Informe o nome do filme: ')
        if filme != 'sair':
            genero = input('Informe o gênero: ')
            duracao = input('Informe a duração (em minutos): ')
            escritor_csv.writerow([filme, genero, duracao])

"""

# DictWriter

# OBS:  As chvaes do dicionário devem ser as mesmas utilizadas como cabeçao.
# Mesmo com as pontuações

from csv import DictWriter

with open('arquivos/filmes_dict.csv', 'w') as arquivo:
    cabecalho = ['Titulo', 'Gênero', 'Duração']
    escritor_csv = DictWriter(arquivo, fieldnames=cabecalho)
    escritor_csv.writeheader()
    filme = None
    while filme != 'sair':
        filme = input('Informe o nome do filme: ')
        if filme != 'sair':
            genero = input('Informe o gênero: ')
            duracao = input('Informe a duração (em minutos): ')
            escritor_csv.writerow({"Titulo": filme, "Gênero": genero, "Duração": duracao})
