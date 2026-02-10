"""
Best Time to Buy and Sell Stock
Easy
Topics
Company Tags
Hints
You are given an integer array prices where prices[i] is the price of NeetCoin on the ith day.

You may choose a single day to buy one NeetCoin and choose a different day in the future to sell it.

Return the maximum profit you can achieve. You may choose to not make any transactions, in which case the profit would be 0.

Example 1:

Input: prices = [10,1,5,6,7,1]

Output: 6
Explanation: Buy prices[1] and sell prices[4], profit = 7 - 1 = 6.

Example 2:

Input: prices = [10,8,7,5,2]

Output: 0
Explanation: No profitable transactions can be made, thus the max profit is 0.

Constraints:

1 <= prices.length <= 100
0 <= prices[i] <= 100

"""


# Approach 1: Using dynamic sliding window
class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        left = 0
        profit = max(0, (prices[left + 1] - prices[left]))

        for right in range(left + 2, len(prices)):
            while prices[left] >= min(prices[left], prices[right]):
                left += 1
            profit = max(0, (prices[right] - prices[left]))

        return profit


if __name__ == "__main__":
    prices = [5, 1, 5, 6, 7, 1]

    solve = Solution()
    print(solve.maxProfit(prices))
