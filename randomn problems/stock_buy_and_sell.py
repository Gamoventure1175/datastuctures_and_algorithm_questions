# Maximum one transaction allowed

# Given an array prices[] of length N, representing the prices of the stocks on different days,
# the task is to find the maximum profit possible by buying and selling the stocks on different days
# when at most one transaction is allowed. Here one transaction means 1 buy + 1 Sell.

# Note: Stock must be bought before being sold.

# Examples:
# Input: prices[] = {7, 10, 1, 3, 6, 9, 2}
# Output: 8
# Explanation: Buy for price 1 and sell for price 9.

# Input: prices[] = {7, 6, 4, 3, 1}
# Output: 0
# Explanation: Since the array is sorted in decreasing order, 0 profit can be made without making any transaction.

# Input: prices[] = {1, 3, 6, 9, 11}
# Output: 10
# Explanation: Since the array is sorted in increasing order, we can make maximum profit by buying at price[0] and
# selling at price[n-1]


# So the concept is simple enough I guess
# You buy the stock when the stock price is the lowest -> find the lowest in the array of prices
# You sell the stock when the stock price is the next highest -> find the highest price in [lowest.......end]

# So I first use a two separate loop solution


def stock_buy_sell(prices: list[int]):
    """A function that takes in stock prices and returns the maximum profit
    that can be made from it by buying and selling stocks maximum one time
    (Max one transaction is allowed)"""

    # This overall works in O(n) time

    lowest_price = prices[0]

    for price in prices[1 : len(prices)]:  # o(n)
        if price < lowest_price:
            lowest_price = price

    index_lowest_price = prices.index(lowest_price)  # o(n)

    highest_price = 0

    for i in range(index_lowest_price, len(prices)):  # o(n-index_lowest_price+1)
        if prices[i] > highest_price:
            highest_price = prices[i]

    if highest_price < lowest_price:
        return 0

    profit = highest_price - lowest_price

    return profit


# The following solution is a much cleaner solution that I understood from chatgpt
# It removes redundant 2 loops for calculating the highest and lowest prices
# which can be done in the same loop
# Also, it removes the unnecessary O(n) index lookup
def stock_buy_sell_cleaner(prices: list[int]):
    """A function that takes in stock prices and returns the maximum profit
    that can be made from it by buying and selling stocks maximum one time
    (Max one transaction is allowed)"""

    if not prices:
        return 0

    lowest_price = prices[0]
    max_profit = 0

    for price in prices[1:]:
        profit = price - lowest_price
        max_profit = max(max_profit, profit)
        lowest_price = max(lowest_price, price)

    return max_profit


if __name__ == "__main__":
    price_array = [1, 3, 6, 9, 11]
    print(stock_buy_sell(price_array))
