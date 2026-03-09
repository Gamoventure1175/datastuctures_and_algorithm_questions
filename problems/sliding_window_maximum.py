"""
Return a list that contains the maximum element in the window at each step.

Example 1:

Input: nums = [1,2,1,0,4,2,6], k = 3

Output: [2,2,4,4,6]

Explanation:
Window position            Max
---------------           -----
[1  2  1] 0  4  2  6        2
 1 [2  1  0] 4  2  6        2
 1  2 [1  0  4] 2  6        4
 1  2  1 [0  4  2] 6        4
 1  2  1  0 [4  2  6]       6
Constraints:

1 <= nums.length <= 100,000
-10,000 <= nums[i] <= 10,000
1 <= k <= nums.length
"""


# Approach 1: Failed
class Solution:
    from collections import deque

    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        current_window = self.deque()
        result = []

        l = 0
        for r in range(len(nums)):
            current_window.append(nums[r])

            if current_window[0] < nums[r]:
                current_window.popleft()
                current_window.append(nums[r])

            if (r - l + 1) > k:
                result.append(current_window.pop())
                l += 1

        return result


if __name__ == "__main__":
    question = Solution()
    nums = [1, 2, 1, 0, 4, 2, 6]
    k = 3
    print(question.maxSlidingWindow(nums, k))
