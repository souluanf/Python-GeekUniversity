"""
Poo - Heranca Múltipla

Herança Multipla nada mais é que a possibilidade que uma classe herdar multiplas classes
fazendo com que a classe filha herde todos os atributos e métodos de todas as classes herdadas

# OBS: A Herança Multipla pode ser feita de duas maneiras:
    - Multiderivação Direta
    - Multiderivação Indireta

# Exemplo 1 - Multiderivação Direta

class Base1:
    pass


class Base2:
    pass


class Base3:
    pass


class Multiderivada(Base1, Base2):
    pass


# Exemplo 2 - Multiderivação Indireta

class Base1:
    pass


class Base2(Base1):
    pass


class Base3(Base2):
    pass


class Multiderivada(Base3):
    pass


# Não importa se a derivação é direta ou indireta. A classe que realizar a herança herdará
todos os atribtos e métodos da super classe

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

nemo = Aquatico('Nemo')
print(nemo.nadar())
print(nemo.cumprimentar())

taz = Terrestre('Taz')
print(taz.andar())
print(taz.cumprimentar())

tux = Pinguim('Tux')
print(tux.andar())
print(tux.nadar())
print(tux.cumprimentar())  # Eu sou Tux da terra! ??? Method Resolution Order - MRO

# Objeto é instância...

print(f'Tux é instância de Animal? {isinstance(tux,Animal)}')
print(f'Tux é instância de Pinguim? {isinstance(tux,Pinguim)}')
print(f'Tux é instância de Aquático? {isinstance(tux,Aquatico)}')
print(f'Tux é instância de Terrestre? {isinstance(tux,Terrestre)}')
print(f'Tux é instância de object? {isinstance(tux,object)}')