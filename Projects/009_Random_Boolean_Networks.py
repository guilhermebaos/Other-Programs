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


states = [0, 1]         # States

# Select parameters
nodes_num = 20          # Number of Nodes
connections_num = 3     # Connections per Node
steps = 30              # Number os Steps computed
show_colors = True      # Show colors instead of 0s and spaces
on_color = 'green'      # Color of the 'On' Nodes

# The step in which the bits are flipped will be indicated by a blue number,
# The first perturbation_num bits will be flipped
perturbation = True     # Cause perturbations? (bit flips)
perturbation_step = 15  # When will the perturbations occur
perturbation_num = 5    # How many bits will be flipped

# Can Nodes receive more than 1 bit from one other Node, e.g:
# if True, than Node 1 can have the following connections [2, 2, 3]
# if False, than Node 1 can't have the repeating connection from Node 2
repeat_connections = True


if show_colors:
    from termcolor import cprint

if perturbation_num >= nodes_num:
    raise Exception('The number of perturbed nodes must be lower than the total number of nodes')

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

steps_len = len(str(steps))
background_color = 'on_' + on_color
for current_step in range(steps):
    # Calculate the states of the new nodes
    new_nodes = []
    for node_list in connections:
        feed = ''
        for node_index in node_list:
            feed += str(nodes[node_index])
        new_nodes += [truth_table[binaryToDecimal(feed)]]

    # Create the perturbations (bit flips)
    if perturbation and current_step == perturbation_step:
        cprint(str(current_step).rjust(steps_len), 'blue', end=' ')
        for i in range(perturbation_num):
            new_nodes[i] = (new_nodes[i] + 1) % 2
    else:
        print(str(current_step).rjust(steps_len), end=' ')

    # Print the results
    for boolean in new_nodes[:-1]:
        if show_colors:
            if boolean == 0:
                print(' ', end='')
            else:
                cprint(' ', on_color, background_color, end='')
        else:
            if boolean == 0:
                text = ' '
            else:
                text = '1'
            print(text, end='')
    if show_colors:
        if new_nodes[-1] == 0:
            print(' ')
        else:
            cprint(' ', on_color, background_color)
    else:
        if new_nodes[-1] == 0:
            print('0')
        else:
            print(' ')
    nodes = new_nodes[:]
