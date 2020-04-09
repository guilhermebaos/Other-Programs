# Manter Ordem Alfabética


def join_list(lst, string=', '):
    """
    :param lst: List to be joined
    :param string: String that will be used to join the items in the list
    :return: List after being converted into a string
    """
    lst = str(string).join(str(x) for x in lst)
    return lst


def unique_list(lst):
    to_eliminate = []
    for c, item in enumerate(lst):
        if lst.index(item) != c:
            to_eliminate += [c]
    to_eliminate.sort(reverse=True)
    for c in to_eliminate:
        lst.pop(c)
    return lst
