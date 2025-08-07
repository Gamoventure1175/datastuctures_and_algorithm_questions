'''
Given an array of integers nums and an integer target, return the indices i and j such that nums[i] + nums[j] == target and i != j.

You may assume that every input has exactly one pair of indices i and j that satisfy the condition.

Return the answer with the smaller index first.

Example 1:

Input: 
nums = [3,4,5,6], target = 7

Output: [0,1]
Explanation: nums[0] + nums[1] == 7, so we return [0, 1].

Example 2:

Input: nums = [4,5,6], target = 10

Output: [0,2]
Example 3:

Input: nums = [5,5], target = 10

Output: [0,1]
Constraints:

2 <= nums.length <= 1000
-10,000,000 <= nums[i] <= 10,000,000
-10,000,000 <= target <= 10,000,000
'''

# I have already solved this problem using brute force method. However, it was o(n**2).

# Approach 2: Using dictionary to keep track of all the elements in the given array

def twoSum(nums: list[int], target: int):
    nums_dict: dict[int, int] = {}
    
    for i in range(len(nums)):
        nums_dict[nums[i]] = i
    
    for i in range(len(nums)):
        diff = target - nums[i]
        
        if nums_dict.get(diff):
            found = nums_dict[diff]
            
            if found == i:
                continue
            
            return [i, found] if i < found else [found, i]

    return False

if __name__ == "__main__":
    
    nums = [1,3,4,2,]
    target = 6
    
    print(twoSum(nums, target))