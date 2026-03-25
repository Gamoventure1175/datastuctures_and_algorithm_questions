"""
Given an array of strings words and an integer k, return the k most frequent strings.

Return the answer sorted by the frequency from highest to lowest. Sort the words with the same frequency by their lexicographical order.



Example 1:

Input: words = ["i","love","leetcode","i","love","coding"], k = 2
Output: ["i","love"]
Explanation: "i" and "love" are the two most frequent words.
Note that "i" comes before "love" due to a lower alphabetical order.
Example 2:

Input: words = ["the","day","is","sunny","the","the","the","sunny","is","is"], k = 4
Output: ["the","is","sunny","day"]
Explanation: "the", "is", "sunny" and "day" are the four most frequent words, with the number of occurrence being 4, 3, 2 and 1 respectively.


Constraints:

1 <= words.length <= 500
1 <= words[i].length <= 10
words[i] consists of lowercase English letters.
k is in the range [1, The number of unique words[i]]


Follow-up: Could you solve it in O(n log(k)) time and O(n) extra space?
"""

# Approach 1: Hashmaps with array buckets


class Solution:

    def word_to_pattern(self, word: str) -> tuple:
        bucket = [0] * 26

        for char in word:
            bucket[ord(char) - ord("a")] += 1

        return tuple(bucket)

    def pattern_to_word(self, pattern: tuple) -> str:
        word = ""
        for i in range(len(pattern)):
            if pattern[i]:
                for _ in range(pattern[i]):
                    char = chr(ord("a") + i)
                    word += char
        return word

    def topKFrequent(self, words: list[str], k: int) -> list[str]:
        word_freq = {}

        for word in words:
            word_freq[word] = word_freq.get(word, 0) + 1

        bucket = [[] for _ in range(max(word_freq.values()) + 1)]  # Assuming this O(n)

        for word, freq in word_freq.items():
            bucket[freq].append(word)

        for word_bucket in bucket:
            if word_bucket:
                word_bucket.sort()

        result = []
        for i in range(-1, -len(bucket) - 1, -1):
            if bucket[i]:
                for word in bucket[i]:
                    result.append(word)

                    if len(result) == k:
                        return result

        return []


if __name__ == "__main__":
    question = Solution()
    words = ["i", "love", "leetcode", "i", "love", "coding"]
    k = 1
    # sample = tuple(
    #     (0, 0, 1, 1, 3, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0)
    # )
    # print(question.pattern_to_word(sample))
    print(question.topKFrequent(words, k))
