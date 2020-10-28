"""
Decoradores (Decorators)

O que são decorator?
    - São funções
    - Envolvem outras funções e aprimora seus comportamentos
    - Também são exemplos de Higher Order Functions
    - Tem sintaxe própria própria, usando @ (Syntact Sugar/Açúcar Sintático)


# Decorator como funções (Síntaxe não reconmebtdada / Sem açúcar Sintático)

def seja_educado(funcao):
    def sendo():
        print('Foi um prazer conhecer você! ')
        funcao()
        print('Tenha um ótimo dia!')

    return sendo


def saudacao():
    print('Seja bem-vindo(a) à Geek University')

# Testando 1

saudacao()
teste = seja_educado(saudacao)
teste()



# Testando 2

def raiva():
    print('Eu te odeio! ')


raiva_educada = seja_educado(raiva)
raiva_educada()

# Decorator com Syntax Sugar

def seja_educado_mesmo(funcao):
    def sendo_mesmo():
        print('Foi um prazer conhecer você! ')
        funcao()
        print('Tenha um excelente dia!')

    return sendo_mesmo


@seja_educado_mesmo
def apresentando():
    print('Meu nome é Pedro')


# Testando
apresentando()


@seja_educado_mesmo
def dormir():
    print('Quero dormir')


dormir()


"""




