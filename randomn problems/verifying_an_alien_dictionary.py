"""
In an alien language, surprisingly, they also use English lowercase letters, but possibly in a different order. The order of the alphabet is some permutation of lowercase letters.

Given a sequence of words written in the alien language, and the order of the alphabet, return true if and only if the given words are sorted lexicographically in this alien language.



Example 1:

Input: words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"
Output: true
Explanation: As 'h' comes before 'l' in this language, then the sequence is sorted.
Example 2:

Input: words = ["word","world","row"], order = "worldabcefghijkmnpqstuvxyz"
Output: false
Explanation: As 'd' comes after 'l' in this language, then words[0] > words[1], hence the sequence is unsorted.
Example 3:

Input: words = ["apple","app"], order = "abcdefghijklmnopqrstuvwxyz"
Output: false
Explanation: The first three characters "app" match, and the second string is shorter (in size.) According to lexicographical rules "apple" > "app", because 'l' > '∅', where '∅' is defined as the blank character which is less than any other character (More info).


Constraints:

1 <= words.length <= 100
1 <= words[i].length <= 20
order.length == 26
All characters in words[i] and order are English lowercase letters.
"""

# # Understanding lexicograhical comparison only or lowercase letters

# words = ["i", "something", "love", "coding", "coder"]
# # tell if the words are sorted lexicographically


# # Manually
# def compare_strings(a: str, b: str) -> int:
#     """
#     returns:
#         -1 if a < b
#         0 if a == b
#         1 if a > b
#     """

#     i = 0

#     while i < len(a) and i < len(b):
#         if a[i] < b[i]:
#             return -1
#         elif a[i] > b[i]:
#             return 1

#         i += 1

#     if len(a) < len(b):
#         return -1
#     elif len(a) > len(b):
#         return 1

#     return 0


# def lexicographical_order_check(words: list[str]) -> bool:
#     for i in range(len(words) - 1):
#         for j in range(1, len(words)):
#             if compare_strings(words[i], words[j]) == 1:
#                 print(words[i], words[j])
#                 return False
#     return True


# print(lexicographical_order_check(words))


# Approach 1: Whatever I understood
class Solution:
    # def isAlienSorted(self, words: list[str], order: str) -> bool:
    #     ltr_order = {}

    #     for position, letter in enumerate(order):
    #         ltr_order[letter] = position

    #     for i in range(len(words) - 1):
    #         curr = words[i]
    #         next = words[i + 1]

    #         # first letter check
    #         if curr[0] != next[0]:
    #             if ltr_order[curr[0]] > ltr_order[next[0]]:
    #                 return False
    #             else:
    #                 continue

    #         # subsequent letters check
    #         j = 1
    #         while j < len(curr) and j < len(next):
    #             if ltr_order[curr[j]] > ltr_order[next[j]]:
    #                 return False
    #             else:
    #                 j += 1
    #                 continue

    #         # if all letters were same till now
    #         if curr[j - 1] == next[j - 1]:
    #             if len(curr) > len(next):
    #                 return False
    #             else:
    #                 continue

    #     return True

    # Approach 2: Making it simpler
    def isAlienSorted(self, words: list[str], order: str) -> bool:
        orderMap = {}

        for position, letter in enumerate(order):
            orderMap[letter] = position

        for i in range(len(words) - 1):
            curr = words[i]
            nxt = words[i + 1]

            j = 0
            while j < len(curr):
                if j >= len(nxt):
                    return False

                if curr[j] != nxt[j]:
                    if orderMap[curr[j]] > orderMap[nxt[j]]:
                        return False
                    else:
                        break

                j += 1

        return True


if __name__ == "__main__":
    words = ["hello", "leetcode", "leetcod"]
    order = "hlabcdefgijkmnopqrstuvwxyz"
    question = Solution()
    print(question.isAlienSorted(words, order))
