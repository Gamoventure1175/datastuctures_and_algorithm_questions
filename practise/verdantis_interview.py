# Longest consecutive sequence


def longestConsecutive(nums: list[int]) -> int:
    unique = set(nums)
    result = 0
    for n in unique:
        if (n - 1) not in unique:
            curr = n
            longest_seq = 0
            while curr in unique:
                longest_seq += 1
                curr += 1

            result = max(result, longest_seq)

    return result


# Product of array except self


def productExceptSelf(nums: list[int]) -> list[int]:
    pre = post = 1

    result = [1] * len(nums)

    for i in range(len(nums)):
        result[i] = pre
        pre *= nums[i]

    for i in range(-1, -len(nums) - 1, -1):
        result[i] *= post
        post *= nums[i]

    return result


class Solution:
    def encode(self, strs: list[str]) -> str:
        encoded = []
        for s in strs:
            c = str(len(s)) + "#" + s
            encoded.append(c)

        return "".join(encoded)

    def decode(self, s: str) -> list[str]:
        decoded = []

        l = r = 0
        while r < len(s):
            ...


def topKFrequent(nums: list[int], k: int) -> list[int]:
    if len(nums) == 1:
        return nums

    frequency = {}

    for n in nums:
        frequency[n] = frequency.get(n, 0) + 1

    bucket = [[] for _ in range(max(frequency.values()) + 1)]

    for n, freq in frequency.items():
        bucket[freq].append(n)

    result = []
    for i in range(-1, -len(bucket) - 1, -1):
        if bucket[i]:
            for n in bucket[i]:
                result.append(n)

                if len(result) == k:
                    return result


def char_to_pattern(s: str) -> tuple:
    pattern = [0] * 26

    for char in s:
        pattern[ord(char) - ord("a")] += 1

    return tuple(pattern)


def groupAnagrams(strs: list[str]) -> list[list[str]]:
    groups: dict[tuple, list[str]] = {}

    for s in strs:
        pattern = char_to_pattern(s)

        group = groups.get(pattern, [])
        group.append(s)
        groups[pattern] = group

    return list(groups.values())


def twoSum(nums: list[int], target: int) -> list[int]:
    hasSeen = {}

    for i in range(len(nums)):
        diff = target - nums[i]

        if diff in hasSeen:
            return [hasSeen[diff], i]

        else:
            hasSeen[nums[i]] = i


def isAnagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    characters = {}

    for char in s:
        characters[char] = characters.get(char, 0) + 1

    for char in t:
        if char not in characters:
            return False

        characters[char] -= 1

    for char, freq in characters.items():
        if freq != 0:
            return False

    return True


class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean_s = []

        for char in s:
            if char.isalpha():
                clean_s.append(char.lower())

        clean_s = "".join(clean_s)

        l = 0
        r = len(clean_s) - 1

        while l <= r:
            if clean_s[l] != clean_s[r]:
                return False
            l += 1
            r -= 1

        return True


def twoSum(numbers: list[int], target: int) -> list[int]:
    l, r = 0, len(numbers) - 1

    while l < r:
        curr = numbers[l] + numbers[r]

        if curr == target:
            return [l, r]

        elif target < curr:
            r -= 1

        else:
            l += 1


def threeSum(nums: list[int]) -> list[list[int]]:
    res = []
    nums.sort()

    for i, a in enumerate(nums):
        if i > 0 and a == nums[i - 1]:
            continue

        l, r = i + 1, len(nums) - 1
        while l < r:
            sum = a + nums[l] + nums[r]

            if sum > 0:
                r -= 1
            elif sum < 0:
                l += 1
            else:
                res.append([a, nums[l], nums[r]])
                l += 1
                while nums[l] == nums[l - 1] and l < r:
                    l += 1
    return res


def maxArea(heights: list[int]) -> int:
    res = 0

    l, r = 0, len(heights) - 1
    while l < r:
        area = min(heights[l], heights[r]) * (r - l)
        res = max(res, area)

        if heights[l] < heights[r]:
            l += 1

        else:
            r -= 1

    return res


def isValid(s: str) -> bool:
    if len(s) < 2:
        return False
    closing_brackets = {"]": "[", "}": "{", ")": "("}
    opening_brackets = []

    for bracket in s:
        if bracket in "([{":
            opening_brackets.append(bracket)
        else:
            if not opening_brackets:
                return False

            if closing_brackets[bracket] != opening_brackets.pop():
                return False

    return True
