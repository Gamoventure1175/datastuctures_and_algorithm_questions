'''
Given an array of strings strs, group all anagrams together into sublists. You may return the output in any order.

An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

Example 1:

Input: strs = ["act","pots","tops","cat","stop","hat"]

Output: [["hat"],["act", "cat"],["stop", "pots", "tops"]]
Example 2:

Input: strs = ["x"]

Output: [["x"]]
Example 3:

Input: strs = [""]

Output: [[""]]
Constraints:

1 <= strs.length <= 1000.
0 <= strs[i].length <= 100
strs[i] is made up of lowercase English letters.
'''

# Approach 1 : Brute Force

'''
With this approach, I divide the problem into 2 main parts, namely:
    1. Selection of strings for checking if they are anagrams
    2. Implementing a anagram algorithm that checks the given two strings for anagram (Already implemented before, has a O(n) running time)

So, this solution will be O(n^3) because the selection involves a time complexity of O(n^2) and the anagram checking algorithm will run in a time complexity of O(n)

The idea is that: 
    first iteration will go over the whole array (i to n-1) -> second iteration will go from (i+1) to n-1 -> each series of iteration would group the 
    anagrams (if found any) and also group the non - anagramic strings individually -> return a new version of the original array with the grouping
    
The following is the code implementation of this approach:
'''

def isValidAnagram(str1: str, str2: str):
    if len(str1) != len(str2):
        return False
    
    char_counts = {}

    for char in str1:
        if char_counts.get(char) == None:
            char_counts[char] = 1
        else: 
            char_counts[char] += 1
            
    for char in str2:
        if char_counts.get(char) == None:
            return False
        else: 
            char_counts[char] -= 1
    
    for key in char_counts:
        if char_counts[key] != 0:
            return False
    
    return True

def groupAnagrams(strs: list[str]):
    is_it_checked: dict[str, bool] = {}

    groups = []
    
    for i in range(len(strs)):
        if is_it_checked.get(strs[i]):
            continue
        
        group = [strs[i]]

        for j in range(1, len(strs)):
            if isValidAnagram(strs[i], strs[j]):
                group.append(strs[j])
                is_it_checked[strs[i]], is_it_checked[strs[j]] = True, True
            else:
                is_it_checked[strs[i]] = True
    
        groups.append(group)

    return groups

if __name__ == "__main__":
    strs = ["act","pots","tops","cat","stop","hat"]

    print(groupAnagrams(strs))