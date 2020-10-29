"""
POO - Classes

Em POO, Classes nada mais são que modelos dos objetos do mundo real representados computacionalmente

Imagine que você queira fazer um sistema para automatizar o controle das lampadas da sua casa.

Classses podem conter:
    - Atributos -> Representam as caracterisaticas do bjeto. Ou seja, pleos atributos conseguimos
    representar computacionalmente os estados de um objeto. No caso da lampada,
    possivelmente iríamos querer saber se a lampada é 110 ou 220 v, a cor, luminosidade etc.

    - Métodos (funções) -> Representam os comportamentos do objeto. Ou seja, as ações que este
    objeto pode realizar no seu sistema. No caso da lapada, por exemplo, um comportamento comum
    que muito provavelmente iríamos querer representar no nosso sistema é o de ligar e desligar
    o mesmo.

Em Python para definir uma classe utilizamos a palavra reservada class.

OBS: utilizamos palavra 'pass' em Python quando temos um bloco de código que ainda nao está implementado.

OBS: QUando nomeados nossas classes em Python utilizamos por convenção o nome com inicam em maiúsculo.
Se o nome for composto, utiliza-se as iniiais de ambas em maiúsculo, todas juntas

"""


class Lampada:
    pass


lamp = Lampada()
print(type(lamp))
