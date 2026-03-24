"""
Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

A subarray is a contiguous non-empty sequence of elements within an array.



Example 1:

Input: nums = [1,1,1], k = 2
Output: 2
Example 2:

Input: nums = [1,2,3], k = 3
Output: 2


Constraints:

1 <= nums.length <= 2 * 104
-1000 <= nums[i] <= 1000
-107 <= k <= 107
"""


class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
        prefix = [0] * (len(nums) + 1)

        for i in range(len(nums)):
            prefix[i + 1] = prefix[i] + nums[i]

        count = 0
        prefix_freq = {}

        for index, _ in enumerate(nums):
            target = prefix[index + 1] - k
            if target in prefix_freq:
                count += 1
                prefix_freq[target] += 1
                continue

            prefix_freq[target] = 1

        return count


if __name__ == "__main__":
    question = Solution()
    nums = [1, 2, 3]
    k = 3
    print(question.subarraySum(nums, k))
