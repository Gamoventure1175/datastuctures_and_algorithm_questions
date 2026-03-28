"""
Given an unsorted integer array nums. Return the smallest positive integer that is not present in nums.

You must implement an algorithm that runs in O(n) time and uses O(1) auxiliary space.



Example 1:

Input: nums = [1,2,0]
Output: 3
Explanation: The numbers in the range [1,2] are all in the array.
Example 2:

Input: nums = [3,4,-1,1]
Output: 2
Explanation: 1 is in the array but 2 is missing.
Example 3:

Input: nums = [7,8,9,11,12]
Output: 1
Explanation: The smallest positive integer 1 is missing.


Constraints:

1 <= nums.length <= 105
-231 <= nums[i] <= 231 - 1=
"""

# Approach 1: Using O(n) extra space
# class Solution:
#     def firstMissingPositive(self, nums: list[int]) -> int:
#         positives = {n for n in nums if n > 0}
#         if not positives:
#             return 1

#         smallest_positive = float("inf")

#         for n in positives:
#             if n > 0 and (n - 1 not in positives):
#                 smallest_positive = min(smallest_positive, n)

#         if smallest_positive != 1:
#             return 1

#         while smallest_positive in positives:
#             smallest_positive += 1

#         return int(smallest_positive)


# Approach 2: Solution lies in  the range 1 to n+1
class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:
        existing = set(nums)

        for n in range(1, len(nums) + 2):
            if n not in existing:
                return n


if __name__ == "__main__":
    question = Solution()
    nums = [1]
    print(question.firstMissingPositive(nums))
