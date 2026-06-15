# Creating a simple array based stack

# Methods in stack:
# 	push
# 	pop
# 	top
# 	is_empty
# 	len


class Empty(Exception):
    """Error attempting to access an element from an empty container"""

    pass


class ArrayStack:
    def __init__(self):
        """Initializing a underlying dynamic array"""
        self._stack = list()

    def push(self, value):
        """Push an element into the stack"""
        self._stack.append(value)

    def pop(self):
        """Pop an element from the stack"""
        if len(self._stack) == 0:
            raise Empty("Stack is empty")
        return self._stack.pop()

    def top(self):
        """Return an instance of the element at the top"""
        if self.is_empty():
            raise Empty("Stack is empty")
        return self._stack[-1]

    def is_empty(self):
        """Return true if the stack is empty"""
        if not len(self._stack):
            return True
        return False

    def __len__(self):
        """Return the length of the stack"""
        return len(self._stack)

    def __repr__(self):
        """A better representation of the stack"""
        format = "[" + "\n"
        for j in range(len(self._stack) - 1, -1, -1):
            format += str(self._stack[j]) + "\n"
        format += "]"
        return format


if __name__ == "__main__":
    example_stack = ArrayStack()
    print("Is stack empty: ", example_stack.is_empty())

    for i in range(1, 17):
        example_stack.push(i)
        print("Element at the top: ", example_stack.top())

    print("Is stack empty: ", example_stack.is_empty())
