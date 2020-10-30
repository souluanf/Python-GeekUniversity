"""
POO - Herança (Inheritance)

A idéia de herança é de reaproveitar código . Também de extender classes.

OBS: Com a herança, a partir de uma classe existente, nos extendemos outra classe
que passa a herdar atributos e métodos da classe herdada.

Cliente
    - nome
    - sobrenome
    - cpf
    - renda
Funcionario
    - nome
    - sobrenome
    - cpf
    - matricula

Perguntar: Existe alguma entidade genérica suficiente para encapsular os atributos
e métodos comuns a outras entidades ?

class Cliente:

    def __init__(self, nome, sobrenome, cpf, renda):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf
        self.__renda = renda

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'


class Funcionario:

    def __init__(self, nome, sobrenome, cpf, matricula):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf
        self.__matricula = matricula

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'


cliente1 = Cliente('Angelina', 'Jolie', '321.321.654.21', 500)

funcionario1 = Funcionario('Luan', 'Fernandes', '321.321.654.21', 1234)

print(cliente1.nome_completo())
print(funcionario1.nome_completo())

OBS: QUando uma classe herda de outra classe ela herda todos os atributos e métodos da classe herdada
QUando uma classe herda de outra classe, a clase herdada é conhecidade por:
    [Pessoa]
    - Super Classe;
    - Classe Mãe;
    - Classe Pai;
    - Classe Base
    - CLasse Genérica
Quando uma classe herda de outra classe ela é chamada:
    [Cliente,Funcionario]
    - Sub Classe
    - Classe Filha
    - Classe Especifica

class Pessoa:
    def __init__(self, nome, sobrenome, cpf):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'


class Cliente(Pessoa):
    # Cliente herda de Pessoa

    def __init__(self, nome, sobrenome, cpf, renda):
        super().__init__(nome, sobrenome, cpf)
        self.__renda = renda


class Funcionario(Pessoa):
    # Funcionário herda de Pessoa

    def __init__(self, nome, sobrenome, cpf, matricula):
        super().__init__(nome, sobrenome, cpf)
        self.__matricula = matricula


cliente1 = Cliente('Angelina', 'Jolie', '321.321.654.21', 500)
funcionario1 = Funcionario('Luan', 'Fernandes', '321.321.654.21', 1234)

print(cliente1.nome_completo())
print(funcionario1.nome_completo())

print(cliente1.__dict__)
print(funcionario1.__dict__)

# Sobrescrita de Métodos (overriding
Ocorre quando reescrevemos/reimplementamos um método presente na super classe
em  classes filhas.

"""


class Pessoa:
    def __init__(self, nome, sobrenome, cpf):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'


class Cliente(Pessoa):
    # Cliente herda de Pessoa

    def __init__(self, nome, sobrenome, cpf, renda):
        super().__init__(nome, sobrenome, cpf)
        self.__renda = renda


class Funcionario(Pessoa):
    # Funcionário herda de Pessoa

    def __init__(self, nome, sobrenome, cpf, matricula):
        super().__init__(nome, sobrenome, cpf)
        self.__matricula = matricula

    def nome_completo(self):
        print(super().nome_completo())
        print(self._Pessoa__cpf)
        return f'Funcionário:  {self.__matricula} Nome: {self._Pessoa__nome}'


# Sobrescrita de Métodos (overriding

cliente1 = Cliente('Angelina', 'Jolie', '321.321.654.21', 500)
funcionario1 = Funcionario('Luan', 'Fernandes', '321.321.654.21', 1234)

print(cliente1.nome_completo())
print(funcionario1.nome_completo())
