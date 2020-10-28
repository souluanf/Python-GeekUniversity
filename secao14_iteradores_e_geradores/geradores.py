"""
Geradores (Generators) são Iterators

# OBS: O contrário não é verdadeiro. Ou seja, nem todo uierator é um generator

Outras informações:
- Generators podem ser criados com funções geradoras;
- Funções geradoras utilizam a palavra reservada yield;
- Generators podem ser criados com Expresões Geradoras

Diferença entre Funções e Generator Functions (Funções Geradoras)
------------------------------------------------------------------------------
| Funções                            |  Generator Functions                   |
-------------------------------------------------------------------------------
| utilizam return                    |  utilizam yield                        |
-------------------------------------------------------------------------------
| retorna uma vez                    |  podem utilizar yield mukltplias vezes |
-------------------------------------------------------------------------------
| quando executada, retona um valor  | quando executada, retorna um generator |
------------------------------------------------------------------------------

# OBS: Uma Generator Function não é um Generator, ela gera um
gem = conta_ate(5)

# print(type(gem))
print(next(gem))
print(next(gem))
print(next(gem))
print(next(gem))
print(next(gem))

# Laço de repetição
for num in gem:
    print(num)

"""


# Exemplo Função Geradora (Generator Function)
def conta_ate(valor_maximo):
    contador = 1
    while contador <= valor_maximo:
        yield contador
        contador = contador + 1


# OBS: Uma Generator Function não é um Generator, ela gera um
gem = conta_ate(10)

print(next(gem))  # 1

print('Continua do segundo')

for num in gem:
    print(num)

