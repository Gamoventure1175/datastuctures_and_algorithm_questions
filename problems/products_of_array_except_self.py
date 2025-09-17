"""
Products of Array Except Self
Given an integer array nums, return an array output where output[i] is
the product of all the elements of nums except nums[i].

Each product is guaranteed to fit in a 32-bit integer.

Follow-up: Could you solve it in O(n) time without using the division operation?

Example 1:

Input: nums = [1,2,4,6]

Output: [48,24,12,8]
Example 2:

Input: nums = [-1,0,1,2,3]

Output: [0,-6,0,0,0]
Constraints:

2 <= nums.length <= 1000
-20 <= nums[i] <= 20
"""


class Solution:
    """
    Encompass all the approaches to solve the products of an array except self problem.
    """

    # Approach 1: Brute Force approach
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        """
        Return product of numbers inside an array excluding the number current number itself.

        Args:
            nums (int): A list containing integer numbers

        Returns:
            list[int]: Returns a list of numbers containing products of all numbers except nums[i]


        Examples:
            >>> productExceptSelf([2, 3, 4, 5])
            [60, 40, 30, 24]
        """

        if len(nums) == 0:
            return [-1]

        result = []

        for i in range(len(nums)):
            curr_product = 1
            for j, num in enumerate(nums):

                if i == j:
                    continue
                curr_product *= num

            result.append(curr_product)

        return result

    # Approach 2: Using Prefix and Suffix approach
    def product_except_self_prefix_suffix(self, nums: list[int]) -> list[int]:
        """
        Return product of numbers inside an array excluding the  number nums[i] itself.

        This function takes a list of numbers and using an optimized approach that utilizes
        prefix and suffix patterns, returns a list of all products excluding number[i].

        Args:
            nums (int): A list containing integer numbers

        Returns:
            list[int]: Returns a list of numbers containing products of all numbers except nums[i].
            Returns [-1] if the list of numbers is empty


        Examples:
            >>> productExceptSelf([2, 3, 4, 5])
            [60, 40, 30, 24]
        """

        # Edge case: If the nums list is empty
        if len(nums) == 0:
            return [-1]

        # Creating prefix products array
        prefix = [1]
        product = 1
        for i in range(len(nums)):
            if i == 0:
                continue
            product = product * nums[i - 1]
            prefix.append(product)

        # Creating suffix products array
        suffix = [1]
        product = 1
        for i in range(-1, -(len(nums)) - 1, -1):
            if i == -1:
                continue
            product = product * nums[i + 1]
            suffix.append(product)

        # The idea is as follows:
        # [prefix] -> product of numbers from left to right except nums[i]
        # [suffix] -> product of all numbers from right to left before i excluding nums[i]

        # So, since when we want product of numbers except the current one (i), we are
        # simply looking at product of all numbers to the left of i and to the right of i
        # and not include i.

        # So when we do prefix * suffix for that particular i, we are essentially doing
        # the same as above.

        # Finally returning the result of the product of the prefix and the suffix
        result = []
        for i in range(len(nums)):
            result.append(prefix[i] * suffix[-(i + 1)])

        return result


if __name__ == "__main__":
    solution = Solution()
    test = [2, 3, 4, 5]
    print(solution.product_except_self_prefix_suffix(test))
