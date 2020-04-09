# Manter Ordem Alfabética


def counter(i=0, f=10, p=1):
    """
    :param i: Beggining of the counter
    :param f: End of the counter
    :param p: Distance between consecutive numbers in the sequece
    :return: List with the entire sequence
    """
    p = abs(p)
    if p == 0:
        p = 1
    if f < i:
        p = p * -1
    contagem = []
    while True:
        contagem += [i]
        i += p
        if i >= f and p > 0:
            break
        elif i <= f and p < 0:
            break
    return contagem


def divisors(num):  # Para números com até 16-17 digitos
    fatprim = primefact(num) + [1]
    organizados = []
    temp = []
    contadores = []
    prime_fact_power = []
    org = fatprim[0]
    divisors_ = [1]
    divisors_temp = []
    for item1 in fatprim:
        if item1 == org:
            temp += [item1]
        else:
            organizados += [temp[:]]
            temp = []
            org = item1
            temp += [item1]
    for item2 in organizados:
        contadores += [item2]
    for item3 in contadores:
        prime_fact_power_temp = []
        for c in range(1, len(item3) + 1):
            prime_fact_power_temp += [item3[0] ** c]
        prime_fact_power += [prime_fact_power_temp[:]]
    for c1 in range(0, len(prime_fact_power)):
        divisors_ += divisors_temp[:]
        divisors_temp = []
        if len(divisors_) == 0:
            divisors_ += prime_fact_power[c1]
            print(divisors_)
        else:
            for item4 in prime_fact_power[c1]:
                for item5 in divisors_:
                    divisors_temp += [item4 * item5]
    divisors_ += divisors_temp[:]
    divisors_.sort()
    return divisors_


def decrease(num=0, pcent=0):
    num = num - (num * pcent / 100)
    return num


def double(num):
    return num * 2


def factorial(num):
    if num == 1:
        return 1
    else:
        return num * factorial(num - 1)


def gcd(*num):
    len_num = len(num)
    if len_num < 2:
        return None
    elif len_num == 2:
        a = num[0]
        b = num[1]
        if a == b:
            return a
        elif a > b:
            big = a
            small = b
        else:
            big = b
            small = a
        small_ = big % small
        if small_ == 0:
            return small
        else:
            return gcd(small, small_)
    else:
        return gcd(gcd(num[0], num[1]), num[2])


def increase(num=0, pcent=0):
    num = num + (num * pcent / 100)
    return num


def lcm(*num):
    len_num = len(num)
    num = list(num)
    if str(type(num[0])) == "<class 'list'>":
        num = num[0]
        len_num = len(num)
    if len_num < 2:
        return None
    elif len_num == 2:
        a = num[0]
        b = num[1]
        if a == b:
            return a
        elif a > b:
            big = a
            small = b
        else:
            big = b
            small = a
        return int(big / gcd(big, small) * small)
    else:
        num[0] = lcm(num[0], num[-1])
        num.pop(-1)
        return lcm(num)


def line_2d(p1=(), p2=()):
    """
    :param p1: Coordinates of first point
    :param p2: Coordinates of second point
    :return: Slope, intersection
    """
    try:
        m = (p2[1] - p1[1]) / (p2[0] - p1[0])
        b = p1[1] - m * p1[0]
        return [m, b]
    except ZeroDivisionError:
        if p2[1] == p1[1]:
            return ['']
        else:
            m = 'N.D.'
            b = 'N.D.'
            return [m, b]


def num_divisors(n):
    fatprim = primefact(n) + [1]
    organizados = []
    temp = []
    contadores = []
    org = fatprim[0]
    for item1 in fatprim:
        if item1 == org:
            temp += [item1]
        else:
            organizados += [temp[:]]
            temp = []
            org = item1
            temp += [item1]
    for item2 in organizados:
        contadores += [len(item2) + 1]
    print(contadores)
    total = 1
    for item3 in contadores:
        total *= item3
    return total


def num_divisors_n_power_n(n):
    fatprim = primefact(n) + [1]
    organizados = []
    temp = []
    contadores = []
    org = fatprim[0]
    for item1 in fatprim:
        if item1 == org:
            temp += [item1]
        else:
            organizados += [temp[:]]
            temp = []
            org = item1
            temp += [item1]
    for item2 in organizados:
        contadores += [len(item2) * n + 1]
    total = 1
    for item3 in contadores:
        total *= item3
    return total


def primefact(n):  # Para números com até 16-17 digitos
    i = 2
    fatores = []
    while (i * i) <= n:
        if (n % i) == 0:
            n = n / i
            fatores += [i]
        else:
            i += 1
            if i % 2 == 0:
                i += 1
            if i % 3 == 0 and i != 3:
                i += 1
    if n > 1:
        fatores += [int(n)]
    return fatores


def triple(num):
    return num * 3
