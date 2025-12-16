"""

Search a 2D Matrix
You are given an m x n 2-D integer array matrix and an integer target.

Each row in matrix is sorted in non-decreasing order.
The first integer of every row is greater than the last integer of the previous row.
Return true if target exists within matrix or false otherwise.

Can you write a solution that runs in O(log(m * n)) time?

Example 1:

[Example 1 diagram](https://imagedelivery.net/CLfkmk9Wzy8_9HRyug4EVA/7ca61f56-00d4-4fa0-26cf-56809028ac00/public)

Input: matrix = [[1,2,4,8],[10,11,12,13],[14,20,30,40]], target = 10

Output: true
Example 2:

[Example 2 diagram](https://imagedelivery.net/CLfkmk9Wzy8_9HRyug4EVA/f25f2085-ce04-4447-9cee-f0a66c32a300/public)

Input: matrix = [[1,2,4,8],[10,11,12,13],[14,20,30,40]], target = 15

Output: false
Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 100
-10000 <= matrix[i][j], target <= 10000
"""

# Approach 1: Using binary search within another binary search


def exists_in_row(nums: list[int], target: int) -> bool:
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return True
        elif target < nums[mid]:
            right = mid - 1
        else:
            left = mid + 1

    return False


def search_2d_matrix(matrix: list[list[int]], target: int) -> bool:
    left = 0
    right = len(matrix) - 1

    while left <= right:
        mid = (left + right) // 2

        if target < matrix[mid][0]:
            right = mid - 1

        elif target > matrix[mid][-1]:
            left = mid + 1

        else:
            exists_in_row(matrix[mid], target)

    return False


if __name__ == "__main__":
    matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
    target = 13

    print(search_2d_matrix(matrix, target))
