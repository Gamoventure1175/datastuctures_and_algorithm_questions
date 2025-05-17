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

#The above approach is not exactly a sliding window approach because it recreates a window everytime with the following commands:
#unique_set.clear()
#unique_set.update(sample[l:r+1])

# print(longest_substring_sliding_window('abcdefacbcbbbzywmijlgetuvqqabcdefghijklmnoprstuv'))



#Sliding window approach
def sliding_window_longest_string(sample: str) -> int:
    k = 1
    max_sub = 0
    l = 0
    r = 0
    
    unique_set = set()
    
    while r <= len(sample)-1:
        if sample[r] not in unique_set:
            if k > max_sub: 
                max_sub = k
            unique_set.add(sample[r])
            r+=1
            k+=1
        else:
            while sample[r] in unique_set:
                unique_set.remove(sample[l])
                l+=1
            unique_set.add(sample[r])
            r+=1
            k=2
            
    return max_sub

print(sliding_window_longest_string('abcdefacbcbbbzywmijlgetuvqqabcdefghijklmnoprstuv'))