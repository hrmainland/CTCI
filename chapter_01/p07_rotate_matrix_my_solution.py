# My solution to p07_rotate_matrix.py


def inner_rotate(matrix):
    tmp = None
    for layer in range(len(matrix) // 2):
        final = len(matrix) - 1 - layer
        for i in range(final - layer):
            coords = [
                (layer, i + layer),
                (i + layer, final),
                (final, final - i),
                (final - i, layer),
            ]
            start = coords[0]
            tmp = matrix[start[0]][start[1]]
            j = -1
            while j > -4:
                this_coords = coords[j]
                next_coords = coords[j + 1]
                matrix[next_coords[0]][next_coords[1]] = matrix[this_coords[0]][
                    this_coords[1]
                ]
                j -= 1
            first = coords[1]
            matrix[first[0]][first[1]] = tmp


# 0000111000-1-1-1000111000-1-1-1
# 111000-1-1-1000111000-1-1-1000

# def rotate(matrix):
#     for _ in range(len(matrix) - 1):
#         for i in range(len(matrix) // 2):
#             inner_rotate(matrix, i, i, len(matrix) - 2 * i)


matrix = [[1, 2, 3, 4],
          [1, 2, 3, 4],
          [1, 2, 3, 4],
          [1, 2, 3, 4]]

matrix =             [
                [21, 16, 11, 6, 1],
                [22, 17, 12, 7, 2],
                [23, 18, 13, 8, 3],
                [24, 19, 14, 9, 4],
                [25, 20, 15, 10, 5],
            ]

inner_rotate(matrix)
for row in matrix:
    print(row)

# rotate(matrix)
# for row in matrix:
#     print(row)
