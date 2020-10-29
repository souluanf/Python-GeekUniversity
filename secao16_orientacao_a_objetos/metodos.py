"""
POO - Metodos
- Metodos (funções) -> Representam os comportamentos do objeto. Ou seja, as ações
que este objeto pode realizarr no seu sistema.

Em python, dividimos os métodos em 2 grupos:
    - Métodos de Instância
    - Métodos de Classe

# Métodos de Instância

# O método dunder init __init__() é um método especial chamado de construtor e
sua função é construir o objeto a partir da classe.

# OBS: Todo elemento em Python que inicia e finaliza em duplo underline é chamado de dunder(double underline)

#OBS: Os métodos/funções dunder em Python são chamados de métodos mágicos

ATENÇÃO! Por mais que possamos criar nossas próprias funções criando dunder não é aconselhado

# Métodos são escritos em letras minúsculas. Se o nome for composto, o nome terá a palavra separada pos underline

p1 = Produto('Playstation 4', 'Video Game', 2300)
print(p1.desconto(10))

user1 = Usuario('Luan', 'Fernandes', 'hello@luanfernandes.dev', '123456')
user2 = Usuario('Luccas', 'Silva', 'silva@Luccas.dev', '123457')

print(Usuario.nome_completo(user1))

print(user1.nome_completo())
print(user2.nome_completo())

print(f'Senha User 1 : {user1._Usuario__senha}')  # Acesso de forma errada de um atribto de classe
print(f'Senha User 2 : {user2._Usuario__senha}')  # Acesso de forma errada de um atribto de classe


nome = input('Informe o nome: ')
sobrenome = input('Informe o sobrenome: ')
email = input('Informe o email: ')
senha = input('Informe a senha: ')
confirma_senha = input('Confirme a senha: ')

if senha == confirma_senha:
    user = Usuario(nome, sobrenome, email, senha)
else:
    print('Senha não confere...')
    exit(42)

print('Usuário criado com sucesso!')

senha = input('Informe a senha para acesso: ')

if user.checa_senha(senha):
    print('Acesso permitido!')
else:
    print('Acesso negado!')

print(f'Senha Criptografada: {user._Usuario__senha}')  # Acesso errado

# Métodos de classe sao conhecidos como métodos estáticos em outras linguagens

# Metodos de classe

user = Usuario('Luan', 'Fernandes', 'hello@luanfernandes.dev', '123456')
# user2 = Usuario('Luccas', 'Silva', 'silva@Luccas.dev', '123457')
Usuario.conta_usuarios()  # Forma correta
user.conta_usuarios()  # Possivel, mas incorreta


"""


class Lampada:
    def __init__(self, cor, voltagem, luminosidade):
        self.__cor = cor
        self.__voltagem = voltagem
        self.luminosidade = luminosidade
        self.__ligada = False


class ContaCorrente:
    contador = 4999

    def __init__(self, limite, saldo):
        self.__numero = ContaCorrente.contador + 1
        self.__limite = limite
        self.__saldo = saldo
        ContaCorrente.contador = self.__numero


class Produto:
    contador = 0

    def __init__(self, nome, descricao, valor):
        self.__id = Produto.contador + 1
        self.__nome = nome
        self.__descricao = descricao
        self.__valor = valor
        Produto.contador = self.__id

    def desconto(self, porcentagem):
        """Retorna o valor do produto com o desconto """
        return (self.__valor * (100 - porcentagem)) / 100


from passlib.hash import pbkdf2_sha256 as cryp


class Usuario:
    contador = 0

    @classmethod
    def conta_usuarios(cls):
        print(f'Classe: {cls}')
        print(f'Temos {cls.contador} clientes no sistema')

    @classmethod
    def ver(cls):
        print('Teste')

    @staticmethod
    def definicao():
        return 'UX344'

    def __init__(self, nome, sobrenome, email, senha):
        self.__id = Usuario.contador + 1
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__email = email
        self.__senha = cryp.hash(senha, rounds=200000, salt_size=16)
        Usuario.contador = self.__id
        print(f'Usuário criado: {self.__gera_usuario()}')

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'

    def checa_senha(self, senha):
        if cryp.verify(senha, self.__senha):
            return True
        return False

    def __gera_usuario(self):
        return self.__email.split('@')[0]


# Método estático
print(Usuario.contador)
print(Usuario.definicao())

user = Usuario('Luan', 'Fernandes', 'hello@luanfernandes.dev', '123456')

print(Usuario.contador)
print(Usuario.definicao())
