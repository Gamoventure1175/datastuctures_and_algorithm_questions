"""
3280. Convert Date to Binary
Solved
Easy
Topics
premium lock icon
Companies
You are given a string date representing a Gregorian calendar date in the yyyy-mm-dd format.

date can be written in its binary representation obtained by converting year, month, and day to their binary representations without any leading zeroes and writing them down in year-month-day format.

Return the binary representation of date.



Example 1:

Input: date = "2080-02-29"

Output: "100000100000-10-11101"

Explanation:

100000100000, 10, and 11101 are the binary representations of 2080, 02, and 29 respectively.

Example 2:

Input: date = "1900-01-01"

Output: "11101101100-1-1"

Explanation:

11101101100, 1, and 1 are the binary representations of 1900, 1, and 1 respectively.



Constraints:

date.length == 10
date[4] == date[7] == '-', and all other date[i]'s are digits.
The input is generated such that date represents a valid Gregorian calendar date between Jan 1st, 1900 and Dec 31st, 2100 (both inclusive).
"""


# Approach 1:
class Solution:
    def numToBinary(self, n: int) -> str:
        if n == 0:
            return "0"

        stack = []

        while n:
            stack.append(str(n % 2))
            n //= 2

        binary = []
        while stack:
            binary.append(stack.pop())

        return "".join(binary)

    def convertDateToBinary(self, date: str) -> str:
        year = int(date[0:4])
        month = int(date[5:7])
        day = int(date[8:10])

        year_binary = self.numToBinary(year)
        month_binary = self.numToBinary(month)
        day_binary = self.numToBinary(day)

        return year_binary + "-" + month_binary + "-" + day_binary


# Approach 2: Pythonic way
class Solution2:
    def convertDateToBinary(self, date: str) -> str:
        year, month, day = map(int, date.split("-"))

        return f"{bin(year)[2:]}-{bin(month)[2:]}-{bin(day)[2:]}"
