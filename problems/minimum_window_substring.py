"""
Given two strings s and t, return the shortest substring of s such that every character in t, including duplicates, is present in the substring. If such a substring does not exist, return an empty string "".

You may assume that the correct output is always unique.

Example 1:

Input: s = "OUZODYXAZV", t = "XYZ"

Output: "YXAZ"
Explanation: "YXAZ" is the shortest substring that includes "X", "Y", and "Z" from string t.

Example 2:

Input: s = "xyz", t = "xyz"

Output: "xyz"
Example 3:

Input: s = "x", t = "xy"

Output: ""
Constraints:

1 <= s.length <= 1000
1 <= t.length <= 1000
s and t consist of uppercase and lowercase English letters.
"""

# Appraoch 1: Failed
# class Solution:
#     def minWindow(self, s: str, t: str) -> str:
#         t_char_map = {}
#         for char in t:
#             t_char_map[char] = t_char_map.get(char, 0) + 1

#         need = len(t_char_map)
#         have = 0

#         current_window_map = {}
#         minl = len(s)
#         shortest_substring = ""

#         l = r = 0
#         while r < len(s):
#             if s[r] in t_char_map and (
#                 t_char_map[s[r]] != current_window_map.get(s[r], 0)
#             ):
#                 current_window_map[s[r]] = current_window_map.get(s[r], 0) + 1
#                 have += 1

#             print(current_window_map)

#             while have == need:
#                 if (r - l + 1) < minl:
#                     minl = r - l + 1
#                     shortest_substring = s[l : r + 1]

#                 current_window_map[s[l]] -= 1
#                 if current_window_map.get(s[l], 0) < 1:
#                     current_window_map.pop(s[l])
#                 if s[l] in t_char_map and (
#                     t_char_map[s[l]] == current_window_map.get(s[l], 0)
#                 ):
#                     have -= 1
#                 l += 1
#             r += 1

#         return shortest_substring


# if __name__ == "__main__":
#     question = Solution()
#     s = "aaaaaaaaaaaabbbbbcdd"
#     t = "abcdd"

#     print(question.minWindow(s, t))


# Approach 2: using
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        countT, window = {}, {}

        if t == "":
            return ""

        for char in t:
            countT[char] = countT.get(char, 0) + 1

        have, need = 0, len(countT)

        result, min_l = [-1, -1], float("infinity")

        l = 0
        for r in range(len(s)):
            if s[r] in countT:
                window[s[r]] = window.get(s[r], 0) + 1

                if window[s[r]] == countT[s[r]]:
                    have += 1

            while have == need:
                if (r - l + 1) < min_l:
                    min_l = r - l + 1
                    result = [l, r]

                if s[l] in countT:
                    window[s[l]] -= 1

                    if window[s[l]] < countT[s[l]]:
                        have -= 1

                l += 1

        return s[result[0] : result[1] + 1] if min_l != float("infinity") else ""
