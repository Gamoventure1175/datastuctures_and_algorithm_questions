"""
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] where nums[i] + nums[j] + nums[k] == 0, and the indices i, j and k are all distinct.

The output should not contain any duplicate triplets. You may return the output and the triplets in any order.

Example 1:

Input: nums = [-1,0,1,2,-1,-4]

Output: [[-1,-1,2],[-1,0,1]]
Explanation:
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].

Example 2:

Input: nums = [0,1,1]

Output: []
Explanation: The only possible triplet does not sum up to 0.

Example 3:

Input: nums = [0,0,0]

Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.

Constraints:

3 <= nums.length <= 1000
-10^5 <= nums[i] <= 10^5
"""

# Approach 1: Using loops and a dictionary


# def threeSum(nums):
#     present_nums = {nums[i]: i for i in range(len(nums))}

#     triplets = []

#     for i in range(len(nums) - 1):
#         for j in range(i + 1, len(nums)):
#             missing_piece = -(nums[i] + nums[j])

#             missing_piece_index = present_nums.get(missing_piece, None)

#             if missing_piece_index != None:
#                 if missing_piece_index not in [i, j]:
#                     triplets.append([i, j, missing_piece_index])

#     return triplets


# if __name__ == "__main__":
#     nums = [-1, 0, 1, 2, -1, -4]
#     print(threeSum(nums=nums))

# Approach 2: Using two pointers approach


def merge(L, R):
    result = []
    i = 0
    j = 0

    n1 = len(L)
    n2 = len(R)

    while i < n1 and j < n2:
        if L[i] <= R[j]:
            result.append(L[i])
            i += 1
        else:
            result.append(R[j])
            j += 1

    while i < n1:
        result.append(L[i])
        i += 1

    while j < n2:
        result.append(R[j])
        j += 1

    return result


def merge_sort(nums: list[int]) -> list[int]:
    if len(nums) <= 1:
        return nums

    mid = len(nums) // 2
    left = nums[:mid]
    right = nums[mid : len(nums)]

    sorted_left = merge_sort(left)
    sorted_right = merge_sort(right)

    return merge(sorted_left, sorted_right)


def threeSum(nums):
    sorted_nums = merge_sort(nums)

    triplets = []

    for num in sorted_nums:
        target = -num

        first_pointer = 0
        second_pointer = len(nums) - 1

        for i in range(len(sorted_nums)):
            if sorted_nums[first_pointer] == num or sorted_nums[second_pointer] == num:
                continue

            pointer_sums = sorted_nums[first_pointer] + sorted_nums[second_pointer]

            if pointer_sums == target:
                triplets.append(
                    [num, sorted_nums[first_pointer], sorted_nums[second_pointer]]
                )

            elif pointer_sums > target:
                second_pointer -= 1
            else:
                first_pointer += 1

    return triplets


if __name__ == "__main__":
    print(threeSum([-1, 0, 1, 2, -1, -4]))
