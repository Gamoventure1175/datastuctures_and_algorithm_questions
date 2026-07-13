"""
An integer has sequential digits if and only if each digit in the number is one more than the previous digit.

Return a sorted list of all the integers in the range [low, high] inclusive that have sequential digits.

 

Example 1:

Input: low = 100, high = 300
Output: [123,234]
Example 2:

Input: low = 1000, high = 13000
Output: [1234,2345,3456,4567,5678,6789,12345]
 

Constraints:

10 <= low <= high <= 10^9
"""
# Attempt 1: Using intuition

# class Solution:
#     def isSequential(self, n: int) -> bool:
#         last_digit = n % 10
#         n //= 10
#         while n:
#             curr = n % 10
#             n //= 10

#             if last_digit != (curr + 1):
#                 return False
            
#             last_digit = curr

#         return True

#     def sequentialDigits(self, low: int, high: int) -> List[int]:
#         result = []

#         for i in range(low, high+1):
#             if self.isSequential(i):
#                 result.append(i)
        
#         return result

# Attempt 2: Trying to find a better approach
class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        sample = "123456789"
        result = []

        min_length = len(str(low))
        max_length = len(str(high))
 
        for length in range(min_length, max_length+1):
            for i in range(10-length):
                test = int(sample[i: i+length])

                if low <= test <= high:
                    result.append(test)

        return result


if __name__ == "__main__":
    sol = Solution()
