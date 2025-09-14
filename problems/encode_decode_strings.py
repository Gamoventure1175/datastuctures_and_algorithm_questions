"""
Encode and Decode Strings
Design an algorithm to encode a list of strings to a single string. The encoded string is then decoded back to the original list of strings.

Please implement encode and decode

Example 1:

Input: ["neet","code","love","you"]
Output:["neet","code","love","you"]

Example 2:

Input: ["we","say",":","yes"]
Output: ["we","say",":","yes"]

Constraints:

0 <= strs.length < 100
0 <= strs[i].length < 200
strs[i] contains only UTF-8 characters.
"""


# Approach 1: By storing lengths of the strings given.
class Solution:
    def __init__(self):
        """
        ### Iinitializes the class with two variables:
            1. self._encoded -> Used to keep track of the encoded string
            2. self._string_lengths -> An array of string lengths.
        """
        self._encoded: str = ""
        self._decoded: list[str] = []
        self._string_lengths: list[str | int] = []
        self._number_of_strings_to_decode: int = 0

    def encode(self, strs: list[str]) -> str:
        """
        ### Combines the strings given in the aray into a single string
        #### Arguments accepted:
            1. strs -> A list of strings

        If any of the elements inside the array is not a string, an exception will be raised
        """
        if len(strs) == 0:
            return "-1"
        self._number_of_strings_to_decode = len(strs)

        for string in strs:
            if type(string) != type(""):
                raise Exception("Every element of the list must be a string")
            if len(string) == 0:
                self._string_lengths.append("*")
            else:
                self._string_lengths.append(len(string))
                self._encoded += string

        return self._encoded

    def decode(self, s: str) -> list[str]:

        if s == "-1":
            return []

        if len(s) == 0:
            return [""]

        curr_len_index = 0
        prev_string_end = 0

        for i in range(0, len(s)):
            print(
                f"Current i: {i}, Current index for lengths: {curr_len_index}, Current length to decode: {self._string_lengths[curr_len_index]}"
            )
            if self._string_lengths[curr_len_index] == "*":
                self._decoded.append("")
                if self._number_of_strings_to_decode != 0:
                    curr_len_index += 1
                    self._number_of_strings_to_decode -= 1
            elif (i + 1) - prev_string_end == self._string_lengths[curr_len_index]:
                self._decoded.append(s[(i + 1) - self._string_lengths[curr_len_index] : (i + 1)])  # type: ignore because when the current length
                # is '*', it is already accounted for in the previous loop

                if self._number_of_strings_to_decode != 0:
                    curr_len_index += 1
                    self._number_of_strings_to_decode -= 1
                    prev_string_end = i + 1

        return self._decoded


if __name__ == "__main__":
    test = ["", "a", "", "bb", "", "ccc", ""]

    print(f"Input: {test}")

    solution = Solution()
    encoded = solution.encode(test)

    print("Result for encoding: ", encoded)

    decoded = solution.decode(encoded)

    print("Result for decoding: ", decoded)

    # print(solution._number_of_strings_to_decode, solution._string_lengths)
