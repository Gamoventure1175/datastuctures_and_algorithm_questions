"""
Given a string s, find the length of the longest substring without duplicate characters.



Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3. Note that "bca" and "cab" are also correct answers.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.


Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.
"""

from typing import List

# Attempt 1: Using sliding window


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = j = 0
        maxL = 0

        curr_window = set()

        while j < len(s):
            if s[j] in curr_window:
                while s[j] in curr_window:
                    curr_window.remove(s[i])
                    i += 1

            curr_window.add(s[j])
            maxL = max(maxL, len(curr_window))
            j += 1

        return maxL
