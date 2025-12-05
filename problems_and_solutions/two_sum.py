"""
Given an array of integers nums and an integer target, return the indices i and j such that nums[i] + nums[j] == target and i != j.

You may assume that every input has exactly one pair of indices i and j that satisfy the condition.

Return the answer with the smaller index first.

Example 1:

Input:
nums = [3,4,5,6], target = 7

Output: [0,1]
Explanation: nums[0] + nums[1] == 7, so we return [0, 1].

Example 2:

Input: nums = [4,5,6], target = 10

Output: [0,2]
Example 3:

Input: nums = [5,5], target = 10

Output: [0,1]
"""

# I have tried the brute force method already getting a worst case o(n**2) time complexity which is pretty bad.

# I will directly jump into to finding a better solution right a way


# Approach 2: Assuming that the pairs of indexes are consequtive? (❌ - doesn't work)

"""
If we assume that the pairs of indexes are consequtive, we can get a very simple solution to this problem as follows:
"""


# def twoSum(nums: list[int], target: int):
#     for i in range(1, len(nums)):
#         if nums[i - 1] + nums[i] == target:
#             return (i - 1, i)
#         return False


if __name__ == "__main__":
    nums = [4, 5, 6]
    target = 10

    # print(twoSum(nums, target))
