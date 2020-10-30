"""
Conhecendo o Pickle

A função do Picke é rewalizar o seguinte processo:
Objeto Pythob -> Binarização
Binarização -> Objeto Python

# OBS: O módulo Pickle não é seguro contra dados maliciosos e desta forma
não é recomendado trabalhar com arquivos pickle vindos de outras pessoas
que você não conheça ou de fontes desconhecidas
# Fazendo a escrita em arquivo Pickle
felix = Gato('Felix')
pluto = Cachorro('Pluto')

with open('arquivos/animais.pickle', 'wb') as arquivo:
    pickle.dump((felix, pluto), arquivo)
"""

import pickle


class Animal:

    def __init__(self, nome):
        self.__nome = nome

    @property
    def nome(self):
        return self.__nome

    def comer(self):
        print(f'{self.__nome} está comendo')


class Gato(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def miar(self):
        print(f'{self.nome} está miando...')


class Cachorro(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def latir(self):
        print(f'{self.nome} está latindo...')


# Fazendo a escrita em arquivo Pickle
# felix = Gato('Felix')
# pluto = Cachorro('Pluto')
#
# with open('arquivos/animais.pickle', 'wb') as arquivo:
#     pickle.dump((felix, pluto), arquivo)

# Fazer a leitura de dados em arquivo pickle

with open('arquivos/animais.pickle', 'rb') as arquivo:
    gato, cachoro = pickle.load(arquivo)
    print(f'O gato chama-se {gato.nome}')
    gato.miar()
    print(f'O tipo do gato é {type(gato)}')

    print(f'O gato chama-se {cachoro.nome}')
    cachoro.latir()
    print(f'O tipo do gato é {type(cachoro)}')
