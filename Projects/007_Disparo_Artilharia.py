import math

import matplotlib.animation as animation
import matplotlib.pyplot as plt
import seaborn as sns
from pynput import keyboard


def inputint(string='Escreva um número inteiro: ', error='ERRO! Escreva um número inteiro válido!\n', show_error=False,
             default=0) -> int:
    while True:
        n = input(string).strip()
        try:
            n = int(n)
            return n
        except ValueError as erro:
            if n == '':
                return default
            else:
                if show_error:
                    erro = str(erro).capitalize()
                    print(f'{error}{erro}\n')
                else:
                    print(f'{erro}\n')


def inputthis(question='-> ', expected_tuple=('Y', 'N'), error='ERRO! Resposta inesperada!'):
    while True:
        x = str(input(question)).strip()
        if x in expected_tuple:
            return x
        else:
            print(error, '\n')


_key = ''


def on_press(key):
    global _key
    try:
        _key = key.char
    except AttributeError:
        _key = key


def on_release(key):
    if str(key) != str('Key.enter'):
        return False


# Fazer títulos (não importante)
def tit(string, lengh=0):
    if lengh == 0:
        al = int(len(str(string)) / 2 + 2)
    else:
        al = int(lengh / 2 + 2)
    return f'''{'-=' * al}
{str(string):^{al * 2}}
{'-=' * al}'''


# Função para obrigar o utilizador a escrever um número (não importante)
def inputfloat(string='Escreva um número: ', error='ERRO! Escreva um número válido!\n', show_error=False,
               change_commas=True, default=0, maxi=-1.0, mini=0.0):
    while True:
        n = input(string).strip()
        if change_commas:
            n = n.replace(',', '.')
        try:
            n = float(n)
            if maxi == -1.0:
                if mini < n:
                    return n
                else:
                    print(f'ERRO! O número que escreveu tem de ser maior que {mini}')
            elif mini < n < maxi:
                return n
            elif maxi < n or mini > n:
                print(f'ERRO! O número que escreveu tem de estar entre {mini} e {maxi}')
        except ValueError as erro:
            if n == '' and default != 0:
                return default
            else:
                if show_error:
                    erro = str(erro).capitalize()
                    print(f'{error}{erro}\n')
                else:
                    print(f'{error}\n')


g = 9.80665
pi = math.pi

print(tit('Simulação de um disparo de artilharia'))

print('\nPrima [Espaço] para executar o programa com as seguintes especificações, prima outro botão para as alterar.')
print('''
A arma pode disparar com uma inclinação de 25° a 45° relativamente ao solo, disparando, no máximo, a cada 10 segundos
A bala sai do cano da arma a uma velocidade inicial de 3600km/h.
O avião viaja a uma velocidade constante de 360 km/h, a uma altitude de 2000m, pode ser detetado a 15000m de distância.
''')

# Recolhe os inputs que o utilizador faz através do teclado
with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()

# Já em unidades SI
if str(_key) == 'Key.space':
    print('\nExecutando o programa com as especificações default...\n\n')
    ang_max = math.radians(45)
    ang_min = math.radians(25)
    rel_tim = 10
    alc_rad = 15000
    vel_avi = 100
    vel_bal = 1000
    alt_avi = 2000

# Em unidades mais convencionais e depois é convertido
else:
    ang_max = 45
    ang_min = 25
    rel_tim = 10
    alc_rad = 15
    vel_avi = 360
    vel_bal = 3600
    alt_avi = 2000
    print(f'''\n\nQual das especificações pretende alterar?
    
[1] Ângulo Máximo de disparo - {ang_max:.1f}°
[2] Angulo Mínimo de disparo - {ang_min:.1f}°
[3] Tempo de recarga - {rel_tim:.1f}s
[4] Alcance do Radar - {alc_rad:.1f}km
[5] Velociade do Avião - {vel_avi:.1f}km/h
[6] Velocidade da Bala disparada - {vel_bal:.1f}km/h
[7] Altitude do avião - {alt_avi:.1f}m

[Espaço] Concluído
    ''')
    while True:
        print('\nEscolha uma das opções acima apresentadas')
        with keyboard.Listener(
                on_press=on_press,
                on_release=on_release) as listener:
            listener.join()
        if str(_key) == '1':
            ang_max = inputfloat(' -> Ângulo Máximo de disparo (graus): ', default=45, maxi=180, mini=1)
        if str(_key) == '2':
            ang_min = inputfloat(' -> Ângulo Mínimo de disparo (graus): ', default=25, maxi=ang_max, mini=0)
        if str(_key) == '3':
            rel_tim = inputfloat(' -> Tempo de Recarga (segundos): ', default=10, mini=0.1)
        if str(_key) == '4':
            alc_rad = inputfloat(' -> Alcance do Radar (km): ', default=15, mini=0.1)
        if str(_key) == '5':
            vel_avi = inputfloat(' -> Velocidade do Avião (km/h): ', default=360, mini=0.1)
        if str(_key) == '6':
            vel_bal = inputfloat(' -> Velocidade da Bala disparada (km/h): ', default=3600, mini=0.1)
        if str(_key) == '7':
            alt_avi = inputfloat(' -> Altitude do Avião (m): ', default=2000, mini=0.1)
        if str(_key) == 'Key.space':
            print(f'''\nNovas especificações:
    
[1] Ângulo Máximo de disparo - {ang_max:.1f}°
[2] Angulo Mínimo de disparo - {ang_min:.1f}°
[3] Tempo de recarga - {rel_tim:.1f}s
[4] Alcance do Radar - {alc_rad:.1f}km
[5] Velociade do Avião - {vel_avi:.1f}km/h
[6] Velocidade da Bala disparada - {vel_bal:.1f}km/h
[7] Altitude do avião - {alt_avi:.1f}m
                \n\n''')
            ang_max = math.radians(ang_max)
            ang_min = math.radians(ang_min)
            alc_rad = alc_rad * 1000
            vel_avi = vel_avi * (1 / 3.6)
            vel_bal = vel_bal * (1 / 3.6)
            break

# Primeiro tiro (menor ângulo possível)
ang = ang_min
ts_dis = [-1 * rel_tim]  # Guarda os vários tempos de disparo
ang_dis = []  # Guarda os vários ângulos de disparo
dts_dis = []  # Guarda os vários delta t de disparo
while True:
    if ((math.sin(ang) * vel_bal) ** 2 - 2 * g * alt_avi) < 0:
        ang += rel_tim / 1000
        if ang > ang_max:
            print('É impossível a bala atingir o avião!')
            break
        continue
    dt_dis = (math.sin(ang) * vel_bal - ((math.sin(
        ang) * vel_bal) ** 2 - 2 * g * alt_avi) ** 0.5) / g  # Tempo que a bala demora a chegar à altitude do avião
    dx_dis = math.cos(ang) * vel_bal * dt_dis  # Deslocamento horizontal da bala nesse intervalo de tempo
    t_dis = (alc_rad - dx_dis) / vel_avi - dt_dis  # Em que instante se deve disparar para atingir o avião
    if t_dis > (ts_dis[-1] + rel_tim):
        if len(ts_dis) == 1:
            ts_dis += [t_dis]
            ang_dis += [ang]
            dts_dis += [dt_dis]
        else:
            while True:  # Tenta diminuir o ângulo o máximo possível
                if ((math.sin(ang) * vel_bal) ** 2 - 2 * g * alt_avi) < 0:
                    ang -= rel_tim / 10000
                    continue
                t_dis_anterior = t_dis
                dt_dis_anterior = dt_dis
                dt_dis = (math.sin(ang) * vel_bal - ((math.sin(ang) * vel_bal) ** 2 - 2 * g * alt_avi) ** 0.5) / g
                dx_dis = math.cos(ang) * vel_bal * dt_dis
                t_dis = (alc_rad - dx_dis) / vel_avi - dt_dis
                if t_dis < (ts_dis[-1] + rel_tim):  # A arma já recarregou
                    ts_dis += [t_dis_anterior]
                    ang_dis += [ang_anterior]
                    dts_dis += [dt_dis_anterior]
                    break
                if ang_min > ang or ang > ang_max:
                    break
                else:
                    ang_anterior = ang
                    ang -= rel_tim / 1000000
    if ang > ang_max:
        break
    else:
        ang += rel_tim / 1000

# Elimina o tempo negativo, necessário para poder fazer ts_dis[-1] + rel_tim a qualquer momento
ts_dis.pop(0)

# Calcular os desvios em relação ao avião de todos os disparos
desvios = []
for t, tv, a in zip(ts_dis, dts_dis, ang_dis):
    x_bal = math.cos(a) * vel_bal * tv                              # Lei xt da bala
    y_bal = math.sin(a) * vel_bal * tv - 0.5 * g * (tv ** 2)        # Lei yt da bala
    x_avi = alc_rad - vel_avi * (t + tv)                            # Lei xt avião
    y_avi = alt_avi                                                 # Lei yt avião
    dx = x_bal - x_avi
    dy = y_bal - y_avi
    desvios += [[dx, dy]]

for c1 in range(0, len(ang_dis)):  # Converter os ângulos em graus
    ang_dis[c1] = math.degrees(ang_dis[c1])

c = 0
for t, dt, a in zip(ts_dis, dts_dis, ang_dis):
    c += 1
    print(
        f'O {c}º tiro será disparado {t:.2f}s após o avião ser detetado, a um ângulo de {a:.1f}°, demorando {dt:.2f}s a atingir o avião.')

visualize = inputthis('\n\nQuer ver a trajetória de de algum dos tiros [S/N]? ', ('S', 'N', 's', 'n'))

for c1 in range(0, len(ang_dis)):  # Converter de volta para radianos
    ang_dis[c1] = math.radians(ang_dis[c1])

visualize = visualize.upper()
if visualize == 'S':
    while True:
        shot = inputint('\nDigite o número do tiro que quer ver (escreva 0 para terminar): ')
        if shot > c:
            print(f'\nSó ocorreram {c} disparos!\n\n')
            continue
        elif shot == 0:
            break
        else:
            n = shot - 1
            inc = 0.1

            x_pos, y_pos = [], []
            t_elapsed = 0
            max_time = dts_dis[n]
            ang_shot = ang_dis[n]
            while True:
                x_pos += [math.cos(ang_shot) * vel_bal * t_elapsed]
                y_pos += [math.sin(ang_shot) * vel_bal * t_elapsed - 0.5 * g * (t_elapsed ** 2)]
                if y_pos[-1] <= 0 and len(y_pos) != 1:
                    break
                t_elapsed += inc

        ani_frames = len(x_pos) - 1
        Writer = animation.writers['ffmpeg']
        writer = Writer(fps=60, metadata=dict(artist='Me'), bitrate=2000)
        image = plt.figure()
        plt.xlim(0, max(x_pos)*1.05)
        plt.ylim(0, max(y_pos)*1.05)
        plt.xlabel('Componente escalar da posição na horizontal')
        plt.ylabel('Componente escalar da posição na vertical')
        plt.title('Trajetória da bala')


        def animate(i):
            snsplot = sns.lineplot(x=x_pos[:i + 1], y=y_pos[:i + 1], color='r')


        ani = animation.FuncAnimation(image, animate, frames=ani_frames, interval=5, repeat=True)
        plt.show()
