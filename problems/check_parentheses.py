# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.

from datastructures.array_based_stack import ArrayStack


# I read about this approach in the DSA book I am reading
# It uses a stack data structure to simplify the process of checking
# for the brackets
def isValidBracket(s: str) -> bool:
    """Takes a string containing sequence of brackets or
    expressions with brackets and determines if they are in the right order"""
    lefty = "({["
    righty = ")}]"

    brackets = ArrayStack()

    for exp in s:
        if exp in lefty:
            brackets.push(exp)
        elif exp in righty:
            if brackets.is_empty():
                return False
            if righty.index(exp) != lefty.index(brackets.pop()):
                return False

    return brackets.is_empty()


if __name__ == "__main__":
    example = "[][][][][][][][][][[][][][][][]][][]()()()()()()()()(()()()()(()()()()()()()()()(())((((()()())(())(()()(()()(()(()((()((())(())))))))))))))"
    print(isValidBracket(example))
