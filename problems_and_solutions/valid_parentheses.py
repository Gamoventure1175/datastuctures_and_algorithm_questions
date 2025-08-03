"""
You are given a string s consisting of the following characters: '(', ')', '{', '}', '[' and ']'.

The input string s is valid if and only if:

Every open bracket is closed by the same type of close bracket.
Open brackets are closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
Return true if s is a valid string, and false otherwise.
"""

# Approach 1: Using a stack and a dictionary for parentheses lookup

"""
The idea is simple. You setup a dictionary (a rather very small one) consisting of the following mappings:
'(' : ')'
'[' : ']'
'{' : '}'

And then you use a stack, python's list implementation works as well here, to check up the parentheses in that dictionary

So the process goes something like this: 
1. Loop through the whole string
2. if the current character is one of (, [, {, push to stack
3. if the current character is one of ), ], } :
    1. pop the stack and check if the popped item is the same as the curr character
    2. if it is not the same character, return False or else continue
4. If it is not a parentheses as all, continue
5. At the end, if the s_stack is empty (which means all the opening parenthese have their corresponding closing ones), return True
else return False

A solution of this approach is as follows:
"""

parentheses: dict[str, str] = {"(": ")", "{": "}", "[": "]"}


def isValidParentheses(s: str):
    s_stack = []
    for char in s:
        if char == "(" or char == "[" or char == "{":
            s_stack.append(char)
        elif char == ")" or char == "]" or char == "}":
            if len(s_stack) != 0 and parentheses[s_stack.pop()] == char:
                continue
            else:
                return False
        else:
            continue

    if (
        len(s_stack) == 0
    ):  # All the opening tags have their respective closing tags in the string
        return True
    return False


if __name__ == "__main__":
    s = "]"
    print(isValidParentheses(s))
