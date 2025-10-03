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



print('[3, -1, 5, 5, 0] -', min_max([3, -1, 5, 5, 0]))
print('[42] -', min_max([42]))
print('[-5, -2, -9] -', min_max([-5, -2, -9]))
print('[] -', min_max([]))
print('[1.5, 2, 2.0, -3.1] -', min_max([1.5, 2, 2.0, -3.1]))

print()
print()
print()

print('[3, 1, 2, 1, 3] -', unique_sorted([3, 1, 2, 1, 3]))
print('[] -', unique_sorted([]))
print('[-1, -1, 0, 2, 2] -', unique_sorted([-1, -1, 0, 2, 2]))
print('[1.0, 1, 2.5, 2.5, 0] -', unique_sorted([1.0, 1, 2.5, 2.5, 0]))

print()
print()
print()

print('[[1, 2], [3, 4]] -', flatten([[1, 2], [3, 4]]))
print('[[1, 2], (3, 4, 5)] -', flatten([[1, 2], (3, 4, 5)]))
print('[[1], [], [2, 3]] -', flatten([[1], [], [2, 3]]))
print('[[1, 2], "ab"] -', flatten([[1, 2], "ab"]))