from random import choice
from time import sleep

lr1 = ['Y', 'N']  # Lista Respostas 1
lqd = ['1', '2', '3', '4', '5', '6', '7', '8', '9']  # Lista Quadrados Disponíveis
lqo = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']  # Lista Quadrados Ocupados
ln = ['1', '2', '3', '4', '5', '6', '7', '8', '9']  # Lista núemros (1-9)
ljpc = []  # Lista de jogadas de entre as quais o pc poderá escolher, determinadas pelas regras
lrs = ['Y', 'N']  # Lista respostas Sim ou Não
lqj1, lqj2 = [], []  # Lista com os quadrados de cada jogador
lcv = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9'],
       ['1', '4', '7'], ['2', '5', '8'], ['3', '6', '9'],
       ['1', '5', '9'], ['3', '5', '7'], ]
lcqv = [['1', '2'], ['2', '3'], ['1', '3'], ['4', '5'], ['5', '6'], ['4', '6'], ['7', '8'], ['8', '9'], ['7', '9'],
        ['1', '4'], ['4', '7'], ['1', '7'], ['2', '5'], ['5', '8'], ['2', '8'], ['3', '6'], ['6', '9'], ['3', '9'],
        ['1', '5'], ['5', '9'], ['1', '9'], ['3', '5'], ['5', '7'], ['3', '7']]
c1 = 0
ck = 0
p4 = 0
lb = []
v = False  # Vitória


def set_approach(a, b):
    return list(set(a) - set(b))


def comprehension(a, b):
    return [x for x in a if x not in b]


def tit(string):
    a = int(len(string) / 2 + 2)
    return f'''{'-=' * a}
{str(string):^{a * 2}}
{'-=' * a}'''


init = '''Kira Gaming Companion 
DEMO v1.1
MODE: Tic Tac Toe'''
print(f'''{'-=' * 11}
{init:^22}
{'-=' * 11}''')
print('\n' * 2)

while True:
    while True:
        p1 = str(input('Number of players[1/2]: ')).strip()
        if p1 not in ['1', '2']:
            print('Write only "1" or "2"!\n')
        else:
            break
    if p1 == '1':
        while True:
            print('Loading KIRA')
            sleep(3)
            print('Player 1 vs Kira:')
            p3 = str(input('''\n\n[1] -> Easy
[2] -> Medium
[3] -> Impossible
Choose the difficulty: '''))
            if p3 not in ['1', '2', '3']:
                print('Write only "1", "2" or "3"!\n')
            else:
                break
    while True:
        p2 = str(input('\nDo you want to see the controls [Y/N]? ')).strip().upper()
        if p2 not in lrs:
            print('Write only "Y" or "N"!\n')
        else:
            break
    if p2 == 'Y':
        print(f'''Here's the board:

         | | 
         | | 
         | | 

During your turn, choose the tile where you want to play, typing the correspondent number:
\n\n\n

        {lqo[1]}|{lqo[2]}|{lqo[3]}
        {lqo[4]}|{lqo[5]}|{lqo[6]}
        {lqo[7]}|{lqo[8]}|{lqo[9]}''')
    if p1 == '1':
        while True:
            p5 = str(input('\nWhich Player goes first [1/Kira]: ')).strip().upper()
            if p5 not in ['1', 'KIRA']:
                print('Write only "1" or "Kira"!\n')
            else:
                break
        if p5 == 'KIRA':
            ck = 1
    sleep(0.5)
    c1 += ck
    print('\n\n')
    print(f'''
        {lqo[1]}|{lqo[2]}|{lqo[3]}
        {lqo[4]}|{lqo[5]}|{lqo[6]}
        {lqo[7]}|{lqo[8]}|{lqo[9]}''')
    while True:
        c1 += 1
        if c1 % 2 != 0:
            while True:
                j1 = str(input("It's your turn, Player 1: ")).strip()
                if j1 not in ln:
                    print('Inexistent tile!')
                elif j1 not in lqd:
                    print('Ocupied tile!')
                else:
                    lqd.remove(j1)
                    lqo[int(j1)] = 'X'
                    lqj1.append(j1)
                    break
        else:
            if p1 == '2':
                while True:
                    j2 = str(input("It's your turn, Player 2: ")).strip()
                    if j2 not in ln:
                        print('Inexistent tile!')
                    elif j2 not in lqd:
                        print('Ocupied tile!')
                    else:
                        lqd.remove(j2)
                        lqo[int(j2)] = 'O'
                        lqj2.append(j2)
                        break
            elif p1 == '1':
                print('Kira is playing...')
                sleep(1.5)
                if p3 == '1':
                    sleep(2)
                    j2 = choice(lqd)
                    lqd.remove(j2)
                    lqo[int(j2)] = 'O'
                    lqj2.append(j2)
                elif p3 == '2':
                    j2 = 0
                    for i4 in lcqv:
                        if j2 in lqd:
                            break
                        if set(i4).issubset(lqj1):
                            for i3 in lcv:
                                if set(i4).issubset(i3):
                                    j2 = comprehension(i3, i4)
                                    j2 = ''.join(j2)
                                    if j2 not in lqd:
                                        j2 = 0
                                    else:
                                        break
                    if j2 == 0:
                        j2 = choice(lqd)
                    sleep(1.5)
                    lqd = set_approach(lqd, j2)
                    lqo[int(''.join(j2))] = 'O'
                    lqj2.append(''.join(j2))
                elif p3 == '3':
                    j2 = 0
                    if j2 == 0:
                        for i8 in lqd:
                            lqj2t = lqj2[:]
                            lqj2t += i8
                            for i9 in lcv:
                                if set(i9).issubset(lqj2t):
                                    j2 = str(i8)
                    if j2 == 0:
                        for i4 in lcqv:
                            if j2 in lqd:
                                break
                            if set(i4).issubset(lqj1):
                                for i3 in lcv:
                                    if set(i4).issubset(i3):
                                        j2 = comprehension(i3, i4)
                                        j2 = ''.join(j2)
                                        # print(j2, lqd)
                                        if j2 not in lqd:
                                            j2 = 0
                                        else:
                                            break
                    if j2 == 0:
                        for i5 in lqd:
                            lqj2t = lqj2[:]
                            lqj2t += i5
                            for i6 in lcqv:
                                if set(i6).issubset(lqj2t):
                                    for i7 in lcqv:
                                        if set(i7).issubset(lqj2t) and i7 != i6:
                                            j2 = str(i5)
                    if j2 == 0:
                        if lqo[5] == '5':
                            j2 = '5'
                    if j2 == 0:
                        if lqo[1] != '1' and lqo[9] == '9':
                            j2 = '9'
                        elif lqo[3] != '3' and lqo[7] == '7':
                            j2 = '7'
                        elif lqo[7] != '7' and lqo[3] == '3':
                            j2 = '3'
                        elif lqo[9] != '9' and lqo[1] == '1':
                            j2 = '1'
                    if j2 == 0:
                        if lqo[1] == 'X' and lqo[5] == 'X':
                            j2 = choice(['3', '7'])
                            if j2 not in lqd:
                                j2 = 0
                        if lqo[3] == 'X' and lqo[5] == 'X':
                            j2 = choice(['1', '9'])
                            if j2 not in lqd:
                                j2 = 0
                        if lqo[7] == 'X' and lqo[5] == 'X':
                            j2 = choice(['1', '9'])
                            if j2 not in lqd:
                                j2 = 0
                        if lqo[9] == 'X' and lqo[5] == 'X':
                            j2 = choice(['3', '7'])
                            # print('1')
                            if j2 not in lqd:
                                j2 = 0
                    if j2 == 0:
                        ncantos = ['2', '4', '6', '8']
                        if lqo[1] != '1' and lqo[9] != '9':
                            j2 = choice(ncantos)
                        if lqo[3] != '3' and lqo[7] != '7':
                            j2 = choice(ncantos)
                    if j2 == 0:
                        for c6 in range(0, 4):
                            cantos = ['1', '3', '7', '9']
                            j2 = choice(cantos)
                            if lqo[int(j2)] != j2:
                                cantos.remove(j2)
                                j2 = 0
                    if j2 == 0:
                        j2 = choice(lqd)
                    sleep(1.5)
                    lqd = set_approach(lqd, j2)
                    lqo[int(''.join(j2))] = 'O'
                    lqj2.append(''.join(j2))
        print('\n' * 40)
        print(f'''
        {lqo[1]}|{lqo[2]}|{lqo[3]}
        {lqo[4]}|{lqo[5]}|{lqo[6]}
        {lqo[7]}|{lqo[8]}|{lqo[9]}''')
        if c1 > 4:
            for i in lcv:
                if set(i).issubset(lqj1):
                    print('Player 1 has won!')
                    v = True
                    c1 = 0
                    break
                elif set(i).issubset(lqj2):
                    if p1 == '1':
                        print('Kira has won!')
                    else:
                        print('Player 2 has won!')
                    v = True
                    c1 = 0
                    break
        if c1 == 9 + ck:
            print('Draw!')
            v = True
        if v:
            while True:
                p4 = 'N'
                '''str(input('\nDo you want to see the controls [Y/N]? ')).strip().upper()
                if p2 not in lrs:
                    print('Write only "Y" or "N"!\n')
                else:
                    break'''
                if p4 not in lrs:
                    print('Write only "Y" or "N"!')
                else:
                    break
            if p4 == 'N':
                break
        if p4 == 'N':
            break
    if p4 == 'N':
        break
stop = input('')
