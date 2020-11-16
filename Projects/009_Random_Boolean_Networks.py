# From Computerphile at: https://www.youtube.com/watch?v=mCML2B94rUg

from random import choice, randint


def binaryToDecimal(num_str):
    dec = 0
    len_num = len(num_str)
    num_str = str(num_str)
    for pos, bit in enumerate(num_str):
        if int(bit) == 1:
            dec += 2 ** (len_num - pos - 1)
    return dec


def join_list(lst, string=''):
    lst = str(string).join(str(x) for x in lst)
    return lst


# Select parameters
nodes_num = 20          # Number of Nodes
connections_num = 3     # Connections per Node
steps = 20              # Number os Steps computed
show_colors = True      # Show colors instead of 0s and spaces
states = [0, 1]

# Can Nodes receive more than 1 bit from one other Node, e.g:
# if True, than Node 1 can have the following connections [2, 2, 3]
# if False, than Node 1 can't have the repeating connection from Node 2
repeat_connections = True


if show_colors:
    from termcolor import cprint

# Create the first nodes and their connections
nodes = []
connections = []
for _ in range(nodes_num):
    nodes += [choice(states)]
    connections += [[]]
    while len(connections[-1]) < connections_num:
        possible = randint(0, nodes_num - 1)
        if (not repeat_connections) and connections[-1].__contains__(possible):
            pass
        else:
            connections[-1] += [possible]

# Create the truth table
truth_table = []
for _ in range(2 ** connections_num):
    truth_table += [choice(states)]

for _ in range(steps):
    # Calculate the states of the new nodes
    new_nodes = []
    for node_list in connections:
        feed = ''
        for node_index in node_list:
            feed += str(nodes[node_index])
        new_nodes += [truth_table[binaryToDecimal(feed)]]

    # Print the results
    for boolean in new_nodes[:-1]:
        if show_colors:
            if boolean == 0:
                color = 'red'
                on_color = 'on_red'
            else:
                color = 'green'
                on_color = 'on_green'
            cprint(' ', color, on_color, end='')
        else:
            if boolean == 0:
                text = '0'
            else:
                text = ' '
            print(text, end='')
    if show_colors:
        if new_nodes[-1] == 0:
            cprint(' ', 'red', 'on_red')
        else:
            cprint(' ', 'green', 'on_green')
    else:
        if new_nodes[-1] == 0:
            print('0')
        else:
            print(' ')
    nodes = new_nodes[:]
