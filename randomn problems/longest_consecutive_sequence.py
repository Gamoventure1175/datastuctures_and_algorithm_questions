# Given an unsorted array of integers nums, return the length of 
# the longest consecutive elements sequence.

# You must write an algorithm that runs in O(n) time.

# Example 1:
'''
Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
'''


# Approach 1 - Brute force approach (❌ doesn't work)

# Using python's list and two nested loops
'''
What is consequtive? 1, 2, 3, 4, 5, ......
Basically, a list of numbers where for a number 'i', the next number will be 'i+1'


So, the following is the thought process of designing the solution:

For a given unsorted list of number, e.g. [100, 4, 200, 1, 3, 2], check for each number. 
Maintain a 'final' empty list outside the loop structure
So, first loop will check for each number maintain a local list in it's body.
The inner loop will look for the next consequtive numbers in the loop.
note: Skip the number when it comes across itself.

If the length of the local list (containing consequtive numbers for the current number)
is bigger than the final list, assigned the local list to the final list and return it's length 
after every number's consequitve iterations have been checked.

Code is as follows: 
'''     
# def brute_force_longest_consequtive_list(num_list: list[int]):
#     final: list[int] = []

#     for i in range(len(num_list)):
#         local:list[int] = []
#         local.append(num_list[i])
#         current_number = num_list[i]
        
#         for j in range(len(num_list)):
#             if i == j:
#                 continue
            
#             if current_number + 1 == num_list[j]:
#                 local.append(num_list[j])
#                 current_number = num_list[j]
#             else:
#                 continue
        
#         if len(local) > len(final):
#             final = local
    
#     if len(final) == 0:
#         return -1
#     else: 
#         return final
    
                
                
# Approach 2 - Sort and do the rest (❌ - Highly inefficient)

'''
This follows the same idea from the previous approach just, before doing the previous approach, you sort the array and then work on it
'''

def sort_brute_force_longest_consequtive_list(num_list: list[int]):
    seq = sorted(num_list)
    final: list[int] = []

    for i in range(len(seq)):
        local:list[int] = []
        local.append(seq[i])
        current_number = seq[i]
        
        for j in range(len(seq)):
            if i == j:
                continue
            
            if current_number + 1 == seq[j]:
                local.append(seq[j])
                current_number = seq[j]
            else:
                continue
        
        if len(local) > len(final):
            final = local
    
    if len(final) == 0:
        return -1
    else: 
        return final
    
if __name__ == "__main__":
    example = [100,4,200,1,3,2]
    print(sort_brute_force_longest_consequtive_list(example))
    
    example2 = [0,3,7,2,5,8,4,6,0,1, 1]
    print(sort_brute_force_longest_consequtive_list(example2))
    
    example3 = [10, 5, 12, 6, 8, 7, 11]
    print(sort_brute_force_longest_consequtive_list(example3))
