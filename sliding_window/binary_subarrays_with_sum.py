"""
Given a binary array nums and an integer goal, return the number of non-empty subarrays with a sum goal.

A subarray is a contiguous part of the array.



Example 1:

Input: nums = [1,0,1,0,1], goal = 2
Output: 4
Explanation: The 4 subarrays are bolded and underlined below:
[1,0,1,0,1]
[1,0,1,0,1]
[1,0,1,0,1]
[1,0,1,0,1]
Example 2:

Input: nums = [0,0,0,0,0], goal = 0
Output: 15


Constraints:

1 <= nums.length <= 3 * 104
nums[i] is either 0 or 1.
0 <= goal <= nums.length
"""

from typing import List

# Attempt 1: Using intuition


# class Solution:
#     def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
#         count = 0

#         for i in range(len(nums)):
#             j = i
#             s = 0
#             while j < len(nums):
#                 s += nums[j]
#                 if s > goal:
#                     break

#                 if s == goal:
#                     count += 1

#                 j += 1

#         return count


# Attempt 2: Sliding window, subarrays using a formula for length l => l(l+1) / 2
# This attempt is incorrect

# class Solution:
#     def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
#         count = 0
#         s = 0
#         i = j = 0

#         while j < len(nums):
#             s += nums[j]

#             while s > goal:
#                 s -= nums[i]
#                 if s == goal:
#                     count += 1
#                 i += 1

#             if s == goal:
#                 count += 1

#             j += 1

#         return count

# Attempt 3: Using hashmap for previous prefix lookup

# You main a hashmap of {seen prefix sum: freq}
# The idea is quite simple, you just have to ask:
# is there a previoud prefix sum that would equal to curr - goal?


class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        seen = {0: 1}
        pref = 0
        count = 0
        for n in nums:
            pref += n
            curr = pref - goal
            count += seen.get(curr, 0)
            seen[pref] = seen.get(pref, 0) + 1

        return count
