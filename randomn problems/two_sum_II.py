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


# Approach 1: Using a hashmap
class Solution:
    # def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
    #     seenNumbers = {}

    #     for index, num in enumerate(nums):

    #         if num in seenNumbers:
    #             seenIndex = seenNumbers[num]
    #             if abs(seenIndex - index) <= k:
    #                 return True

    #         seenNumbers[num] = index

    #     return False

    # Approach 2: Using a k fixed size hashmap with k size sliding window
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        seenNumbers = set()
        l = r = 0

        while r < len(nums):
            if r - l > k:
                seenNumbers.remove(nums[l])
                l += 1

            current_num = nums[r]

            if current_num in seenNumbers:
                return True

            seenNumbers.add(current_num)

            r += 1

        return False


if __name__ == "__main__":
    question = Solution()
    nums = [
        1,
        0,
        1,
        1,
    ]
    k = 1
    print(question.containsNearbyDuplicate(nums, k))
