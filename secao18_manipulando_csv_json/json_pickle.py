"""
Json e Pickle

JSON -> Javascript Object Notation
API -> Meios de comunicação entre os serviços dodferecidos por empresas e terceiros

ret = json.dumps(['produto', {'Plastation 4 ': ('2TB', 'Novo', '2020V', 2340)}])
print(type(ret))
print(ret)

import json


class Gato:
    def __init__(self, nome, raca):
        self.__nome = nome
        self.__raca = raca

    @property
    def nome(self):
        return self.__nome

    @property
    def raca(self):
        return self.__raca


felix = Gato('Felix', 'Angora')

ret = json.dumps(felix.__dict__)
print(ret)

# Integrando o JSON com o Pickle

pip install jsonpickle

import jsonpickle


class Gato:
    def __init__(self, nome, raca):
        self.__nome = nome
        self.__raca = raca

    @property
    def nome(self):
        return self.__nome

    @property
    def raca(self):
        return self.__raca


felix = Gato('Felix', 'Angora')

ret = jsonpickle.encode(felix)

print(ret)

# Escrevendo o arquivo json/picke
import jsonpickle


class Gato:
    def __init__(self, nome, raca):
        self.__nome = nome
        self.__raca = raca

    @property
    def nome(self):
        return self.__nome

    @property
    def raca(self):
        return self.__raca


felix = Gato('Felix', 'Angora')

with open('arquivos/felix.json', 'w') as arquivo:
    ret = jsonpickle.encode(felix)
    arquivo.write(ret)


"""
# Lendo o arquivo json/picke
import jsonpickle


class Gato:
    def __init__(self, nome, raca):
        self.__nome = nome
        self.__raca = raca

    @property
    def nome(self):
        return self.__nome

    @property
    def raca(self):
        return self.__raca


# felix = Gato('Felix', 'Angora')

with open('arquivos/felix.json', 'r') as arquivo:
    conteudo = arquivo.read()
    ret = jsonpickle.decode(conteudo)
    print(ret)
    print(type(ret))
    print(ret.nome)
    print(ret.raca)
