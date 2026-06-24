"""

Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.



Example 1:

Input: nums = [1,2,3,1], k = 3
Output: true
Example 2:

Input: nums = [1,0,1,1], k = 1
Output: true
Example 3:

Input: nums = [1,2,3,1,2,3], k = 2
Output: false


Constraints:

1 <= nums.length <= 105
-109 <= nums[i] <= 109
0 <= k <= 105

"""

from typing import List

# Attempt 1: Using intuition


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        i = 0
        window = set()

        for j in range(len(nums)):
            if j - i > k:
                window.remove(nums[i])
                i += 1

            if nums[j] in window:
                return True

            window.add(nums[j])

        return False


# A cleaner version
# class Solution:
#     def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
#         window = set()

#         for i, num in enumerate(nums):

#             if num in window:
#                 return True

#             window.add(num)

#             if len(window) > k:
#                 window.remove(nums[i - k])

#         return False
