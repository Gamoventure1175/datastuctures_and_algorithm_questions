"""
Given an integer array nums and an integer k, return the k most frequent elements within the array.

The test cases are generated such that the answer is always unique.

You may return the output in any order.

Example 1:

Input: nums = [1,2,2,3,3,3], k = 2

Output: [2,3]
Example 2:

Input: nums = [7,7], k = 1

Output: [7]
Constraints:

1 <= nums.length <= 10^4.
-1000 <= nums[i] <= 1000
1 <= k <= number of distinct elements in nums.
"""

# Approach 1: Using a Counter dictionary to get count of the numbers and return output based on that ❌
# def topKFrequent(input, k):
#     if len(input) == 0:
#         return [-1]

#     from collections import Counter
#     freqCount = Counter(input)
#     freqCountItems = list(freqCount.items()) # Used later on for appending these keys to output
#     print(f'Dictionary: {freqCount}')
#     print(f'Keys: {freqCountItems}')
#     output = []
#     freqSet = set()
#     for value in freqCount.values():
#         freqSet.add(value)

#     if len(freqSet) != len(freqCount):
#         return [-1]
#     else:
#         for i in range(k):
#             output.append(freqCountItems[i][0])
#     return output

# if __name__ == '__main__':
#     nums = [1,1,1,2,2,3]
#     k = 2


#     print(topKFrequent(nums, k))


# Approach 2: Using a custom sorting algorithm for sorting ❌
# def topKFrequent(nums, k):
#     if len(nums) == 0:
#         return [-1]

#     freq = {}
#     for ele in nums:
#         if freq.get(ele):
#             freq[ele] += 1
#         else:
#             freq[ele] = 1

#     freq_keys = list(freq.keys())
#     freq_values = list(freq.values())
#     freq_count_set = set(freq_values)

#     print("Before: ", freq_keys, freq_values, freq_count_set)

#     if len(freq_count_set) == 1:
#         result = []
#         for i in range(-1, -k-1, -1):
#             result.append(freq_keys[i])
#         return result
#     elif len(freq_values) > len(freq_count_set):
#         return [-1]
#     else:
#         for i in range(1, len(freq_keys)):
#             prev, curr = i-1, i

#             while prev >= 0:
#                 if freq_values[prev] > freq_values[curr]:
#                     freq_values[prev], freq_values[curr] = freq_values[curr], freq_values[prev]
#                     freq_keys[prev], freq_keys[curr] = freq_keys[curr], freq_keys[prev]
#                     prev -= 1

#                     curr -= 1
#                 else:
#                     prev -= 1
#                     curr -= 1
#                     continue

#     print("After: ", freq_keys, freq_values, freq_count_set)
#     result = []

#     for i in range(-1, -k-1, -1):
#         result.append(freq_keys[i])

#     return result

# if __name__ == "__main__":
#     nums=[3,0,1,0]
#     k=1
#     print(topKFrequent(nums, k))


# Approach 3: Checking for uniqueness of answer right before returning the answer ❌
# def topKFrequent(nums, k):
#     if len(nums) == 0:
#         return [-1]

#     freq = {}

#     for ele in nums:
#         if freq.get(ele):
#             freq[ele] += 1
#         else:
#             freq[ele] = 1

#     freq_values = list(freq.values())
#     freq_keys = list(freq.keys())

#     for i in range(1, len(freq_values)):
#         prev, curr = i-1, i

#         while prev >= 0:
#             if freq_values[prev] > freq_values[curr]:
#                 freq_values[prev], freq_values[curr] = freq_values[curr], freq_values[prev]
#                 freq_keys[prev], freq_keys[curr] = freq_keys[curr], freq_keys[prev]
#                 prev -= 1

#                 curr -= 1
#             else:
#                 prev -= 1
#                 curr -= 1
#                 continue

#     result_values = []
#     result_keys = []

#     for i in range(-1, -k-1, -1):
#         result_values.append(freq_values[i])
#         result_keys.append(freq_keys[i])

#     result_values_set = set(result_values)

#     if len(result_values_set) != 1 and len(result_values_set) < k:
#         return [-1]
#     else:
#         return result_keys


# # Approach 4: Skipping mannual uniqueness check completely ✅
# def topKFrequent(nums, k):
#     if len(nums) == 0:
#         return [-1]

#     freq = {}

#     for ele in nums:
#         if freq.get(ele):
#             freq[ele] += 1
#         else:
#             freq[ele] = 1

#     freq_values = list(freq.values())
#     freq_keys = list(freq.keys())

#     for i in range(1, len(freq_values)):
#         prev, curr = i-1, i

#         while prev >= 0:
#             if freq_values[prev] > freq_values[curr]:
#                 freq_values[prev], freq_values[curr] = freq_values[curr], freq_values[prev]
#                 freq_keys[prev], freq_keys[curr] = freq_keys[curr], freq_keys[prev]
#                 prev -= 1

#                 curr -= 1
#             else:
#                 prev -= 1
#                 curr -= 1
#                 continue

#     result_values = []
#     result_keys = []

#     for i in range(-1, -k-1, -1):
#         result_values.append(freq_values[i])
#         result_keys.append(freq_keys[i])

#     return result_keys

# if __name__ == "__main__":
#     nums = [1,1,2,2]
#     k = 2

#     print(topKFrequent(nums, k))


# Approach 5: Using a dictionary


def topKFrequent(nums: list[int], k: int) -> list[int]:
    frequencies = {}
    for num in nums:
        frequencies[num] = frequencies.get(num, 0) + 1

    frequency_number = {}
    for num, freq in frequencies.items():
        group = frequency_number.get(freq, [])
        group.append(num)
        frequency_number[freq] = group

    top_frequency_elements = []
    for i in range(len(nums), 0, -1):
        if frequency_number.get(i):
            top_frequency_elements.extend(frequency_number[i])

    return top_frequency_elements[0:k]


if __name__ == "__main__":
    result = topKFrequent([1, 2], k=3)

    print(result)
