import json
from random import randint
from time import sleep

board_true = []


def print_space():
    esp = '\n' * 40
    print(esp)


def tit(string):
    a = int(len(string) / 2 + 2)
    return f'''{'-=' * a}
{str(string):^{a * 2}}
{'-=' * a}'''


def inputint(s='Escreva um número inteiro: '):
    while True:
        n2 = input(s)
        try:
            n2 = int(n2)
            return n2
        except ValueError:
            print('ERRO! Escreva um número inteiro!\n')


def possibilities(q=0, *num):
    """
    :param q: Número de quadrados a considerar
    :param num: Em quantos quadrados a soma do nº de bombas é 1
    :return:
    pos -> Possibilidade de distribuição das bombas
    tot -> Número de quadrados nos quais só há uma bomba
    i -> Início da contagem dos quadrados onde a soma das bombas é 1
    """
    lbn = []
    lp = []
    num = str(num).replace('(', '[').replace(')', ']')
    num = json.loads(num)
    for c4 in range(0, len(num)):
        num[c4] += ['']
    for c1 in range(0, 2 ** q):
        pos = []
        bn = str(bin(c1)).replace('0b', '')  # bn = int(bn, base=2) -> Reverte o processo
        bn = bn.rjust(q, '0')
        pos += bn
        ts = 0
        for c2 in range(0, len(num)):
            i = num[c2][0]
            tot = num[c2][1]  # print(bn, tot, pos)
            s = 0
            for c3 in range(i, tot + i):
                if pos[c3] == '1':
                    s += 1
            if num[c2][3] != '':
                # print(num[c2], pos[num[c2][3]])
                if pos[num[c2][3]] == '1':
                    s += 1
            if s == num[c2][2]:
                ts += 1
            # print(bn, s)
        if ts == len(num):
            lbn += [bn]
    for c5 in range(0, q):
        lp += [0]
    for item in lbn:
        for c6 in range(0, q):
            if item[c6] == '1':
                lp[c6] += 1
    return lp  # print(possibilities(10, [0, 2, 1], [1, 2, 1], [2, 3, 1], [4, 4, 2], [7, 2, 1], [8, 2, 1]))


def criar_campo(linhas, colunas):
    campo1 = []
    for c9 in range(0, colunas + 1):
        if c9 == 0:
            c9 = ' '.ljust(len(str(colunas)) + len(str(linhas)) + 2)
        campo1 += [(str(c9) + ' ').ljust(len(str(colunas)) + 1)]
    for c7 in range(0, linhas):
        if c7 == 0:
            campo1 += ['\n\n']
        else:
            campo1 += ['\n']
        for c8 in range(0, colunas + 2):
            if c8 == 0:
                campo1 += [str(c7 + 1).ljust(len(str(linhas)) + 3)]
            elif c8 == colunas + 1:
                campo1 += [str(c7 + 1).rjust(len(str(linhas)) + 4)]
            else:

                campo1 += [' ' * len(str(colunas)) + 'X']
    campo1 += ['\n']
    campo1 += ['\n']
    for c10 in range(0, colunas + 1):
        if c10 == 0:
            c10 = ' '.ljust(len(str(colunas)) + len(str(linhas)) + 2)
        campo1 += [(str(c10) + ' ').ljust(len(str(colunas)) + 1)]
    return campo1


def print_campo(board_setup):
    campo2 = ''.join(board_setup)
    print(campo2)


def bombas_campo(col1, lin1, bombs0):
    temp_campo = []
    temp_campo2d = []
    cb = 0
    for c14 in range(0, col1):
        temp_campo2d += [[]]
    for item in temp_campo2d:
        for c15 in range(0, lin1):
            item += [0]
    tamanho = col1 * lin1
    probs = ((bombs0 / tamanho) * 100) * 0.99
    while True:
        for item1 in range(0, len(temp_campo2d)):
            for item2 in range(0, len(temp_campo2d[item1])):
                dice = randint(1, 100)
                if dice <= probs:
                    if temp_campo2d[item1][item2] != 'B':
                        temp_campo2d[item1][item2] = 'B'
                        cb += 1
                if cb == bombs0:
                    break
            if cb == bombs0:
                break
        if cb == bombs0:
            break
    # print(temp_campo2d)
    n = 0
    if temp_campo2d[y1 - 1][x1 - 1] == 'B':
        for item1 in range(0, len(temp_campo2d)):
            for item2 in range(0, len(temp_campo2d[item1])):
                if temp_campo2d[item1][item2] == 0:
                    temp_campo2d[item1][item2] = 'B'
                    n += 1
                    break
                if n == 1:
                    break
            if n == 1:
                break
        temp_campo2d[y1 - 1][x1 - 1] = 0
    # print(temp_campo2d)
    for item1 in range(0, len(temp_campo2d)):
        for item2 in range(0, len(temp_campo2d[item1])):
            if temp_campo2d[item1][item2] == 0:
                try:
                    if temp_campo2d[item1 - 1][item2 - 1] == 'B' and item1 - 1 >= 0 and item2 - 1 >= 0:
                        temp_campo2d[item1][item2] += 1
                except IndexError:
                    temp_campo2d[item1][item2] += 0
                try:
                    if temp_campo2d[item1 - 1][item2] == 'B' and item1 - 1 >= 0 and item2 >= 0:
                        temp_campo2d[item1][item2] += 1
                except IndexError:
                    temp_campo2d[item1][item2] += 0
                try:
                    if temp_campo2d[item1 - 1][item2 + 1] == 'B' and item1 - 1 >= 0 and item2 + 1 >= 0:
                        temp_campo2d[item1][item2] += 1
                except IndexError:
                    temp_campo2d[item1][item2] += 0
                try:
                    if temp_campo2d[item1][item2 - 1] == 'B' and item1 >= 0 and item2 - 1 >= 0:
                        temp_campo2d[item1][item2] += 1
                except IndexError:
                    temp_campo2d[item1][item2] += 0
                try:
                    if temp_campo2d[item1][item2 + 1] == 'B' and item1 >= 0 and item2 + 1 >= 0:
                        temp_campo2d[item1][item2] += 1
                except IndexError:
                    temp_campo2d[item1][item2] += 0
                try:
                    if temp_campo2d[item1 + 1][item2 - 1] == 'B' and item1 + 1 >= 0 and item2 - 1 >= 0:
                        temp_campo2d[item1][item2] += 1
                except IndexError:
                    temp_campo2d[item1][item2] += 0
                try:
                    if temp_campo2d[item1 + 1][item2] == 'B' and item1 + 1 >= 0 and item2 >= 0:
                        temp_campo2d[item1][item2] += 1
                except IndexError:
                    temp_campo2d[item1][item2] += 0
                try:
                    if temp_campo2d[item1 + 1][item2 + 1] == 'B' and item1 + 1 >= 0 and item2 + 1 >= 0:
                        temp_campo2d[item1][item2] += 1
                except IndexError:
                    temp_campo2d[item1][item2] += 0
    # print(temp_campo2d)
    for item1 in range(0, len(temp_campo2d)):
        for item2 in range(0, len(temp_campo2d[item1])):
            temp_campo += [temp_campo2d[item1][item2]]
    # print(temp_campo)
    return temp_campo


def inputcoordenadas(show=False):
    """
    Converte coordenadas 2D para 1D
    :return: pos0 -> Posição na lista das bombas (1D)
            pos00 -> Posição no campo (2D)
    """
    col2 = col
    lin2 = lin
    line = 'Indica as coordenadas da casa que queres selecionar, separadas por um espaço (coluna linha): '
    while True:  # print(x, z, y)
        try:
            x, y = input(line).strip().ljust(len(str(col2)) + 1 + len(str(lin2))).split()
        except ValueError:
            print('ERRO! Escreva só os números e o espaço!\n')
            continue
        if x.isnumeric() and y.isnumeric():
            x = int(x)
            y = int(y)
            if 0 < x <= col2 and 0 < y <= lin2:
                break
            else:
                print('Valores incorretos, quadrado inexistente!\n')
        else:
            print_campo('ERRO! Escreva só os números e o espaço!\n')
    pos0 = x + (y - 1) * col2 - 1
    pos00 = pos0 + col2 + 1 + 3 * y - 1
    if show:
        return pos0, pos00, x, y
    else:
        return pos0, pos00


def abrir_zeros(x0, y0, c0, pos0):
    if bombs[pos0] == 0:
        for c16 in range(-1, 2):
            x3 = x0
            x3 += c16
            for c17 in range(-1, 2):
                y3 = y0
                y3 += c17
                if col >= x3 > 0 and lin >= y3 > 0:
                    pos10 = x3 + (y3 - 1) * col - 1
                    pos20 = pos10 + col + 1 + 3 * y3 - 1
                    try:
                        if board_show[pos20] != str(' ' * len(str(col)) + str(bombs[pos10])) and bombs[pos10] != 'B':
                            board_show[pos20] = str(' ' * len(str(col)) + str(bombs[pos10]))
                            c0 += 1
                            if board_show[pos20] == str(' ' * len(str(col)) + str(0)):
                                c0 = abrir_zeros(x3, y3, c0, pos10)
                    except IndexError:
                        c0 += 0
    return c0


# PROGRAMA PRINCIPAL
b = 0
c = 0
d = 0
while True:
    if d == 0:
        print(tit('          MINESWEEPER          '))
        print('')
        print(tit('Como Jogar'))
        print('''Em cada jogada, exceto a primeira, selecionas uma quadrado e o que queres fazer:
         A -> Abrir o quadrado e descobrir o que está por baixo
         B -> Por uma bandeira [simbolizada por um P]''')
        print('')
        print(tit('Campo'))
        lin = inputint('Número de linhas: ')
        col = inputint('Número de colunas: ')
        while True:
            bombas = inputint('Número de bombas a espalhar pelo campo: ')
            if bombas >= (lin * col) - 1:
                print('O campo é demasiado pequeno para tantas bombas!\n')
            elif bombas == 0:
                print('Tens de ter pelo menos uma bomba!\n')
            else:
                break
        board_show = criar_campo(lin, col)  # print(board_show)
        print_space()
        print_campo(board_show)
        pos1, pos2, x1, y1 = inputcoordenadas(show=True)
        bombs = bombas_campo(col, lin, bombas)  # print(bombs)
        board_show[pos2] = str(' ' * len(str(col)) + str(bombs[pos1]))
        if bombs[pos1] == 0:
            c = abrir_zeros(x1, y1, c, pos1)
        print_campo(board_show)
        if c + 1 == col * lin - bombas:
            print_space()
            print('\n\nGANHASTE!\n\n')
            print_campo(board_show)
            break
        d += 1
    print_space()
    print(f'''Número de quadrados abertos: {c + 1}    Total de quadrados: {col * lin}
Número de bandeiras plantadas: {b}      Minas por descobrir: {bombas - b}\n
''')
    print_campo(board_show)
    pos1, pos2, x2, y2 = inputcoordenadas(show=True)  # print(pos1, bombs[pos1], board_show[pos2])
    while True:
        acao = str(input('O que queres fazer (A/B): ')).strip().upper()
        if acao in ['A', 'B']:
            break
        else:
            print('ERRO! Escreva só "A" ou "B"\n')
    if acao == 'A':
        if board_show[pos2] != str(' ' * len(str(col)) + str(bombs[pos1])):
            board_show[pos2] = str(' ' * len(str(col)) + str(bombs[pos1]))  # print(board_show)
            c += 1
        if bombs[pos1] == 0:
            c = abrir_zeros(x2, y2, c, pos1)
            print('\nComo o quadrado que abriste era um "0", os quadrados adjacentes foram automaticamente abertos')
        if bombs[pos1] == 'B':
            print(f'''\n\nPERDESTE!
    Abriste {c + 1} quadrados\n\n''')
            print_campo(board_show)
            break
        if c + 1 == col * lin - bombas:  # print(col * lin, bombas)
            print('\n\nGANHASTE!\n\n')
            print_campo(board_show)
            break
    elif acao == 'B':
        if board_show[pos2] != str(' ' * len(str(col)) + str(bombs[pos1])):
            if board_show[pos2] != str(' ' * len(str(col)) + 'P'):
                board_show[pos2] = str(' ' * len(str(col)) + 'P')
                b += 1
            else:
                board_show[pos2] = str(' ' * len(str(col)) + 'X')
                b -= 1
        else:
            print('Quadrado já aberto!')

'''for c16 in range(1, lin + 1):
    for c17 in range(1, col + 1):
        x, y = c16, c17
        pos1 = x + (y - 1) * col - 1
        pos2 = pos1 + col + 1 + 3 * y - 1
        board_show[pos2] = str(' ' * len(str(col)) + str(bombs[pos1]))  # print(board_show)
        print_campo(board_show)'''

sleep(10)
