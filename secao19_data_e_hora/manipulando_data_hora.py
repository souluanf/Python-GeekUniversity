"""
Manipulando Data e Hora

Python tem um módulo built-in (integrado) para se trabalhar com data e hora

# print(dir(datetime))

print(datetime.MAXYEAR)

print(datetime.MINYEAR)

# Retorna data e hora corrente
print(datetime.datetime.now())  # 2020-10-30 14:38:06.033828

# datetime.datetime(year, month, day, hour, minute, second, microsecond)
print(repr(datetime.datetime.now()))

# replace() para fazer ajustes na data/hora
inicio = datetime.datetime.now()
print(inicio)

# Alterar o horário para 16 horas, 0 minuto,0 segundo, 0 micosegundo
inicio = inicio.replace(hour=16, minute=0, second=0, microsecond=0)

print(inicio)
"""

import datetime

evento = datetime.datetime(2019, 1, 1, 0)

print(type(evento))
print(type('31/12/2020'))

print(evento)

nascimento = input('Informe sua data de nascimento (dd/mm/yyyy): ')
nascimento = nascimento.split('/')
nascimento = datetime.datetime(int(nascimento[2]), int(nascimento[1]), int(nascimento[0]))
print(nascimento)
print(type(nascimento))


# Acesso individual dos elementos

print(evento.year)
print(evento.month)
print(evento.day)
print(evento.hour)
print(evento.minute)
print(evento.second)
print(evento.microsecond)

