# Given a square matrix mat[][] of size n x n, such that mat[i][j] = 1 means ith person
# knows jth person, the task is to find the celebrity. A celebrity is a person who is known
# to all but does not know anyone. Return the index of the celebrity, if there is no celebrity return -1.

# Note: Follow 0-based indexing and mat[i][i] will always be 1.

# Examples:

# Input: mat[][] = [[1, 1, 0],
#                   [0, 1, 0],
#                   [0, 1, 1]]
# Output: 1
# Explanation: 0th and 2nd person both know 1. Therefore, 1 is the celebrity.

# Input: mat[][] = [[1, 1],
#                   [1, 1]]


# The matrix of n*n size is like map of people's connection with other people
# The connection can be understood in the following way ->
# [
#     [1, 1, 0, 1], -> 0th person (for the matrix)
#     [0, 1, 0, 1], -> 1st person
#     [1, 1, 1, 1], -> 2nd person
#     [0, 0, 0, 1]  -> 3rd person
# ]

# Someone is called a celebrity if all the other person know them but they don't know anyone
# In other words, the celebrity should only know themselves while other people will know themselves as well as the celebrity

# How to mark if a person knows someone?
#       if a person knows someone -> denoted by 1
#       if a person does not know someone -> denoted by 0

# From the example, to say that 0th person knows 3rd person would mean that matrix[0][3] = 1
# [
#     [1, 1, 0, 1], -> 0th person (for the matrix)
#     [0, 1, 0, 1], -> 1st person
#     [1, 1, 1, 1], -> 2nd person
#     [0, 0, 0, 1] -> 3rd person
# ]

# So for a celebrity c, the following conditions must apply:
#       for i != c, matrix[i][c] == 1 -> all the persons should know c
#       for j != c, matric[c][j] == 0 -> c should not know anyone else except themselves


# The following is a brute force method using loops with overall complexity
# of o(n^2) for its functioning and a space complexity of o(1)
def celebrity_finder(mat: list[list[int]]):
    """Take any n*n matrix with 1 and 0 representing the connection between
    the persons by denoting 1 if they know an person and 0 if they don't know
    the person and return the index of a celebrity person if they exist in the matrix

    Conditions for the celebrity c:
        1.  for i != c, matrix[i][c] == 1 -> all the persons should know c
        2.  for j != c, matric[c][j] == 0 -> c should not know anyone else except themselves
    """
    n = len(mat)

    celeb_index = 0

    if n == 1:
        return -1

    c = 0
    while c < len(mat):
        celeb = True
        for i in range(n):
            if i == c:
                continue
            elif mat[i][c] != 1:
                celeb = False
                break
        if celeb:
            for j in range(n):
                if j == c:
                    celeb_index = c
                    continue
                elif mat[c][j] != 0:
                    celeb = False
                    celeb_index = 0
                    break

        if celeb:
            return celeb_index
        c += 1

    return -1


# Another approach I thought of using 2 loops


def celebrity_finder_simplified(mat: list[list[int]]):

    if len(mat) == 1:
        return -1

    for c in range(len(mat)):
        celeb = True
        for i in range(len(mat)):
            if i != c and (mat[i][c] != 1 or mat[c][i] != 0):
                celeb = False
                break
        if celeb == True:
            return c
    return -1


if __name__ == "__main__":
    example = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]

    print(celebrity_finder(example))

    mat = [[1, 0, 1, 0], [0, 1, 1, 0], [0, 0, 1, 0], [1, 1, 1, 1]]

    mat_7x7 = [
        [1, 0, 0, 1, 0, 0, 0],
        [0, 1, 0, 1, 0, 0, 0],
        [0, 0, 1, 1, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0],  # <- Celebrity
        [0, 0, 0, 1, 1, 0, 0],
        [0, 0, 0, 1, 0, 1, 0],
        [0, 0, 0, 1, 0, 0, 1],
    ]

    mat_6x6 = [
        [1, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [1, 1, 1, 0, 0, 0],
        [0, 0, 1, 1, 0, 0],
        [0, 0, 0, 1, 1, 1],
        [0, 0, 0, 1, 0, 1],
    ]

    print(celebrity_finder_simplified(mat_7x7))
