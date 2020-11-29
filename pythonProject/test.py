import numpy as np
np.full((5, 5), np.inf)


size = int(input())
matrix = []*size
print(matrix)

for i in range(size):
    for j in range(size):
        matrix.append(j)
    # matrix.append([])

print(matrix)


matrix = [
    [0, 1, 2, 3, 4],
    [0, 1, 2, 3, 4],
    [0, 1, 2, 3, 4],
    [0, 1, 2, 3, 4],
    [0, 1, 2, 3, 4]
]
counter = 0
for row in range(5):
    for col in range(5):
        if row == 0 and col == 0:
            matrix[row][col] = func()
            counter += 1
        elif col != 0:
            collor = func()
            counter += 1
            while matrix[row][col - 1] == collor:
                collor = func()
                counter += 1
            matrix[row][col] = collor
        elif row != 0:
            if col == 0:
                collor = fun()
                counter += 1
                while matrix[row - 1][col] == collor:
                    collor = fun()
                    counter += 1
                matrix[row][col] = collor
            elif col != 0:
                collor = fun()
                counter += 1
                while matrix[row - 1][col] == collor or matrix[row][col - 1] == collor:
                    collor = fun()
                    counter += 1
                matrix[row][col] = collor
