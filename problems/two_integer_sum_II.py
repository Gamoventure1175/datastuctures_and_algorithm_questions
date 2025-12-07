"""
Given an array of integers numbers that is sorted in non-decreasing order.

Return the indices (1-indexed) of two numbers, [index1, index2], such that they add up to a given target number target and index1 < index2. Note that index1 and index2 cannot be equal, therefore you may not use the same element twice.

There will always be exactly one valid solution.

Your solution must use O(1) additional space.

Example 1:

Input: numbers = [1,2,3,4], target = 3

Output: [1,2]
Explanation:
The sum of 1 and 2 is 3. Since we are assuming a 1-indexed array, index1 = 1, index2 = 2. We return [1, 2].
"""

# Noted: I have used hints for this problem as I couldn't come with my own solution right away

# Approach 1: Using two pointers (I have used hints)

"""
This approach is based on the following two ideas:
    1. If smallest + largest > target, largest cannot be considered in any pair 
    2. If smallest + largest < target, smallest cannot be considered in any pair
Resons: 
    1. If adding the largest number amounts for a value greater than target, this
    largest number should not be considered into any further pairs
    2. Vice versa

So, we will use two pointers to denote the smallest (starting from the left) and the largest
(starting from the right) and based on the above conditions, keep moving the pointers

The following is the code implementation of the above
"""


def twoSum(numbers: list[int], target: int):
    first_pointer = 0
    second_pointer = len(numbers) - 1
    while first_pointer < second_pointer:
        if numbers[first_pointer] + numbers[second_pointer] == target:
            return [first_pointer + 1, second_pointer + 1]
        elif numbers[first_pointer] + numbers[second_pointer] > target:
            second_pointer -= 1
        else:
            first_pointer += 1
    return False


if __name__ == "__main__":
    numbers = [2, 7, 11, 15]
    target = 9

    print(twoSum(numbers, target))
