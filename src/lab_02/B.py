def check(matrix):
    if not matrix: return True
    k = len(matrix[0])
    for i in matrix:
        if len(i) != k: return False
    return True


def transpose(matrix: list[list[float | int]]) -> list[list]:
    if not check(matrix): return 'ValueError'
    if not matrix: return []
    new_list = []
    for i in range(len(matrix[0])):
        new_list.append([])
    for i in matrix:
        n = 0
        for j in i:
            new_list[n].append(j)
            n += 1
    return new_list


def row_sums(matrix: list[list[float | int]]) -> list[float]:
    if not check(matrix): return 'ValueError'
    if not matrix: return 'ValueError'
    new_list = []
    for i in matrix:
        new_list.append(sum(i))
    return new_list


def col_sums(matrix: list[list[float | int]]) -> list[float]:
    if not check(matrix): return 'ValueError'
    if not matrix: return 'ValueError'
    new_list1 = []
    if type(matrix[0]) != list: return matrix
    for i in range(len(matrix[0])):
        new_list1.append([])
    for i in matrix:
        for k in range(len(i)):
            new_list1[k].append(i[k])
            new_list = []
    for i in new_list1:
        new_list.append(sum(i))
    return new_list


print('[[1, 2, 3]] -', transpose([[1, 2, 3]]))
print('[[1], [2], [3]]  -', transpose([[1], [2], [3]] ))
print('[[1, 2], [3, 4]] -', transpose([[1, 2], [3, 4]]))
print('[] -', transpose([]))
print('[[1, 2], [3]] -', transpose([[1, 2], [3]]))

print()
print()
print()
print()
print()

print('[[1, 2, 3], [4, 5, 6]] -', row_sums([[1, 2, 3], [4, 5, 6]]))
print('[[-1, 1], [10, -10]]  -', row_sums([[-1, 1], [10, -10]]))
print('[[0, 0], [0, 0]] -', row_sums([[0, 0], [0, 0]]))
print('[] -', row_sums([]))
print('[[1, 2], [3]] -', row_sums([[1, 2], [3]]))

print()
print()
print()
print()
print()


print('[[1, 2, 3], [4, 5, 6]] -', col_sums([[1, 2, 3], [4, 5, 6]]))
print('[[-1, 1], [10, -10]]  -', col_sums([[-1, 1], [10, -10]]))
print('[[0, 0], [0, 0]] -', col_sums([[0, 0], [0, 0]]))
print('[] -', col_sums([]))
print('[[1, 2], [3]] -', col_sums([[1, 2], [3]]))

print()
print()
print()
print()
print()