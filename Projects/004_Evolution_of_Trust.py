from random import choice
from time import sleep

lp = []
lc = []
lpc = []
personas = ['1', '2', '3', '4', '5', '6', '7', '8']
pp = 0
ppc = 0


def inputint(s='Escreva um número inteiro: '):
    while True:
        n2 = input(s)
        try:
            n2 = int(n2)
            return n2
        except ValueError:
            print('ERRO! Escreva um número inteiro!\n')


def rancoroso():
    if 'R' in lp:
        return 'R'
    else:
        return 'P'


def inteligente():
    try:
        if lp[-1] == 'P':
            return 'P'
    except IndexError:
        return 'P'
    else:
        return 'R'


def inteligente_simpatico():
    try:
        if lp[-1] == 'R' and lp[-2] == 'R':
            return 'R'
    except IndexError:
        return 'P'
    else:
        return 'P'


def analista():
    if len(lp) < 2:
        return 'P'
    else:
        if len(lp) % 2 == 0 and lp[-2] == 'P':
            return 'R'
        else:
            if lp[-1] == 'P':
                return 'P'
            else:
                return 'R'


def aleatorio():
    choice(['P', 'R'])


def inteligente_aproveitador():
    if len(lc) == 1:
        return 'R'
    else:
        try:
            if lp[-1] == 'P':
                return 'P'
        except IndexError:
            return 'P'
        else:
            return 'R'


def ingenuo():
    return 'P'


def desconfiado():
    return 'R'


print(f'''{"-" * 30}
{"Evolution of Trust":^30}
{"-" * 30}
''')
print('''Neste jogo, em cada turno, podes fazer uma de duas coisas:
[P] -> Partilhar
[R] -> Roubar

Se ambos os jogadores partilharem, ambos recebem 3€
Se um deles partilhar o outro roubar, quem roubou recebe 5€ e quem partilhou não recebe nada
Se ambos roubarem, ambos recebem 1€

''')
while True:
    p1 = str(input('''Escolha a personalidade com quem vai querer jogar:
                0. Informação sobre as personagens
                1. 'O Rancoroso'
                2. 'O Inteligente'
                3. 'O Inteligente Simpático'
                4. 'O Analista'
                5. 'O Aleatório'
                6. 'O Inteligente Aproveitador'
                7. 'O Ingénuo'
                8. 'O Desconfiado' 
    -> ''')).strip()
    if p1 in personas:
        break
    elif p1 == '0':
        print('''
        'O Rancoroso' -> Começa por partilhar, assim que for roubado, roubará até ao final do jogo
        'O Inteligente' -> Imita o que fizeste na jogada anterior
        'O Inteligente Simpático' -> Rouba-te se o roubares duas vezes seguidas
        'O Analista' -> Começa por partilhar, mas irá eventualmente roubar, e se tu não o roubares de volta, ele continuará a roubar-te
        'O Aleatório' -> Partilha e rouba de forma aleatória
        'O Inteligente Aproveitador' -> Imita o que tu fizeste na última ronda, mas de vez em quando rouba
        'O Ingénuo' -> Partilha sempre
        'O Desconfiado' -> Rouba sempre
        ''')
    else:
        print('Escreva só o número!\n\n\n')

if p1 == '1':
    pers = rancoroso
if p1 == '2':
    pers = inteligente
if p1 == '3':
    pers = inteligente_simpatico
if p1 == '4':
    pers = analista
if p1 == '5':
    pers = aleatorio
if p1 == '6':
    pers = inteligente_aproveitador
if p1 == '7':
    pers = ingenuo
if p1 == '8':
    pers = desconfiado
p5 = inputint('Quantas rondas queres jogar? ')
while True:
    p3 = str(input('Queres ser uma personalidade [S/N]? ')).strip().upper()
    if p3 in ['S', 'N']:
        break
    else:
        print('ERRO! Escreve só "S" ou "N"!\n')
if p3 == 'S':
    while True:
        p4 = str(input('''\n\nEscolha a personalidade que queres imitar:
                    1. 'O Rancoroso'
                    2. 'O Inteligente'
                    3. 'O Inteligente Simpático'
                    4. 'O Analista'
                    5. 'O Aleatório'
                    6. 'O Inteligente Aproveitador'
                    7. 'O Ingénuo'
                    8. 'O Desconfiado' 
        -> ''')).strip()
        if p4 in personas:
            break
        else:
            print('Escreva só o número!\n\n\n')

    if p4 == '1':
        persj = rancoroso
    if p4 == '2':
        persj = inteligente
    if p4 == '3':
        persj = inteligente_simpatico
    if p4 == '4':
        persj = analista
    if p4 == '5':
        persj = aleatorio
    if p4 == '6':
        persj = inteligente_aproveitador
    if p4 == '7':
        persj = ingenuo
    if p4 == '8':
        persj = desconfiado

for a in range(0, p5):
    if p3 == 'N':
        while True:
            p2 = str(input('\n\nQueres Partilhar ou Roubar? ')).strip().upper()
            if p2 in ['P', 'R']:
                break
            else:
                print('ERRO, Ercreva só "P" ou "R"!\n')
    else:
        p2 = persj()
        sleep(0.5)
    pc = pers()
    lp += [p2]
    lc += [pc]
    t = [p2, pc]
    lpc += [t]
    print(f'''
    Jogador ->    {', '.join(lp)}
    Computador -> {', '.join(lc)}''')

for item in lpc:
    if item[0] == 'P' and item[1] == 'P':
        pp += 3
        ppc += 3
    elif item[0] == 'P' and item[1] == 'R':
        pp += 0
        ppc += 5
    elif item[0] == 'R' and item[1] == 'P':
        pp += 5
        ppc += 0
    elif item[0] == 'R' and item[1] == 'r':
        pp += 1
        ppc += 1
print(f'''\n\n\nReceita final (15 rondas):
Jogador - {pp}€
Computador - {ppc}€''')
