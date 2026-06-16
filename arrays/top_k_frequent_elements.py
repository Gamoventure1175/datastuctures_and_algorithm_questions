"""
Given an integer array nums and an integer k, return the k most frequent elements within the array.

The test cases are generated such that the answer is always unique.

You may return the output in any order.

Example 1:

Input: nums = [1,2,2,3,3,3], k = 2

Output: [2,3]
Example 2:

Input: nums = [7,7], k = 1

Output: [7]
Constraints:

1 <= nums.length <= 10^4.
-1000 <= nums[i] <= 1000
1 <= k <= number of distinct elements in nums.
"""

from typing import List

# Using a heap with O(n log k) time complexity and O(n) space complexity


# class Solution:
#     def topKFrequent(self, nums: List[int], k: int) -> List[int]:
#         freq = {}
#         for num in nums:
#             freq[num] = freq.get(num, 0) + 1
#         return sorted(freq, key=lambda x: freq[x], reverse=True)[:k]

# Using a heap with array buckets to get O(n) time complexity and O(n) space complexity


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        buckets = [[] for _ in range(len(nums) + 1)]
        for num, count in freq.items():
            buckets[count].append(num)

        result = []
        for i in range(len(buckets) - 1, 0, -1):
            if buckets[i]:
                result.extend(buckets[i])
                if len(result) >= k:
                    break

        return result[:k]


if __name__ == "__main__":
    solution = Solution()
    print(solution.topKFrequent([1, 2, 2, 3, 3, 3], 2))  # Output: [2, 3]
    print(solution.topKFrequent([7, 7], 1))  # Output: [7]
