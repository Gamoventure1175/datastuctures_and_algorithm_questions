"""
You are given two strings s1 and s2.

Return true if s2 contains a permutation of s1, or false otherwise. That means if a permutation of s1 exists as a substring of s2, then return true.

Both strings only contain lowercase letters.

Example 1:

Input: s1 = "abc", s2 = "lecabee"

Output: true
Explanation: The substring "cab" is a permutation of "abc" and is present in "lecabee".

Example 2:

Input: s1 = "abc", s2 = "lecaabee"

Output: false
Constraints:

1 <= s1.length, s2.length <= 1000
"""


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        k = len(s1)
        s1_freq_map = {}
        for char in s1:
            s1_freq_map[char] = s1_freq_map.get(char, 0) + 1
        # print("S1 map: ", s1_freq_map)
        l = 0
        current_map = {}
        for r in range(len(s2)):
            current_map[s2[r]] = current_map.get(s2[r], 0) + 1

            if (r - l + 1) > k:
                current_map[s2[l]] = current_map[s2[l]] - 1
                if current_map[s2[l]] < 1:
                    current_map.pop(s2[l])
                l += 1
            # print("Current map: ", current_map, "S1 map: ", s1_freq_map)

            if current_map == s1_freq_map:
                return True

        return False


if __name__ == "__main__":
    question = Solution()
    s1 = "abc"
    s2 = "lecaabee"
    print(question.checkInclusion(s1, s2))
