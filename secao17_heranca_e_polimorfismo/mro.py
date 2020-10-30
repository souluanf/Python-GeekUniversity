"""
POO - MRO - Method Resolution Order

Method Resolution Order (Resolução de Ordem dos Métodos) é a ordem
de execução dos métodos (quem será executado primeiro)

Em Python, voce pode conferir a ordem de execução dos métodos(MRO) de 3 formas
    - via propriedade da classe __mro__
    - via método mro()
    - via help()
"""


class Animal:
    def __init__(self, nome):
        self.__nome = nome

    def cumprimentar(self):
        return f'Eu sou {self.__nome}'


class Aquatico(Animal):
    def __init__(self, nome):
        super().__init__(nome)

    def nadar(self):
        return f'{self._Animal__nome} está nadando.'

    def cumprimentar(self):
        return f'Eu sou {self._Animal__nome} do mar!'


class Terrestre(Animal):
    def __init__(self, nome):
        super().__init__(nome)

    def andar(self):
        return f'{self._Animal__nome} está andando.'

    def cumprimentar(self):
        return f'Eu sou {self._Animal__nome} da terra!'


class Pinguim(Aquatico, Terrestre):
    def __init__(self, nome):
        super().__init__(nome)


# Testando

tux = Pinguim('Tux')
print(tux.cumprimentar())

"""
Pinguim(Aquatico, Terrestre)
Eu sou Tux do mar!

Pinguim(Terrestre,Aquatico)
Eu sou Tux da terra!
"""
