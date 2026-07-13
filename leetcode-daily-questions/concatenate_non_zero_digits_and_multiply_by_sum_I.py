"""
You are given an integer n.

Form a new integer x by concatenating all the non-zero digits of n in their original order. If there are no non-zero digits, x = 0.

Let sum be the sum of digits in x.

Return an integer representing the value of x * sum.

 

Example 1:

Input: n = 10203004

Output: 12340

Explanation:

The non-zero digits are 1, 2, 3, and 4. Thus, x = 1234.
The sum of digits is sum = 1 + 2 + 3 + 4 = 10.
Therefore, the answer is x * sum = 1234 * 10 = 12340.
Example 2:

Input: n = 1000

Output: 1

Explanation:

The non-zero digit is 1, so x = 1 and sum = 1.
Therefore, the answer is x * sum = 1 * 1 = 1.
 

Constraints:

0 <= n <= 109
"""

# Attempt 1: Using intuition
class Solution:
    def sumAndMultiply(self, n: int) -> int:
        non_zero = []

        while n:
            last_digit = n % 10
            n //= 10

            if last_digit: non_zero.append(last_digit)

        x = sum(non_zero)
        power = len(non_zero)-1 
        new_num = 0
        while power >= 0:
            new_num = new_num + non_zero.pop() * (10 ** power)
            power -= 1

        return new_num * x
