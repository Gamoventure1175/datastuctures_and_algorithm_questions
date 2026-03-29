"""
Given an integer array nums, return the maximum possible sum of elements of the array such that it is divisible by three.



Example 1:

Input: nums = [3,6,5,1,8]
Output: 18
Explanation: Pick numbers 3, 6, 1 and 8 their sum is 18 (maximum sum divisible by 3).
Example 2:

Input: nums = [4]
Output: 0
Explanation: Since 4 is not divisible by 3, do not pick any number.
Example 3:

Input: nums = [1,2,3,4,4]
Output: 12
Explanation: Pick numbers 1, 3, 4 and 4 their sum is 12 (maximum sum divisible by 3).


Constraints:

1 <= nums.length <= 4 * 104
1 <= nums[i] <= 104
"""


# Approach 1: Using rmainders to map out what to remove
class Solution:
    def maxSumDivThree(self, nums: list[int]) -> int:
        total = sum(nums)
        rmd = total % 3

        if rmd == 0:
            return total

        mod1 = [n for n in nums if n % 3 == 1]
        mod2 = [n for n in nums if n % 3 == 2]
        mod1.sort()
        mod2.sort()

        if rmd == 1:
            remove1 = mod1[0] if mod1 else float("inf")
            remove2 = mod2[0] + mod2[1] if (len(mod2) >= 2) else float("inf")

        if rmd == 2:
            remove1 = mod1[0] + mod1[1] if (len(mod1) >= 2) else float("inf")
            remove2 = mod2[0] if mod2 else float("inf")

        return total - min(remove1, remove2)


if __name__ == "__main__":
    question = Solution()
    nums = [3, 6, 5, 1, 8]
    print(question.maxSumDivThree(nums))
