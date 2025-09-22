"""
Longest Consecutive Sequence
Given an array of integers nums, return the length of the longest consecutive sequence
of elements that can be formed.

A consecutive sequence is a sequence of elements in which each element is exactly 1 greater
than the previous element. The elements do not have to be consecutive in the original array.

You must write an algorithm that runs in O(n) time.

Example 1:

Input: nums = [2,20,4,10,3,4,5]

Output: 4
Explanation: The longest consecutive sequence is [2, 3, 4, 5].

Example 2:
Input: nums = [0,3,2,5,4,6,1,1]

Output: 7


Constraints:

0 <= nums.length <= 1000
-10^9 <= nums[i] <= 10^9
"""

# Approach 1: Brute force approach


class Solution:
    def longestConsequtive(self, nums: list[int]) -> int:
        """Find longest consequtive sequence

        Given a list of numbers, finds the longest
        sequence of consequtive numbers and returns it's length

        Args:
            nums (list[int]): list of integers

        Returns:
            int: length of the the longest sequence
        """

        if len(nums) == 0:
            return 0

        if len(nums) == 1:
            return 1

        final_length = 0

        for num in set(nums):
            length_counter = 1
            for i in range(1, len(nums)):
                if num + i in nums:
                    length_counter += 1
                    continue
                break

            final_length = (
                length_counter if (length_counter > final_length) else final_length
            )

        return final_length


if __name__ == "__main__":
    test = [1000000, 999999, 999998, -1000000]
    solution = Solution()
    print(solution.longestConsequtive(test))
