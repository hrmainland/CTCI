from itertools import product


def horizontal_is_valid(board, row):
    array = [elem for elem in board[row] if elem]
    return len(set(array)) == len(array)


def vertical_is_valid(board, col):
    array = [row[col] for row in board if row[col]]
    return len(set(array)) == len(array)


def box_is_valid(board, row, col):
    mid_row = 3 * (row // 3) + 1
    mid_col = 3 * (col // 3) + 1
    vectors = product(range(-1, 2), repeat=2)
    array = [
        board[mid_row + row][mid_col + col]
        for row, col in vectors
        if board[mid_row + row][mid_col + col]
    ]
    return len(set(array)) == len(array)


def is_valid(board, row, col):
    return (
        horizontal_is_valid(board, row)
        and vertical_is_valid(board, col)
        and box_is_valid(board, row, col)
    )


def search(board, row, col):
    if board[row][col]:
        if row == col == 8:
            return True
        return search(board, row + int(bool(col == 8)), (col + 1) % 9)
    for number in range(1, 10):
        board[row][col] = number
        if is_valid(board, row, col):
            if row == col == 8:
                return True
            next_valid = search(board, row + int(bool(col == 8)), (col + 1) % 9)
            if next_valid:
                return next_valid
    board[row][col] = 0
    return False


sudoku_easy = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9],
]

sudoku_hard = [
    [0, 0, 0, 0, 0, 0, 0, 1, 2],
    [0, 0, 0, 0, 0, 7, 0, 0, 0],
    [0, 0, 1, 0, 9, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 4, 0, 0],
    [0, 0, 5, 0, 0, 0, 3, 0, 0],
    [0, 0, 2, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 4, 0, 1, 0, 0],
    [0, 0, 0, 9, 0, 0, 0, 0, 0],
    [6, 7, 0, 0, 0, 0, 0, 0, 0],
]

result = search(sudoku_hard, 0, 0)
print(result)
for row in sudoku_hard:
    print(row)

for result in product(range(-1, 2), repeat=2):
    print(result)
