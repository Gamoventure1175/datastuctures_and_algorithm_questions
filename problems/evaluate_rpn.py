"""
Evaluate Reverse Polish Notation
Medium
Topics
Company Tags
Hints
You are given an array of strings tokens that represents a valid arithmetic expression in Reverse Polish Notation.

Return the integer that represents the evaluation of the expression.

The operands may be integers or the results of other operations.
The operators include '+', '-', '*', and '/'.
Assume that division between integers always truncates toward zero.
Example 1:

Input: tokens = ["1","2","+","3","*","4","-"]

Output: 5

Explanation: ((1 + 2) * 3) - 4 = 5
Constraints:

1 <= tokens.length <= 1000.
tokens[i] is "+", "-", "*", or "/", or a string representing an integer in the range [-100, 100].

"""

# Approach 1: Using a stack


class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        operands = []
        for t in tokens:
            if t not in ["+", "-", "*", "/"]:
                operands.append(int(t))
            else:
                operand_1 = operands.pop()
                operand_2 = operands.pop()
                if t == "+":
                    operands.append(operand_2 + operand_1)
                elif t == "-":
                    operands.append(operand_2 - operand_1)
                elif t == "*":
                    operands.append(operand_2 * operand_1)
                else:
                    operands.append(int(operand_2 / operand_1))

        return operands.pop()
