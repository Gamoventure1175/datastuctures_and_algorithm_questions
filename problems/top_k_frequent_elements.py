'''
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
'''

# Approach 1: Using a Counter dictionary to get count of the numbers and return output based on that
def topKFrequent(input, k):
    if len(input) == 0:
        return [-1]
        
    from collections import Counter
    freqCount = Counter(input)
    freqCountItems = list(freqCount.items()) # Used later on for appending these keys to output
    print(f'Dictionary: {freqCount}')
    print(f'Keys: {freqCountItems}')
    output = []
    freqSet = set()    
    for value in freqCount.values():
        freqSet.add(value)
    
    if len(freqSet) != len(freqCount):
        return [-1]
    else:
        for i in range(k):
            output.append(freqCountItems[i][0])
    return output

if __name__ == '__main__':
    nums = [1,1,1,2,2,3]
    k = 2

    
    print(topKFrequent(nums, k))
