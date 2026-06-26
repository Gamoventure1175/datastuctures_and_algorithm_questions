"""
You are given an integer array nums and two integers indexDiff and valueDiff.

Find a pair of indices (i, j) such that:

i != j,
abs(i - j) <= indexDiff.
abs(nums[i] - nums[j]) <= valueDiff, and
Return true if such pair exists or false otherwise.



Example 1:

Input: nums = [1,2,3,1], indexDiff = 3, valueDiff = 0
Output: true
Explanation: We can choose (i, j) = (0, 3).
We satisfy the three conditions:
i != j --> 0 != 3
abs(i - j) <= indexDiff --> abs(0 - 3) <= 3
abs(nums[i] - nums[j]) <= valueDiff --> abs(1 - 1) <= 0
Example 2:

Input: nums = [1,5,9,1,5,9], indexDiff = 2, valueDiff = 3
Output: false
Explanation: After trying all the possible pairs (i, j), we cannot satisfy the three conditions, so we return false.


Constraints:

2 <= nums.length <= 105
-109 <= nums[i] <= 109
1 <= indexDiff <= nums.length
0 <= valueDiff <= 109
"""

from typing import Dict, List

# Attempt 1: Using intuition


# class Solution:
#     def containsNearbyAlmostDuplicate(
#         self, nums: List[int], indexDiff: int, valueDiff: int
#     ) -> bool:
#         i = j = 0

#         while j < len(nums):

#             while j - i > indexDiff:
#                 i += 1

#             for temp in range(i, j):
#                 if abs(nums[temp] - nums[j]) <= valueDiff:
#                     return True
#             j += 1
#         return False


# Attempt 2: Using a sorted bucket kind of
# This is wrong
# class Solution:
#     def containsNearbyAlmostDuplicate(
#         self, nums: List[int], indexDiff: int, valueDiff: int
#     ) -> bool:
#         i = j = 0
#         bucket: Dict[int, list] = {}
#         while j < len(nums):

#             while j - i > indexDiff:
#                 i += 1

#             diff = abs(nums[j] - nums[i])
#             if bucket.get(diff):
#                 bucket.get(diff).append((i, j))

#             else:
#                 bucket[diff] = []
#                 bucket[diff].append((i, j))

#             j += 1

#         if bucket.get(valueDiff):
#             return True

#         return False


class Solution:
    def containsNearbyAlmostDuplicate(
        self, nums: List[int], indexDiff: int, valueDiff: int
    ) -> bool:
        buckets = {}
        width = valueDiff + 1
        left = right = 0

        while right < len(nums):
            if (right - left) > indexDiff:
                key = nums[left] // width
                del buckets[key]
                left += 1

            key = nums[right] // width

            if key in buckets:
                return True

            if key - 1 in buckets:
                if abs(nums[right] - buckets[key - 1]) <= valueDiff:
                    return True

            if key + 1 in buckets:
                if abs(nums[right] - buckets[key + 1]) <= valueDiff:
                    return True

            buckets[key] = nums[right]

            right += 1

        return False


print(Solution.containsNearbyAlmostDuplicate(Solution(), [1, 2, 3, 1], 3, 0))
