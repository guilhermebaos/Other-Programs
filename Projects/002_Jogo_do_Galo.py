from random import choice
from time import sleep

lr1 = ['S', 'N']  # Lista Respostas 1
lqd = ['1', '2', '3', '4', '5', '6', '7', '8', '9']  # Lista Quadrados Disponíveis
lqo = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']  # Lista Quadrados Ocupados
ln = ['1', '2', '3', '4', '5', '6', '7', '8', '9']  # Lista núemros (1-9)
ljpc = []  # Lista de jogadas de entre as quais o pc poderá escolher, determinadas pelas regras
lrs = ['S', 'N']  # Lista respostas Sim ou Não
lqj1, lqj2 = [], []  # Lista com os quadrados de cada jogador
lcv = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9'],
       ['1', '4', '7'], ['2', '5', '8'], ['3', '6', '9'],
       ['1', '5', '9'], ['3', '5', '7'], ]
lcqv = [['1', '2'], ['2', '3'], ['1', '3'], ['4', '5'], ['5', '6'], ['4', '6'], ['7', '8'], ['8', '9'], ['7', '9'],
        ['1', '4'], ['4', '7'], ['1', '7'], ['2', '5'], ['5', '8'], ['2', '8'], ['3', '6'], ['6', '9'], ['3', '9'],
        ['1', '5'], ['5', '9'], ['1', '9'], ['3', '5'], ['5', '7'], ['3', '7']]
c1 = 0
p4 = 0
lb = []
v = False  # Vitória


def set_approach(a, b):
    return list(set(a) - set(b))


def comprehension(a, b):
    return [x for x in a if x not in b]


print(f'''{'-=' * 11}
{'Jogo do Galo':^22}
{'-=' * 11}''')
print('Depois de escreveres, clica Enter!')
print('\n' * 2)

while True:
    while True:
        p1 = str(input('Número de jogadores[1/2]: ')).strip()
        if p1 not in ['1', '2']:
            print('Escreve só "1" ou "2"!\n')
        else:
            break
    if p1 == '1':
        while True:
            p3 = str(input('''\n[1] -> Fácil
[2] -> Médio
[3] -> Impossível
Escolhe a dificuldade: '''))
            if p3 not in ['1', '2', '3']:
                print('Escreve só "1", "2" ou "3"!\n')
            else:
                break
    while True:
        p2 = str(input('\nQueres ver como se joga[S/N]? ')).strip().upper()
        if p2 not in lrs:
            print('Escreve só "S" ou "N"!\n')
        else:
            break
    if p2 == 'S':
        print('''Aqui está o campo:
        
         | | 
         | | 
         | | 
         
Quando for a tua vez, escolhes um lugar para jogar, escrevendo o número correspondente:''')
    print(f'''
        {lqo[1]}|{lqo[2]}|{lqo[3]}
        {lqo[4]}|{lqo[5]}|{lqo[6]}
        {lqo[7]}|{lqo[8]}|{lqo[9]}''')
    while True:
        c1 += 1
        if c1 % 2 != 0:
            while True:
                j1 = str(input('É a tua vez, Jogador 1: ')).strip()
                if j1 not in ln:
                    print('Quadrado inexistente!')
                elif j1 not in lqd:
                    print('Quadrado ocupado!')
                else:
                    lqd.remove(j1)
                    lqo[int(j1)] = 'X'
                    lqj1.append(j1)
                    break
        else:
            if p1 == '2':
                while True:
                    j2 = str(input('É a tua vez, Jogador 2: ')).strip()
                    if j2 not in ln:
                        print('Quadrado inexistente!')
                    elif j2 not in lqd:
                        print('Quadrado ocupado!')
                    else:
                        lqd.remove(j2)
                        lqo[int(j2)] = 'O'
                        lqj2.append(j2)
                        break
            elif p1 == '1':
                print('O computador vai jogar...')
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
                                    # print(i4, i3, lqj1)
                                    j2 = comprehension(i3, i4)
                                    # print(''.join(j2))
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
                                        # print(i4, i3, lqj1)
                                        j2 = comprehension(i3, i4)
                                        # print(''.join(j2))
                                        j2 = ''.join(j2)
                                        if j2 not in lqd:
                                            j2 = 0
                                        else:
                                            break
                    if j2 == 0:
                        # print('teste, f0')
                        for i5 in lqd:
                            lqj2t = lqj2[:]
                            lqj2t += i5
                            for i6 in lcqv:
                                if set(i6).issubset(lqj2t):
                                    # print('teste, f1', i5, i6)
                                    for i7 in lcqv:
                                        if set(i7).issubset(lqj2t) and i7 != i6:
                                            j2 = str(i5)
                                            # print(i5, i6, i7, j2)
                    if j2 == 0:
                        if lqo[5] == '5':
                            j2 = '5'
                            print('1')
                    if j2 == 0:
                        if lqo[1] != '1' and lqo[9] == '9':
                            j2 = '9'
                            print('2')
                        elif lqo[3] != '3' and lqo[7] == '7':
                            j2 = '7'
                            print('2')
                        elif lqo[7] != '7' and lqo[3] == '3':
                            j2 = '3'
                            print('2')
                        elif lqo[9] != '9' and lqo[1] == '1':
                            j2 = '1'
                            print('2')
                        # print(1, j2)
                    if j2 == 0:
                        ncantos = ['2', '4', '6', '8']
                        if lqo[1] != '1' and lqo[9] != '9':
                            j2 = choice(ncantos)
                            print('3')
                        if lqo[3] != '3' and lqo[7] != '7':
                            j2 = choice(ncantos)
                            print('3')
                    if j2 == 0:
                        for c6 in range(0, 4):
                            cantos = ['1', '3', '7', '9']
                            j2 = choice(cantos)
                            if lqo[int(j2)] != j2:
                                cantos.remove(j2)
                                j2 = 0
                        # print(2, j2)
                    if j2 == 0:
                        j2 = choice(lqd)
                        # print(j2, 'random')
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
                    print('O Jogador 1 ganhou!')
                    v = True
                    c1 = 0
                    break
                elif set(i).issubset(lqj2):
                    print('O Jogador 2 ganhou!')
                    v = True
                    c1 = 0
                    break
        if c1 == 9:
            print('Empate!')
            v = True
        if v:
            while True:
                p4 = 'N'  # str(input('Queres jogar outra vez[S/N]? ')).strip().upper()
                if p4 not in lrs:
                    print('Escreve só "S" ou "N"!')
                else:
                    break
            if p4 == 'N':
                break
        if p4 == 'N':
            break
    if p4 == 'N':
        break
stop = input('')
