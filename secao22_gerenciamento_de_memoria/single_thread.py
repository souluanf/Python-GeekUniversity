import time
from threading import Thread

CONTADOR = 50000000


def contagem_regresiva(n):
    while n > 0:
        n -= 1


inicio = time.time()
contagem_regresiva(CONTADOR)
fim = time.time()

print(f'Tempo em segundos: {fim - inicio}')
