"""
Given two strings s and t, return true if the two strings are anagrams of each other, otherwise return false.

An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

Example 1:

Input: s = "racecar", t = "carrace"

Output: true
Example 2:

Input: s = "jar", t = "jam"

Output: false
Constraints:

s and t consist of lowercase English letters.

"""

# Approach 1: Using sets and subtraction
# def isAnagram(s, t):
#     s_set = set(s)
#     t_set = set(t)

#     return True if len(s_set) == len(t_set) else False

# Approach 2: Using Counter from collections

# def count_dict_creator(string):
#     string_dict = {}
#     for char in string:
#         if char in string_dict:
#             string_dict[char] += 1
#             continue
#         string_dict[char] = 1
#     return string_dict


def isAnagram(s, t):
    if len(s) != len(t):
        return False

    def counter(string):
        string_dict = {}
        for char in string:
            string_dict[char] = string_dict.get(char, 0) + 1
        return string_dict

    s_char_count = counter(s)

    for char in t:
        if s_char_count.get(char, 0) > 0:
            s_char_count[char] -= 1
            continue
        return False

    for char in s_char_count:
        if s_char_count.get(char) != 0:
            return False

    return True


# Approach 2: Using array as count bucket
class Solution:
    # def isAnagram(self, s: str, t: str) -> bool:
    #     if len(s) != len(t):
    #         return False

    #     charCount = [0] * 26

    #     for i in range(len(s)):
    #         charCount[ord(s[i]) - ord("a")] += 1
    #         charCount[ord(t[i]) - ord("a")] -= 1

    #     for count in charCount:
    #         if count != 0:
    #             return False

    #     return True

    # Approach 3: Using hasmap for unicode characters
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        charCount = {}

        for char in s:
            charCount[char] = charCount.get(char, 0) + 1

        for char in t:
            if char not in charCount:
                return False

            charCount[char] -= 1

            if charCount[char] < 0:
                return False

        return True


if __name__ == "__main__":
    # result = isAnagram("gaurav", "auravg")
    # print(result)

    question = Solution()
    s = "gaurav#"
    t = "auragv#"
    print(question.isAnagram(s, t))
