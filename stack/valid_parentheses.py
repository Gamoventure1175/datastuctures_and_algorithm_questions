"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 

Example 1:

Input: s = "()"

Output: true

Example 2:

Input: s = "()[]{}"

Output: true

Example 3:

Input: s = "(]"

Output: false

Example 4:

Input: s = "([])"

Output: true

Example 5:

Input: s = "([)]"

Output: false

 

Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.
"""

# Attempt 1: Using a stack

class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) <= 1: return False
        valid_brackets = {"(": ")", "{": "}", "[":"]"}
        stack = []

        for c in s:
            if c in "({[":
                stack.append(valid_brackets[c])

            if c in ")}]" and not stack: return False
            
            if c in ")}]" and stack.pop() != c: return False
            
        if stack:
            return False
        
        return True

