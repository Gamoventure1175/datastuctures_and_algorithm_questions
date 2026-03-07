"""
You are given a string s consisting of only uppercase english characters and an integer k. You can choose up to k characters of the string and replace them with any other uppercase English character.

After performing at most k replacements, return the length of the longest substring which contains only one distinct character.

Example 1:

Input: s = "XYYX", k = 2

Output: 4
Explanation: Either replace the 'X's with 'Y's, or replace the 'Y's with 'X's.

Example 2:

Input: s = "AAABABB", k = 1

Output: 5
Constraints:

1 <= s.length <= 1000
0 <= k <= s.length
"""


# Using sliding window plus keeping count
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        result = 0
        maxf = 0
        l = 0
        for r in range(len(s)):
            count[s[r]] = count.get(s[r], 0) + 1
            maxf = max(maxf, count[s[r]])
            while (r - l + 1) - maxf > k:
                count[s[l]] -= 1
                l += 1

            result = max(result, r - l + 1)

        return result


if __name__ == "__main__":
    question = Solution()

    s = "aaabaabb"
    k = 2

    question.characterReplacement(s, k)
