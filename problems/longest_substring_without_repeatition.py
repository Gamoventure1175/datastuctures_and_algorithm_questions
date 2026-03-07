"""
Given a string s, find the length of the longest substring without duplicate characters.

A substring is a contiguous sequence of characters within a string.

Example 1:

Input: s = "zxyzxyz"

Output: 3
Explanation: The string "xyz" is the longest without duplicate characters.

Example 2:

Input: s = "xxxx"

Output: 1
Constraints:

0 <= s.length <= 1000
s may consist of printable ASCII characters.
"""

# Approach 1: Dynamic sliding window


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not len(s):
            return 0

        l, r = 0, 1
        possibleSubstring = set()
        possibleSubstring.add(s[l])

        maxLength = len(possibleSubstring)

        while r < len(s):
            while s[r] in possibleSubstring:
                possibleSubstring.discard(s[l])
                l += 1

            possibleSubstring.add(s[r])
            r += 1

            maxLength = max(maxLength, len(possibleSubstring))

        return maxLength


if __name__ == "__main__":
    question = Solution()
    s = "pwwkew"
    print(question.lengthOfLongestSubstring(s))
