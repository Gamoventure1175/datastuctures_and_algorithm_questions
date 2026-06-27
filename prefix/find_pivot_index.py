"""
Given an array of integers nums, calculate the pivot index of this array.

The pivot index is the index where the sum of all the numbers strictly to the left of the index is equal to the sum of all the numbers strictly to the index's right.

If the index is on the left edge of the array, then the left sum is 0 because there are no elements to the left. This also applies to the right edge of the array.

Return the leftmost pivot index. If no such index exists, return -1.



Example 1:

Input: nums = [1,7,3,6,5,6]
Output: 3
Explanation:
The pivot index is 3.
Left sum = nums[0] + nums[1] + nums[2] = 1 + 7 + 3 = 11
Right sum = nums[4] + nums[5] = 5 + 6 = 11
Example 2:

Input: nums = [1,2,3]
Output: -1
Explanation:
There is no index that satisfies the conditions in the problem statement.
Example 3:

Input: nums = [2,1,-1]
Output: 0
Explanation:
The pivot index is 0.
Left sum = 0 (no elements to the left of index 0)
Right sum = nums[1] + nums[2] = 1 + -1 = 0


Constraints:

1 <= nums.length <= 104
-1000 <= nums[i] <= 1000

"""

from typing import List

# Attempt 1: Using the monotonic property of a prefix summation
# This solution does not work because the prefix that the solution
# relies on is actually not monotonic in nature.

# class Solution:
#     def pivotIndex(self, nums: List[int]) -> int:
#         # Assume that the index is the middle one
#         l = len(nums)
#         m = l // 2

#         prefix = []
#         temp = 0
#         for n in nums:
#             temp += n
#             prefix.append(temp)

#         while 0 <= m < l:
#             leftValue = 0 if (m-1) == -1 else prefix[m-1]
#             rightValue = prefix[l-1] - prefix[m]

#             if leftValue == rightValue:
#                 return m

#             elif leftValue < rightValue:
#                 m += 1

#             else:
#                 m-=1

#         return -1


# Attempt 2: Creating sumLeft and sumRight


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        l = len(nums)
        sumLeft = []
        sumRight = [0] * l
        temp = 0
        for n in nums:
            sumLeft.append(temp)
            temp += n

        temp = 0
        for i in range(-1, -l - 1, -1):
            sumRight[i] = temp
            temp += nums[i]

        for i in range(l):
            if sumLeft[i] == sumRight[i]:
                return i

        return -1
