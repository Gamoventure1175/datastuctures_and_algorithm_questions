# A question that converts a given decimal number (number > 0) to binary

# I use a stack for this approach
# The idea is that when we keep dividing the number by 2, we get:
#   1. quotient
#   2. remainder
# The idea is that we keep dividing by 2 until the remainder becomes 1 and quotient is greater than 0

from datastructures.array_based_stack import ArrayStack


def dec_to_bin(num: int):
    """A function that takes any decimal number > 0 and converts it to binary"""
    stack = ArrayStack()
    binary = ""

    while num > 0:
        rem = num % 2
        stack.push(rem)
        num = num // 2

    while stack:
        binary += str(stack.pop())

    return binary


if __name__ == "__main__":
    print(dec_to_bin(56))
