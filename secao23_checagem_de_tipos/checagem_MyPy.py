"""
 1 - Usar Type Hintig em todas funções e métodos
 2 - mypy arquivo.py
"""


def cabecalho(texto: str, alinhamento: bool = True) -> str:
    if alinhamento:
        return f"{texto.title()}\n{'-' * len(texto)}"
    else:
        return f" {texto.title()} ".center(50, '#')


print(cabecalho('Geek University'))
print(cabecalho('Geek University', alinhamento=False))
print(cabecalho('Geek University', alinhamento=True))

"""
Vantagens:
    - Mypy avalia e checa erros;
    - melhor documentação do código;
    - Melhora funcionalidade da IDE para autocomplete e sugestões;
    - Detalhamento do código
"""
