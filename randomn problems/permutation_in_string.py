"""
Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

In other words, return true if one of s1's permutations is the substring of s2.



Example 1:

Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").
Example 2:

Input: s1 = "ab", s2 = "eidboaoo"
Output: false


Constraints:

1 <= s1.length, s2.length <= 104
s1 and s2 consist of lowercase English letters.
"""


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        char_freq = {}
        for chr in s1:
            char_freq[chr] = char_freq.get(chr, 0) + 1

        l = r = 0
        curr_window = {}

        while r < len(s2):
            while (r - l + 1) > len(s1):
                if s2[l] in char_freq:
                    curr_window[s2[l]] -= 1
                l += 1

            if s2[r] in char_freq:
                curr_window[s2[r]] = curr_window.get(s2[r], 0) + 1

            if curr_window == char_freq:
                return True

            r += 1

        return False


if __name__ == "__main__":
    question = Solution()
    s1 = "ab"
    s2 = "eidbaoo"
    print(question.checkInclusion(s1, s2))
