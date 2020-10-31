"""
Doctests são testes que colocamos na docstring das funções/métodos do python

def soma(a, b):
    #soma os números a e b
   # >>> soma(1,2)
    3
   # >>> soma(4,6)
    10
    #
    return a + b

Para rodar um teste do doctest:

python -m doctest -v secao20_testes/doctests.py

Trying:
    soma(1,2)
Expecting:
    3
ok
1 items had no tests:
    doctests
1 items passed all tests:
   1 tests in doctests.soma
1 tests in 2 items.
1 passed and 0 failed.
Test passed.


"""


# Outro exemplo, aplicando o TDD

def duplicar(valores):
    """duplica os valores em uma lista

    >>> duplicar([1,2,3,4])
    [2, 4, 6, 8]
    >>> duplicar([])
    []
    >>> duplicar(['a','b','c'])
    ['aa', 'bb', 'cc']
    >>> duplicar([True,None])
    Traceback (most recent call last):
      ...
    TypeError: unsupported operand type(s) for *: 'int' and 'NoneType'
    """
    return [2 * elemento for elemento in valores]
