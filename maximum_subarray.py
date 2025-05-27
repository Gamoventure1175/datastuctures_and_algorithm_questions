# Given an array arr[], the task is to find the subarray that has the maximum sum and return its sum.
# Example:

# Input: arr[] = {2, 3, -8, 7, -1, 2, 3}
# Output: 11
# Explanation: The subarray {7, -1, 2, 3} has the largest sum 11.

# I am trying the brute force method first where I use 2 for loops to check for all the possible subarrays


# THE BELOW APPROACH IS INCORRECT ❌
# def max_sub_array(a: list) -> int:
#     '''A function that takes an array (python list) and finds
#     the subarray that has the maximum sum and returns its sum'''

#     max_sum = 0
#     sub_array = []

#     for i in range(len(a)):
#         for j in range(len(a)):
#             if sum(sub_array) + a[j] >= max_sum:
#                 sub_array.append(a[j])
#                 max_sum = sum(sub_array)
#             elif sum(sub_array) + a[j] < max_sum:
#                 break
#         sub_array = []

#     return max_sum



# I have kind of cheated for the solution below. I read it from geeks for geeks
# It uses the 2 loops but it is much clearer in logic and 

def max_sub_array(arr: list):
    '''A function that takes an array (python list) and finds
    the subarray that has the maximum sum and returns its sum'''
    
    res = arr[0]
    
    for i in range(len(arr)):
        currSum = 0
        
        for j in range(i, len(arr)):
            currSum += arr[j]
            res = max(res, currSum)
            # print(f'From the number {arr[i]}: {currSum}')     #Just for testing purposes

    return res


# This next approach uses Kadane's algorithm I learnt from geeksforgeeks
def max_sub_array_kadanes(arr: list):
    """A function that takes an array (python list) and finds
    the subarray that has the maximum sum and returns its sum
    using Kadane's algorithm"""
    curr_sum = max_sum = arr[0]
    
    for i in range(1, len(arr)):
        curr_sum = max(arr[i], curr_sum + arr[i])
        max_sum = max(max_sum, curr_sum)
    
    return max_sum

if __name__ == "__main__":
    example = [2, 3, -8, 7, -1, 2, 3, -10, 8, 8, 9, 10]
    print("Using the brute force approach: ", max_sub_array(example))
    print("Using the kadane's algorithm approach: ", max_sub_array_kadanes(example))
    