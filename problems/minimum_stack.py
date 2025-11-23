"""
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Implement the MinStack class:

MinStack() initializes the stack object.
void push(int val) pushes the element val onto the stack.
void pop() removes the element on the top of the stack.
int top() gets the top element of the stack.
int getMin() retrieves the minimum element in the stack.
You must implement a solution with O(1) time complexity for each function.
"""

# Approach 1: Python's list based stack ❌ (Time complexity is not O(n))
# class MinStack:
#     def __init__(self):
#         self._n = 0
#         self._stack = []
#         self._Min: int | None = None

#     def push(self, val: int):
#         self._Min = min(self._Min, val) if self._Min else val

#         self._stack.append(val)
#         self._n += 1

#     def __len__(self):
#         return self._n

#     def __repr__(self):
#         sample = ""
#         for i in range(self._n - 1, -1, -1):
#             sample += "| " + str(self._stack[i]) + " |" + "\n"
#         return sample

#     def pop(self):
#         if self._n == 0:
#             raise Exception("Cannot pop from an empty stack")
#         self._n -= 1
#         self._Min = None
#         popped_obj = self._stack.pop()
#         for val in self._stack:
#             self._Min = min(self._Min, val) if self._Min is not None else val
#         return popped_obj

#     def top(self):
#         if self._n == 0:
#             raise Exception("Cannot peek from an empty stack")
#         return self._stack[self._n - 1]

#     def getMin(self):
#         if self._n == 0:
#             raise Exception("Cannot get minimum element from an empty stack")
#         return self._Min


# Approach 2: Using 2 stacks ✅
# class MinStack:
#     def __init__(self):
#         self._minStack = []
#         self._stack = []
#         self._n = 0
#         self._min = None

#     def __len__(self):
#         return self._n

#     def __repr__(self):
#         sample = ""
#         for i in range(self._n - 1, -1, -1):
#             sample += "| " + str(self._stack[i]) + " |" + "\n"
#         return sample

#     def push(self, val):
#         if self._min == None:
#             self._min = val
#         else:
#             self._min = min(self._min, val)

#         self._n += 1
#         self._minStack.append(self._min)
#         self._stack.append(val)

#     def top(self):
#         if self._n == 0:
#             raise Exception("Cannot view top element of an empty stack")
#         top_element = self._stack[-1]
#         return top_element

#     def pop(self):
#         if self._n == 0:
#             raise Exception("Cannot pop elements from an empty stack")
#         self._n -= 1
#         self._minStack.pop()
#         if len(self._minStack) != 0:
#             self._min = self._minStack[-1]
#         else:
#             self._min = None
#         return self._stack.pop()

#     def getMin(self):
#         if self._n == 0:
#             raise Exception("Cannot return a minimum element from an empty stack")
#         return self._minStack[-1]


# if __name__ == "__main__":
#     test = MinStack()
#     # Trying to do operations on an empty stack
#     # test.pop()
#     # test.getMin()
#     # test.top()

#     test.push(-1)
#     test.push(4)
#     test.push(-2)
#     test.push(10)
#     test.push(2)

#     print(f"Stack: \n {test}")
#     print(f"Length of the stack: {len(test)}")
#     print(f"Top element of the stack: {test.top()}")
#     print(f"Minimum element from the stack: {test.getMin()}")

#     # Popping elements from the stack
#     for i in range(len(test)):
#         test.pop()
#         if len(test) == 0:
#             break
#         print("State of the stack after just popping an element")
#         print(f"Stack: \n {test}")
#         print(f"Length of the stack: {len(test)}")
#         print(f"Top element of the stack: {test.top()}")
#         print(f"Minimum element from the stack: {test.getMin()}")


# Approach 3 : Using python's list object


class MinStack:
    def __init__(self):
        self._stack = []

    def push(self, num):
        if not self._stack:
            self._stack.append((num, num))
        else:
            min_so_far = min(self._stack[-1][-1], num)
            self._stack.append((num, min_so_far))

    def pop(self):
        return self._stack.pop()[0]

    def top(self):
        return self._stack[-1][0]

    def getMin(self):
        return self._stack[-1][-1]


if __name__ == "__main__":
    stack = MinStack()
    stack.push(5)
    stack.push(0)
    stack.push(2)
    stack.push(4)

    stack.getMin()
    stack.pop()
    stack.getMin()
    stack.pop()
    print(stack.getMin())
