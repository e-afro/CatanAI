def get_row_len(row):
    if row < 3:
        tmp = row % 3
    else:
        tmp = 2 - ((row + 1) % 3)

    return 3 + tmp


def fill_first_land_in_row(row, previous_nodes):
    nodes = [0] * 6

    if row < 2:
        nodes[0] = previous_nodes[2] + 1
        nodes[3] = previous_nodes[3] + 5
    elif row == 2:
        nodes[0] = previous_nodes[2] + 1
        nodes[3] = previous_nodes[3] + 4
    else:
        nodes[0] = previous_nodes[2] + 2
        nodes[3] = previous_nodes[3] + 3

    for i in range(2):
        nodes[1 + i] = nodes[i] + 1
        nodes[4 + i] = nodes[3 + i] - 1

    return nodes


def fill_next_lands_in_row(row, land, lands_nodes):
    row_len = get_row_len(row)

    for i in range(1, row_len):
        nodes = [0]*6
        previous_nodes = lands_nodes[land-1]

        nodes[0] = previous_nodes[2]
        nodes[3] = previous_nodes[3] + 2

        for j in range(2):
            nodes[1+j] = nodes[j] + 1
            nodes[4+j] = nodes[3+j] - 1

        lands_nodes.append(nodes)
        land += 1

    return land


def fill_lands_nodes():
    land = 0
    lands_nodes = list()
    lands_nodes.append([1, 2, 3, 11, 10, 9])

    for i in range(5):

        if land != 0:
            nodes = fill_first_land_in_row(i, lands_nodes[land-1])
            lands_nodes.append(nodes)
        land += 1

        land = fill_next_lands_in_row(i, land, lands_nodes)

    return lands_nodes

