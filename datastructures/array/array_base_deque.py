"""
Implementation of a double ended queue (deque / deck) using python list as
the internal data structure and circular indexing buffer for keeping track
of front and back of the deque

Operations of a deque ADT:
    1. add_first()
    2. add_last()
    3. delete_first()
    4. delete_last()
    5. __len__(deque)
    6. first()
    7. last()
    8. is_empty()
"""


class EmptyDequeError(Exception):
    "Raises an exception when an operation is performed on an empty deque"

    def __init__(self, operation: str):
        super().__init__(f"Deque is empty. Cannot perform '{operation}'.")
        self.operation = operation


class Deque:
    """
    Double ended queue implementation using python list as the internal storage

    Note:
        Default capacity of the deque is 10.
        Operations at the end  or start of the array are amortized O(1).
        Operations in the middle of the array are O(n).
    """

    DEFAULT_CAPACITY = 10

    def __init__(self):
        self._data = [None] * Deque.DEFAULT_CAPACITY
        self._front = 0
        self._size = 0

        # back -> Calculated during runtime using _front, _size and capacity of _data

    def _resize(self, c):
        """
        Resizes the internal _data list by 'length of _data * c'
        """

        old = self._data
        self._data = [None] * c
        walk = self._front
        for i in range(self._size):
            self._data[i] = old[walk]
            walk = (walk + 1) % len(old)
        self._front = 0

    def _back(self):
        return (self._front + self._size - 1) % len(self._data)

    def __len__(self):
        """Return the actual number of elements in the deque"""
        return self._size

    def is_empty(self):
        """Return a boolean balue based on the emptiness of the deque"""
        return self._size == 0

    def add_first(self, e):
        """Adds an element to the start of the deque"""
        if self._size == len(self._data):
            self._resize(2 * len(self._data))

        self._front = (self._front - 1) % len(self._data)
        self._data[self._front] = e
        self._size += 1

    def add_last(self, e):
        """Adds and element to the end of the deque"""
        if self._size == len(self._data):
            self._resize(2 * len(self._data))

        avail = (self._front + self._size) % len(self._data)
        self._data[avail] = e
        self._size += 1

    def delete_first(self):
        """Removes an element from the start of the deque"""
        if self.is_empty():
            raise EmptyDequeError("delete_first")
        self._data[self._front] = None
        self._front = (self._front + 1) % len(self._data)
        self._size -= 1

        if (
            0 < self._size < len(self._data) // 4
            and len(self._data) > Deque.DEFAULT_CAPACITY
        ):
            self._resize(len(self._data) // 2)

    def delete_last(self):
        """Removes an element from the end of the deque"""
        if self.is_empty():
            raise EmptyDequeError("delete_last")

        last_index = self._back()
        self._data[last_index] = None
        self._size -= 1

        if (
            0 < self._size < len(self._data) // 4
            and len(self._data) > Deque.DEFAULT_CAPACITY
        ):
            self._resize(len(self._data) // 2)

    def first(self):
        """Returns the first element in the deque"""
        if self.is_empty():
            raise EmptyDequeError("first")
        return self._data[self._front]

    def last(self):
        """Returns the last element in the deque"""
        if self.is_empty():
            raise EmptyDequeError("last")
        return self._data[self._back()]

    def __repr__(self):
        """A better representation of the deque"""
        format = "in/out <-> [ "
        for j in range(len(self._data)):
            format += str(self._data[j]) + ", "
        format += "] <-> in/out"
        return format


if __name__ == "__main__":
    example = Deque()

    example.add_first(10)
    example.add_first(11)
    example.add_last(343)
    example.add_last(33)
    example.add_first(3)
    example.delete_first()
    print(example)
    print(example.first())
    print(example.last())
