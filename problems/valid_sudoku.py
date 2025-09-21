"""
Valid Sudoku

You are given a 9 x 9 Sudoku board board. A Sudoku board is valid if the
following rules are followed:

    Each row must contain the digits 1-9 without duplicates.
    Each column must contain the digits 1-9 without duplicates.
    Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without duplicates.

Return true if the Sudoku board is valid, otherwise return false

Note: A board does not need to be full or be solvable to be valid.

Example 1:
Input: board =
[["1","2",".",".","3",".",".",".","."],
 ["4",".",".","5",".",".",".",".","."],
 [".","9","8",".",".",".",".",".","3"],
 ["5",".",".",".","6",".",".",".","4"],
 [".",".",".","8",".","3",".",".","5"],
 ["7",".",".",".","2",".",".",".","6"],
 [".",".",".",".",".",".","2",".","."],
 [".",".",".","4","1","9",".",".","8"],
 [".",".",".",".","8",".",".","7","9"]]

Output: true

Example 2:

Input: board =
[["1","2",".",".","3",".",".",".","."],
 ["4",".",".","5",".",".",".",".","."],
 [".","9","1",".",".",".",".",".","3"],
 ["5",".",".",".","6",".",".",".","4"],
 [".",".",".","8",".","3",".",".","5"],
 ["7",".",".",".","2",".",".",".","6"],
 [".",".",".",".",".",".","2",".","."],
 [".",".",".","4","1","9",".",".","8"],
 [".",".",".",".","8",".",".","7","9"]]

Output: false
Explanation: There are two 1's in the top-left 3x3 sub-box.
"""


class Solution:
    """
    Solution for the proposed dsa problem
    """

    def is_valid_sudoku(self, board: list[list[str]]) -> bool:
        """
        Checks if a sudoku board is valid.

        The function follows 3 rules to verify that a sudoku board is valid:
            1. Each row must contain the digits 1-9 without duplicates.
            2. Each column must contain the digits 1-9 without duplicates.
            3. Each of the nine 3 x 3 sub-boxes of the grid must contain the digits
            1-9 without duplicates.

        Args:
            board (list[list[str]]): 2D matrix style sudoku board of size 9x9

        Returns:
            bool: True or False based on the validity of the board
        """

        # Row wise test
        for row in board:
            row_numbers = []
            row_numbers_freq = {}

            for i in range(9):
                if row[i].isdigit():
                    row_numbers.append(row[i])

                    if row_numbers_freq.get(row[i]):
                        row_numbers_freq[row[i]] += 1
                    else:
                        row_numbers_freq[row[i]] = 1

            if len(row_numbers) != len(row_numbers_freq):
                return False

        # Column wise test
        for c in range(9):
            col_numbers = []
            col_numbers_freq = {}

            for r in range(9):
                if board[r][c].isdigit():
                    print(f"Element: {board[r][c]}")
                    col_numbers.append(board[r][c])

                    if col_numbers_freq.get(board[r][c]):
                        col_numbers_freq[board[r][c]] += 1
                    else:
                        col_numbers_freq[board[r][c]] = 1

            if len(col_numbers) != len(col_numbers_freq):
                return False

        # 3x3 sub-box wise test
        sub_boxes = [
            [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)],
            [(0, 3), (0, 4), (0, 5), (1, 3), (1, 4), (1, 5), (2, 3), (2, 4), (2, 5)],
            [(0, 6), (0, 7), (0, 8), (1, 6), (1, 7), (1, 8), (2, 6), (2, 7), (2, 8)],
            [(3, 0), (3, 1), (3, 2), (4, 0), (4, 1), (4, 2), (5, 0), (5, 1), (5, 2)],
            [(3, 3), (3, 4), (3, 5), (4, 3), (4, 4), (4, 5), (5, 3), (5, 4), (5, 5)],
            [(3, 6), (3, 7), (3, 8), (4, 6), (4, 7), (4, 8), (5, 6), (5, 7), (5, 8)],
            [(6, 0), (6, 1), (6, 2), (7, 0), (7, 1), (7, 2), (8, 0), (8, 1), (8, 2)],
            [(6, 3), (6, 4), (6, 5), (7, 3), (7, 4), (7, 5), (8, 3), (8, 4), (8, 5)],
            [(6, 6), (6, 7), (6, 8), (7, 6), (7, 7), (7, 8), (8, 6), (8, 7), (8, 8)],
        ]

        for sub_box in sub_boxes:
            box_numbers = []
            box_numbers_freq = {}

            for i, j in sub_box:
                if board[i][j].isdigit():
                    box_numbers.append(board[i][j])
                    if box_numbers_freq.get(board[i][j]):
                        box_numbers_freq[board[i][j]] += 1
                    else:
                        box_numbers_freq[board[i][j]] = 1

            if len(box_numbers) != len(box_numbers_freq):
                return False

        return True


if __name__ == "__main__":
    solution = Solution()

    board = [
        [".", ".", "4", ".", ".", ".", "6", "3", "."],
        [".", ".", ".", ".", ".", ".", ".", ".", "."],
        ["5", ".", ".", ".", ".", ".", ".", "9", "."],
        [".", ".", ".", "5", "6", ".", ".", ".", "."],
        ["4", ".", "3", ".", ".", ".", ".", ".", "1"],
        [".", ".", ".", "7", ".", ".", ".", ".", "."],
        [".", ".", ".", "5", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", ".", "."],
    ]

    print(solution.is_valid_sudoku(board))
