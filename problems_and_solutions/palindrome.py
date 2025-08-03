"""
Given a string s, return true if it is a palindrome, otherwise return false.

A palindrome is a string that reads the same forward and backward. It is also case-insensitive and ignores all non-alphanumeric characters.

Note: Alphanumeric characters consist of letters (A-Z, a-z) and numbers (0-9).

Example 1:

Input: s = "Was it a car or a cat I saw?"

Output: true
Explanation: After considering only alphanumerical characters we have "wasitacaroracatisaw", which is a palindrome.
"""

# This question in essence is pretty straightforward
# You just have to think clearly how you identify a palindrom string

# Since a palindrome a basically a symmetric string over the middle character/characters, I can think of the following solution:


# Approach 1: Two pointers (✅ - is O(n) in nature.)
"""
We have to consider alphanumeric strings for this problem. So, if we get any string for this problem, we will have to get rid of spaces,
special characters and other things and only consider the alpha numeric characters.

There are exceptions that need to be addressed before the solution:
    1. String is empty -> ''
    2. String has single character -> " ", "a", "_"
In such scenarios, we simply return True

For a palindromic string like 'aabaa', assume a s_p and e_p pointers at the start and end of the string respectively.

Both pointers are expected to go in the following direction when the loop is moving:

s_p ->                 <- e_p
      a   a   b   a   a
      
For every position of the two pointers in the string, you check the following everytime:

string[s_p] == string[e_p]

If the above condition is satisfied, you keep continue to change the position of the pointers and if not,
you simply return False

Also, you continue to change the pointers position until you reach the following condition:

s_p >= e_p

The following is the execution of this approach
"""


def isPalindrome(s: str):
    alphabetical_s = "".join(char for char in s if char.isalnum()).lower()

    if len(alphabetical_s) == 0 or len(alphabetical_s) == 1:
        return True

    s_p = 0
    e_p = len(alphabetical_s) - 1

    for _ in alphabetical_s:
        if s_p >= e_p:
            return True
        else:
            if alphabetical_s[s_p] == alphabetical_s[e_p]:
                s_p += 1
                e_p -= 1
                continue
            else:
                return False


if __name__ == "__main__":
    s = "0p"
    print(isPalindrome(s))
