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


# Approach 1: Python's list based stack
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


# Approach 2: 

if __name__ == "__main__":
    # test = MinStack()
    # # Trying to do operations on an empty stack
    # # test.pop()
    # # test.getMin()
    # # test.top()

    # for i in range(1, 6):
    #     test.push(i)

    # print(f"Stack: \n {test}")
    # print(f"Length of the stack: {len(test)}")
    # print(f"Top element of the stack: {test.top()}")

    # # Popping elements from the stack
    # popped = test.pop()
    # print(f"Popped element: {popped}")
    # print(f"Stack after pop: \n {test}")

    # some_other = MinStack()
    # some_other.push(1)
    # some_other.push(2)
    # some_other.push(10)
    # some_other.push(5)
    # # Minimum element from the stack
    # print(f"Minimum element from the stack: {test.getMin()}")

    # some_test = MinStack()
    # some_test.push(0)
    # some_test.push(1)
    # some_test.push(0)
    # print(some_test.getMin())
    # some_test.pop()
    # print(some_test._Min)
