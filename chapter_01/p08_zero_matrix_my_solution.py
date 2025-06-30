# My solution to p08_zero_matrix.py
def my_sol(matrix):
    rows = set()
    cols = set()
    for i, row in enumerate(matrix):
        for j, elem in enumerate(row):
            if elem == 0:
                rows.add(i)
                cols.add(j)

    for row_index in rows:
        matrix[row_index] = [0] * len(matrix[0])
    for col_index in cols:
        for i in range(len(matrix)):
            matrix[i][col_index] = 0
    return matrix


matrix = [[0, 2, 3], 
          [1, 2, 3], 
          [1, 2, 0], 
          [1, 2, 3]]

my_sol(matrix)
print(matrix)
