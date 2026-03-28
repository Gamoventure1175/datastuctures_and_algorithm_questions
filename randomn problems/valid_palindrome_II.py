"""
Given a string s, return true if the s can be palindrome after deleting at most one character from it.



Example 1:

Input: s = "aba"
Output: true
Example 2:

Input: s = "abca"
Output: true
Explanation: You could delete the character 'c'.
Example 3:

Input: s = "abc"
Output: false


Constraints:

1 <= s.length <= 105
s consists of lowercase English letters.
"""

# Approach 1: Thinking based on the frequency
# class Solution:
#     def validPalindrome(self, s: str) -> bool:
#         bucket = [0] * 26

#         for c in s:
#             bucket[ord(c) - ord("a")] += 1

#         k = 0

#         for freq in bucket:
#             if freq:
#                 if freq % 2 == 1:
#                     k += 1

#         if k - 1 > 1:
#             return False

#         return True


# Approach 2: two pointer with one violation allowed or two pointer + greedy
class Solution:
    def isPalindrome(self, s: str, l: int, r: int) -> bool:
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True

    def validPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        while l < r:
            if s[l] != s[r]:
                return self.isPalindrome(s, l + 1, r) or self.isPalindrome(s, l, r - 1)

            l += 1
            r -= 1
        return True


if __name__ == "__main__":
    question = Solution()
    s = "aguokepatgbnvfqmgmlcupuufxoohdfpgjdmysgvhmvffcnqxjjxqncffvmhvgsymdjgpfdhooxfuupuculmgmqfvnbgtapekouga"
    print(question.validPalindrome(s))
