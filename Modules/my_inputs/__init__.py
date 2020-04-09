# Manter Ordem Alfabética


def inputfloat(string='Escreva um número: ', error='ERRO! Escreva um número válido!\n', show_error=False,
               change_commas=True, default=0):
    """
    :param string: Input text
    :param error: Error message for non-float input
    :param show_error: Show what caused the error
    :param change_commas: Change commas in numbers to dots
    :param default: Default value for input
    :return: The float entered by the user
    """
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


def inputint(string='Escreva um número inteiro: ', error='ERRO! Escreva um número inteiro válido!\n', show_error=False,
             default=0) -> int:
    """
    :param string: Input text
    :param error: Error message for non-interger input
    :param show_error: Show what caused the error
    :param default: Default value for input
    :return: The interger entered by the user
    """
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
    """
    :param question: Input text
    :param expected_tuple: Tuple containing all the options from wich the user should choose from
    :param error: Error message for when the input isn't cointained in the tuple
    :return: The user's answer
    """
    while True:
        x = str(input(question)).strip()
        if x in expected_tuple:
            return x
        else:
            print(error, '\n')
