# How does a matrix work?

from typing import Sequence


simple_3x3_matrix = [[0, 0, 0] for i in range(3)]
# print(simple_3x3_matrix)

for i in range(len(simple_3x3_matrix)):
    for j in range(len(simple_3x3_matrix[0])):
        # print(i, j)
        ...


# Defining rows and columns and then creating a matrix
rows = cols = 3
s_3x3_matrix = [[_ for _ in range(rows)] for _ in range(cols)]
# print(s_3x3_matrix)


# Travelling a matrix
s_3x3_matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]

#      0th  1st  2nd
#    0th[    |    ]
#    1st[    |    ]
#    2nd[    |    ]

# How to travel a specific row ?
row_number = 1
# idea being that range(Ith row, Ith + 1)
for i in range(row_number, row_number + 1):  # O(n) btw
    row = []
    for j in range(len(s_3x3_matrix[0])):
        row.append(s_3x3_matrix[i][j])
    # print(row)


# How to travel a specific column ?
column_number = 1
for i in range(column_number, column_number + 1):  # O(n) btw
    column = []
    for j in range(len(s_3x3_matrix)):
        column.append(s_3x3_matrix[j][i])
    # print(column)


# Is it possible to do both the traversal at the same time ?
# Suppose a pair of i, j is given, it possible to travel:
#       ith row
#       jth column at the same time
# at the same time ?


# Like travelling 0th row and 1st column?
#        0th  1st  2nd
#    0th[ *    *    * ]
#    1st[      *      ]
#    2nd[      *      ]

# [
#     [1,2,3],
#     [4,5,6],
#     [7,8,9],
# ]

# i, j
pair = (0, 2)

i, j = pair

row = []
column = []

for value in range(len(s_3x3_matrix[0])):
    row.append(s_3x3_matrix[i][value])

for value in range(len(s_3x3_matrix)):
    column.append(s_3x3_matrix[value][j])

# print(f"{i}th row = {row}")
# print(f"{j}th column = {column}")


# The actual question

# Given a boolean matrix mat where each cell contains either 0 or 1,
# the task is to modify it such that if a matrix cell matrix[i][j] is 1
# then all the cells in its ith row and jth column will become 1.

# Examples:

# Input:  [[1, 0],
#           [0, 0]]
# Output: [[1, 1],
#          [1, 0]]


def boolean_matrix(mat: list[list[int]]):
    """Takes a matrix of nxn size where each cell contains only boolean values (1, 0)
    and modifies it such that if a matrix cell [i][j] is 1 then all the cells in its ith row
    and jth column will become 1"""
    res = mat.copy()
    l_rows = len(mat)
    l_cols = len(mat[0])

    pairs = list()

    for i in range(l_rows):
        for j in range(l_cols):
            if mat[i][j] == 1:
                pairs.append((i, j))  # O(n^2)

    for pair in pairs:
        i, j = pair
        for k in range(l_cols):
            res[i][k] = 1
        for k in range(l_rows):
            res[k][j] = 1

    return res


if __name__ == "__main__":
    example = [
            [1, 0, 0, 1],
            [0, 0, 1, 0],
            [0, 0, 0, 0]
        ]

    res = boolean_matrix(example)
    for i in res:
        print(i)
    
