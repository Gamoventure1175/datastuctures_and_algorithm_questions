"""
Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.

Example 1:

Input: nums = [1, 2, 3, 3]

Output: true

Example 2:

Input: nums = [1, 2, 3, 4]

Output: false
"""

# Approach 1 : Using sets and early exit strategy


def hasDuplicate(nums):

    existing_nums = set()

    for num in nums:
        if num in existing_nums:
            return True
        existing_nums.add(num)

    return False
