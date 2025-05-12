#Given a string s having lowercase characters, find the length of the longest substring without repeating characters.

#Brute force approach (Linear Approach)
# def longest_substring(sample: str) -> int:
#     b = []
#     count = 0

#     for i in range(0, len(sample)): 
#         if sample[i] not in b:
#             b.append(sample[i])
#         else:
#             if len(b) > count: 
#                 count = len(b)
#             b = []
#             b.append(sample[i])
#     if len(b) > count:
#         count = len(b)
            
#     return count



# print(longest_substring('abcdefacbcbbbzywmijlgetuvqqabcdefghijklmnoprstuv'))

#Trying a sliding window approach
def longest_substring_sliding_window(sample: str) -> int:
    k = 1
    max_sub_str = 0
    l = 0
    r = 0
    
    unique_set = set(sample[l:r+1])
    
    while r <= len(sample)-1:
        if len(unique_set) == k:
            max_sub_str = k
            k += 1
            r += 1
            unique_set.clear()
            unique_set.update(sample[l:r+1])
        else:
            k = max_sub_str
            l = r
            r += k
            unique_set.clear()
            unique_set.update(sample[l:r+1])
            k+=1
            
    return max_sub_str

print(longest_substring_sliding_window('abcdefacbcbbbzywmijlgetuvqqabcdefghijklmnoprstuv'))