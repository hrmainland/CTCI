# My solution to p12_eight_queens.py


def n_queens(n):
    board = [["_" for _ in range(n)] for _ in range(n)]

    def is_available(row, col):
        for crow in range(row):
            if board[crow][col] == "Q":
                return False

        vectors = [(-1, -1), (-1, 1)]
        original_row, original_col = row, col
        for crow, ccol in vectors:
            row, col = original_row, original_col
            while 0 <= row < len(board) and 0 <= col < len(board[0]):
                if board[row][col] == "Q":
                    return False
                row, col = row + crow, col + ccol

        return True

    result = 0

    def dfs(row):
        if row == len(board):
            result += 1
            # for row in board:
            #     print(row)
            # print()
            # return True
        for col in range(len(board[row])):
            if is_available(row, col):
                board[row][col] = "Q"
                dfs(row + 1)
                board[row][col] = "_"
        return False

    dfs(0)
    return result


result = n_queens(15)
