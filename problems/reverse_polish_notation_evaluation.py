"""
Evaluate Reverse Polish Notation
You are given an array of strings tokens that represents a valid arithmetic expression in Reverse Polish Notation.

Return the integer that represents the evaluation of the expression.

The _operands may be integers or the results of other operations.
The _operators include '+', '-', '*', and '/'.
Assume that division between integers always truncates toward zero.
Example 1:

Input: tokens = ["1","2","+","3","*","4","-"]

Output: 5

Explanation: ((1 + 2) * 3) - 4 = 5

Constraints:

1 <= tokens.length <= 1000.
tokens[i] is "+", "-", "*", or "/", or a string representing an integer in the range [-100, 100].
"""

# Approach 1: Using a stack for _operands and a dictionary for _operators? ❌
# (Wrong understanding of the RPN concept and hence the wrong solution)


class Solution:
    def __init__(self):
        self._operators = {
            "+": (lambda x, y: x + y),
            "-": (lambda x, y: x - y),
            "*": (lambda x, y: x * y),
            "/": (lambda x, y: x / y),
        }

        self._operands = []

    def evalRPN(self, tokens):
        if len(tokens) < 3:
            print(
                "Tokens list must have atleast 3 characters for RPN evaluation to work"
            )
            return None

        for ele in tokens:
            if str(ele).isalpha():
                print(
                    "The token list should only consist of numerical _operands and the arithmetic _operators"
                )
                return None

            if self._operators.get(ele):
                evaluation = self._operands.pop()
                while len(self._operands) != 0:
                    # This sequence matters as it evaluates from left operand
                    # to right operand respective to the tokens list
                    evaluation = self._operators.get(ele)(
                        self._operands.pop(), evaluation  # type: ignore
                    )
                self._operands.append(evaluation)
            else:
                self._operands.append(int(ele))

        if len(self._operands) > 1:
            return None

        return self._operands.pop()


if __name__ == "__main__":
    tokens = ["4", "13", "5", "/", "+"]
    test = Solution()
    print(test.evalRPN(tokens))
