"""
Introdução ao módulo Unittest

Unittest -> Testes Unitários

O que são testes unitários?

Teste é a forma de se testar unidades individuais de código fonte

Unidades individuais podem ser: funções, métodos, classes, métodos etc

# OBS: Teste unitário não é especifico da linguagem Python

Para criar nossos testes, criamos classes que heram de unitteste.TestCase
e a partit de então ganhamos todos os 'assertions' presentes no módulo

Para rodar os testes, utilizamos o unittest.main()

TesteCase -> Casos de teste para sua unidade

# Conhecendo as assertions

https://docs.python.org/3.8/library/unittest.html

assertEqual(a, b)            a == b
assertNotEqual(a, b)         a != b
assertTrue(x)                bool(x) is True
assertFalse(x)               bool(x) is False
assertIs(a, b)               a is b
assertIsNot(a, b)            a is not b
assertIsNone(x)              x is None
assertIsNotNone(x)           x is not None
assertIn(a, b)               a in b
assertNotIn(a, b)             a not in b
assertIsInstance(a, b)       isinstance(a, b)
assertNotIsInstance(a, b)    not isinstance(a, b)


Por convenção, todos os testes em um TesteCase deve ter seu nome iniciado com 'test_'

Para executar os testes com unittest

python nome_do_modulo.py

# Para executar os testes com unittest no modo verbose

python nome_do_modulo -v

# Docstrings nos testes

Podemos acrescentar (e é recomendado) docstrings nos nosso testes.
"""

# pratica - Utilizando a abodagem TDD
