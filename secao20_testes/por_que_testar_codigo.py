"""


Testes automatizados!

        Aplicação web
---------------------------------
|       frontend e backend       |
|________________________________|
|   testes automatizados         |
|________________________________|

Por que testar código?
    - Reduzir bugs (problemas) no código existente;
    - Testes garantem que novos rcursos da sua alpicação não quebrem (alterem recursos antigos;
    - Testes garantem que bugs (problemas) que foram corrigidos anteriormente continuem corrigidos;
    - Testes garantem que a refatoração que costumamamos fazer não tragam novos bugs (problemas).


TDD - Test Driven Development (Desenvolvimento GUiado Por Testes)
 Com TDD é utilizado estágio de desenvolvimewnto:
    - Você escreve seu teste primeiro;
    - Estão você escrve o código mínimo suficiente para afzer o teste passar (ou seja, executar com sucesso);
    - Etão refatoa o código para realizar a funcionalidade e testa novamente;
    - Uma vez que o teste passa, o recurso é considerado completo

Estes estágios do desenvolvimento do TDD são quase um mantra que os desenvolvedores seguem, conhecidos como:
    - Red;
    - Green;
    - Refactor;
"""


class Gato:
    def __init__(self, nome):
        self.__nome = nome

    @property
    def nome(self):
        return self.__nome

    def miar(self):
        print(f'{self.__nome} está miando ...')


felix = Gato('Felix')
felix.miar()
print(felix.nome)
