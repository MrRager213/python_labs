def min_max(matrix):
    if not matrix: return 'ValueError'
    new_list = []
    for i in matrix:
        new_list.append(i)
    return (min(new_list), max(new_list))


def unique_sorted(matrix):
    if not matrix: return 'ValueError'
    new_list = sorted(list(set(matrix)))
    return new_list


def flatten(matrix):
    new_list = []
    for i in matrix:
        if type(i) != list:
            if type(i) == tuple: new_list += list(i)
            else: return 'ValueError'
        else: new_list += i
    return new_list