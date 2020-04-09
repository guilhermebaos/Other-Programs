from time import sleep

while True:
    v = []
    r = ' '
    print('\n')
    print('-=-' * 20)
    print('PROGRAMA DE ENCRIPTAÇÃO')
    print('-=-' * 20)
    print('Prima [ 0 ] para encriptar')
    print('Prima [ 1 ] para desencriptar')
    print('-=-' * 20)
    while True:
        f = str(input('\nFunção desejada: '))
        if f == '0':
            e = 'encriptar'
            e1 = 'encriptada'
            e2 = 'ENCRIPTANDO'
            e3 = 1.5
            break
        elif f == '1':
            e = 'desencriptar'
            e1 = 'desencriptada'
            e2 = 'DESENCRIPTANDO'
            e3 = 1.5
            break
        else:
            print('Escreva apenas "0" ou "1"!')
    m = str(input(f'Escreva a mensagem que deseja {e}: ')).strip()
    lm = len(m)
    print(f'{e2}...')
    lj = (int(lm ** 0.5) + 1) ** 2
    m = m.ljust(lj)
    for c1 in range(0, int(lj ** 0.5)):
        for c2 in range(0 + c1, lj, int(lj ** 0.5)):
            v += [m[c2]]
    sleep(e3)
    print(''.join(v))
    while r not in 'SN':
        r = str(input('\nQueres codificar/ descodificar outra mensagem? (S/N)')).strip().upper()[0]
        if r not in 'SN':
            print('Escreve apenas "S" ou "N" ')
    if r == 'N':
        break
