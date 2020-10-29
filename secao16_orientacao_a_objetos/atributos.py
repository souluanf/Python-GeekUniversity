"""
POO - Atributos

- Atributos -> Representam as caracterisaticas do bjeto. Ou seja, pleos atributos conseguimos
    representar computacionalmente os estados de um objeto.

Em python dividimos atributos em 3 grupos:
    - de instância;
    - de classe;
    - dinâmicos;

# Atributo de Instância: São atributos declarados dentro do metodos construtor

# OBS: Metodos Construtor: É um metodo especial utilizado para a construção do objeto

# Em Java, uma classe Lâmpad, incluindo os atributos ficaria mais ou menos:

class Lampada{
  private int voltagem;
  private String cor;
  private boolean ligada = false;

  public Lampada (int voltagem, String cor){
    this.voltagem = voltagem;
    this.cor = cor;
  }

  public int getVoltagem(){
    return this.voltagem;
  }


Em Python, por convenção, ficou estabelecido que todo atributo de uma classe é publico.
Ou seja, pode ser acessado em todo o projeto.

Caso queiramos demonstrar que determinado atributo deve ser tratado como privado, ou seja,
que deve ser acessedo/utilizado somente dentro da própria classe onde está declarado,
utiliza-se __ dulpo underscore no inicio de seu nome.

Iso é conhecido também como Name Mangling


# OBS: Lembre-se que isso é apenas uma convenção, ou seja. A linguagem python não
# vai impedir que façamos acesso aos atributos sinalizados fora da classe

# Exemplo

user = Acesso('user@gmail.com', '123456')

user.mostra_senha()
user.mostra_email()

# O que significa Atributos de Instância?

# Significa que ao criarmos instãncias/objetos de uma classe, todas as instâncias
# terão estes atributos

user1 = Acesso('user1@gmail.com', '123456')
user2 = Acesso('user2@gmail.com', '123456')

user1.mostra_email()
user2.mostra_email()

# Atribuos de Classe, são atributos, claro, que são declarados diretamente na clase, ou seja,
# fora do construtor. geralmente já inicializamos um valor, e este valor é compartilhado entre
# todas instâncias da classe. Ou seja, ao invés de cada instância da classe ter seus próprios
# valores como é o caso dos atributos de instância, com os atributos de classe todas as instâncias
# terão o mesmo valor para este atributo.


p1 = Produto('Playstation 4', 'Video Game', 2300)
p2 = Produto('Xbox 5', 'Video Game', 4500)

print(p1.valor)
print(p2.valor)

# OBS: Não precisamos criar uma instância de uma classe  para fazer acessso a um atributo de classe

print(Produto.imposto)  # ACesso correto de um atributo de classe

print(p1.id)
print(p2.id)

# Em linguagens como o Java, os atributos conhecidos como atributos de classe aqui em Python
# são chamados de atributos estáticos

"""


# Classe com Atributos de Instãncia Públcios

class Lampada:

    def __init__(self, voltagem, cor):
        self.__voltagem = voltagem
        self.__cor = cor
        self.__ligada = False


class ContaCorrente:

    def __init__(self, numero, limite, saldo):
        self.numero = numero
        self.limite = limite
        self.saldo = saldo


class Produto:

    def __init__(self, nome, descricao, valor):
        self.nome = nome
        self.descricao = descricao
        self.valor = valor


class Usuario:

    def __init__(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.senha = senha


# Atributos públicos e privados

class Acesso:
    def __init__(self, email, senha):
        self.email = email
        self.__senha = senha

    def mostra_senha(self):
        print(self.__senha)

    def mostra_email(self):
        print(self.email)


# Atributos de Classe


# Refatorar a classe Produto

class Produto:
    # Atributo de classe
    imposto = 1.05  # 0.05 % de imposto
    contador = 0

    def __init__(self, nome, descricao, valor):
        self.id = Produto.contador + 1
        self.nome = nome
        self.descricao = descricao
        self.valor = (valor * Produto.imposto)
        Produto.contador = self.id


#  Atributos Dinâmicos -> Um atributo de instância qu pode sewr criado em tempo de execução
# OBS: O atributo dinâmico será exclusivo da instância que o criou


p1 = Produto('Playstation 4', 'Video Game', 2300)
p2 = Produto('Arroz', 'Mercearia', 25)

# Criando um atributo dinâmico em tempo de execução
p2.peso = '5kg'  # Na classe produto não existe peso

# Deletando atributos

print(p1.__dict__)
print(p2.__dict__)

del p2.peso
del p2.descricao

print(p1.__dict__)
print(p2.__dict__)
