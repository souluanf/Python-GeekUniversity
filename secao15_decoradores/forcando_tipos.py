"""
Forçando tipos de dados com decoradores

zip

a = (1,3,5)
b = (2,4,6)

c = zip(a,b)

(1,2), (3,4), (5,6)

"""


def forca_tipo(*tipos):
    def decorador(funcao):
        def converte(*args, **kwargs):
            novo_args = []
            for (valor, tipo) in zip(args, tipos):
                novo_args.append(tipo(valor))
            return funcao(*args, **kwargs)

        return converte

    return decorador


@forca_tipo(str, int)
def repete_msg(msg, vezes):
    for vez in range(vezes):
        print(msg)


repete_msg('Luan', 3)
