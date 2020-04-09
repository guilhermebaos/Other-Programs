# Manter Ordem Alfabética


def format_euro(num=0):
    num = float(num)
    string = f'{num:.2f}€'
    string_org = string.replace('.', ',')
    return string_org


def tit(string, lengh=0):
    if lengh == 0:
        a = int(len(str(string)) / 2 + 2)
    else:
        a = int(lengh / 2 + 2)
    return f'''{'-=' * a}
{str(string):^{a * 2}}
{'-=' * a}'''
