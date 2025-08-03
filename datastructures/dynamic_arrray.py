import sys
import ctypes
from typing import Any


class DynamicArray:
    """A dynamic array class akin to simplified Python list"""

    def __init__(self) -> None:
        """Create an empty array"""
        self._n = 0  # Count the actual number of elements in the array
        self._capacity = 1  # The actual size of the array
        self._A = self._make_array(self._capacity)

    def __len__(self):
        """Return number of elements stored in the array"""
        return self._n

    def __getitem__(self, k):
        """Return element at index k"""
        if not 0 <= k < self._n:
            raise IndexError("Invalid index")
        return self._A[k]

    def append(self, obj: object):
        """Add object to the end of the array"""
        if self._n == self._capacity:
            self._resize(2 * self._capacity)
        self._A[self._n] = obj
        self._n += 1

    def _resize(self, c):
        """Resize internal array to capacity c"""
        B = self._make_array(c)
        for k in range(0, self._n):
            B[k] = self._A[k]
        self._A = B
        self._capacity = c

    def _make_array(self, c: int):
        """Return a new array with capacity c."""
        return (c * ctypes.py_object)()

    def insert(self, k, value):
        """Insert an element at a given index"""
        # assume that 0<=k<n
        if self._n == self._capacity:
            self._resize(2 * self._capacity)

        for j in range(self._n, k, -1):
            self._A[j] = self._A[j - 1]
        self._A[k] = value
        self._n += 1

    def remove(self, value):
        """Remove a value from the array"""
        for k in range(0, self._n):
            if self._A[k] == value:
                deleted = self._A[k]
                for j in range(k + 1, self._n):
                    self._A[j - 1] = self._A[j]
                self._n -= 1
                if self._n > 0 and self._n == self._capacity // 4:
                    self._resize(self._capacity // 2)
                return deleted
        raise ValueError("Value not found")

    def pop(self):
        """Remove the last element from the array"""
        deleted = self.remove(self._A[self._n - 1])
        if self._n == (self._capacity / 4):
            self._resize(self._capacity // 2)
        return deleted

    def __repr__(self):
        """Represent the array in a better format"""
        format = "["
        for j in range(0, self._n):
            format += str(self._A[j]) + ", "
        format += "]"
        return format


if __name__ == "__main__":
    someArray = DynamicArray()
    for i in range(1, 17):
        someArray.append(i)
        print(f"Elements: {someArray._n}      |     Capacity: {someArray._capacity}")

    print()
    print(someArray)

    for i in range(1, 17):
        someArray.pop()
        print(f"Elements: {someArray._n+1}      |     Capacity: {someArray._capacity}")
