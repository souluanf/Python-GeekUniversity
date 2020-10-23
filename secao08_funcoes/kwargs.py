"""
**kwargs
Poderíamos chamar este parâmetros de **xis, mas por convenção chamamos de **kwargs
Este é só mais um parâmetro, mas diferente do args que coloca os avalores extras em uma tupla
O **kwargs exige que utilizemos parâmetros nomeados e transforma esse parãmetros extras em um dicionários

# Exemplo
def cores_favoritas(**kwargs):
    for pessoa, cor in kwargs.items():
        print(f'A cor favosita de {pessoa.title()} é {cor}')

cores_favoritas(marcos='verde', julia='amarelo', fernanda='azul', vanessa='branco')

# OBS: Os parâmetros *args e **kwargs não são obrigatórios
cores_favoritas()
cores_favoritas(geek='Navy')

# Exemplo mais complexo

def cumprimento_especial(**kwargs):
    if 'geek' in kwargs and kwargs['geek'] == 'python':
        print(f'Você srecebeu um cumprimento Pythônico Geek')
    elif 'geek' in kwargs:
        return f"{kwargs['geek']} Geek!"
    return 'Não tenho certeza que você é...'

print(cumprimento_especial(geek='Python'))

# NAa funções , podemos ter(nesta ordem):


- Parâmetros obrigatórios;
- * args;
- Parâmetros default (não obrigatórios);
- **kwargs;

def minha_funcao(idade, nome, *args, solteiro=False, **kwargs):
    print(f'{nome} tem {idade} anos')
    print(args)
    if solteiro:
        print('Solteiro')
    else:
        print('Casado')
    print(kwargs)


minha_funcao(24, 'Luan',3,eu='Não',voce='Vai',solteiro=True)

"""



