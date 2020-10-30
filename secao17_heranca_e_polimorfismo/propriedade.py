"""
POO - Propriedades - Properties

Em linguagens de programaão como Java, ao declararmos atributos privados nas classes
costumamos a criar métodos públicos para manipulação desses atributos. Esses métodos
são conheciso por getters e setters, onde os getters retornam o valor dos atributos
e os setters alteram o valor deles

class Conta:
    contador = 0

    def __init__(self, titular, saldo, limite):
        self.__numero = Conta.contador + 1
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        Conta.contador += 1

    def extrato(self):
        print(f'Saldo de {self.__saldo} do titular {self.__titular} com limite de {self.__limite}')

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
        else:
            print('O valor precisa ser positivo')

    def sacar(self, valor):
        if valor > 0:
            if self.__saldo >= valor:
                self.__saldo -= valor
            else:
                print('Saldo insuficiente')
        else:
            print('O valor deve ser positivo')

    def transferir(self, valor, conta_destino):
        # 1 - Remover valor conta de origem
        self.__saldo -= valor

        # 2 - Adicionar o valor na conta de destino
        conta_destino.__saldo += valor

    def get_numero(self):
        return self.__numero

    def set_numero(self, numero):
        self.__numero = numero

    def get_titular(self):
        return self.__titular

    def set_titular(self, titular):
        self.__titular = titular

    def get_saldo(self):
        return self.__saldo

    def set_saldo(self, saldo):
        self.__saldo = saldo

    def get_limite(self):
        return self.__limite

    def set_limite(self, limite):
        self.__limite = limite


conta1 = Conta('Luan', 3000, 5000)
conta2 = Conta('Fernandes', 2000, 4000)

conta1.extrato()
conta2.extrato()

soma = conta1.get_saldo() + conta2.get_saldo()
print(f'A soma do saldo das contas é: {soma}')

print(conta1.__dict__)
conta1.set_limite(99999)
print(conta1.__dict__)


"""


class Conta:
    contador = 0

    def __init__(self, titular, saldo, limite):
        self.__numero = Conta.contador + 1
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        Conta.contador += 1

    @property
    def numero(self):
        return self.__numero

    @property
    def titular(self):
        return self.__titular

    @property
    def saldo(self):
        return self.__saldo

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, novo_limite):
        self.__limite = novo_limite

    def extrato(self):
        print(f'Saldo de {self.__saldo} do titular {self.__titular} com limite de {self.__limite}')

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
        else:
            print('O valor precisa ser positivo')

    def sacar(self, valor):
        if valor > 0:
            if self.__saldo >= valor:
                self.__saldo -= valor
            else:
                print('Saldo insuficiente')
        else:
            print('O valor deve ser positivo')

    def transferir(self, valor, conta_destino):
        # 1 - Remover valor conta de origem
        self.__saldo -= valor

        # 2 - Adicionar o valor na conta de destino
        conta_destino.__saldo += valor

    @property
    def valor_total(self):
        return self.__saldo + self.__limite


conta1 = Conta('Luan', 3000, 5000)
conta2 = Conta('Fernandes', 2000, 4000)

conta1.extrato()
conta2.extrato()

soma = conta1.saldo + conta2.saldo
print(f'A soma do saldo das contas é: {soma}')

print(conta1.__dict__)
conta1.limite = 76543
print(conta1.__dict__)

print(conta1.valor_total)
print(conta2.valor_total)