import math

import matplotlib.pyplot as plt  # Função para fazer gráficos


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
def inputfloat(string='Escreva um número: ', error='ERRO! Escreva um número válido!\n', show_error=True,
               change_commas=True, default=0):
    while True:
        n = input(string).strip()
        if change_commas:
            n = n.replace(',', '.')
        try:
            n = float(n)
            return n
        except ValueError as erro:
            if n == '' and default != 0:
                return default
            else:
                if show_error:
                    erro = str(erro).capitalize()
                    print(f'{error}{erro}\n')
                else:
                    print(f'{error}\n')


# Função para calcular a Resistência do ar, recebe a velocidade e a aceleração e devolve o módulo da força
def drag(velo, area):
    air_density = 1.225  # kg/m^3
    drag_coefficient = 0.47  # Esfera
    drag_force = 0.5 * air_density * velo ** 2 * drag_coefficient * area
    return drag_force


# Lei v(t)
def velocity(v0, a0, time):
    return v0 + a0 * time


# Lei x(t)
def position(x0, v0, a0, time):
    return x0 + v0 * time + 0.5 * a0 * (time ** 2)


# Inputs do utilizador
tit('Simulador de queda com resistência do ar')
m = inputfloat('Massa da bola (kg): ')
h = inputfloat('Altura de queda (m): ')
r = inputfloat('Raio da bola (m): ')
p = inputfloat('Resolução (pontos por segundo): ', default=2000)

# Constantes
g = 9.80665
pi = math.pi

# Variáveis cujo valor é constante
P = m * g
A = pi * r ** 2

# Valor inicial das variáveis
t = 0
x = 0
v = 0
a = g
j = 0

# Valor inicial das listas que guardam os vários valores das variáveis ao longo do tempo
tim = [t]
pos = [x]
vel = [v]
acc = [a]
jerk = [j]

# Loop para ir calculando os vários valores ao fim de cada intervalo de tempo definido pelo utilizador
while True:
    d_t = p ** (-1)  # Intervalo de tempo = 1/(pontos por segundo) -> d_t = Delta t
    t += d_t  # Instante de tempo a que correspondem os valores calculados
    Fd = drag(v, A)  # Calcular o drag de acordo com o Vf do intervalo anteriormente calculado
    Fr = P - Fd  # Calcular o módulo da resultante de forças
    a = Fr / m  # Calcular o módulo da aceleração
    x = position(x, v, a, d_t)  # Calcular o Xf de acrdo com o Xf e Vf do instante anterior e a aceleração deste
    v = velocity(v, a, d_t)  # Calcular o Vf de acordo com o Vf do instante anterior e a aceleração deste
    if len(acc) <= 2:
        j = 0
    else:
        j = (a - acc[-2]) / (t - tim[-2])  # Calcular o J usando (y2 - y1) / (x2 - x1), para dois pontos consecutivos
    tim += [t]  # Guardar o t atual
    pos += [x]  # Guardar o Xf deste instante
    vel += [v]  # Guardar o Vf deste instante
    acc += [a]  # Guardar o a deste instante
    jerk += [j]  # Guardar o j deste instante (mais corretamente, o Jm)
    # print(t, x, v, a, j) -> Usado para ver se está tudo bem com os valores ao longo do tempo
    if x > h:  # Parar quando o objeto chegar ao chão
        break

# Fazer os gráficos, aparecem um de cada vez
plt.plot(tim, pos)
plt.show()
plt.plot(tim, vel)
plt.show()
plt.plot(tim, acc)
plt.show()
plt.plot(tim, jerk)
plt.show()

# Gráfico com os 4 ao mesmo tempo
print('\n\n\n')
tit('Gráfico Final:')
print('Azul: x(t) \nVerde: v(t) \nVermelho: a(t) \nCiano: j(t)')
plt.plot(tim, pos, '-b', tim, vel, '-g', tim, acc, '-r', tim, jerk, '-c')
plt.show()
