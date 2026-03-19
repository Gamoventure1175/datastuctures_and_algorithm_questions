class Solution:
    def search(self, nums: list[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return True

            elif nums[mid] > target:
                r = mid - 1

            else:
                l = mid + 1

        return False

    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        l, r = 0, len(matrix) - 1

        while l <= r:
            mid = (l + r) // 2

            if matrix[mid][0] >= target >= matrix[mid][-1]:
                return

            elif target < matrix[mid][0]:
                r = mid - 1

            else:
                l = mid + 1
