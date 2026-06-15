from typing import Any


class _Node:
    """
    A base node containing the data field and two pointers for:
    * next
    * prev
    """

    __slots__ = "_data", "_next", "_prev"

    def __init__(self, data, next=None, prev=None):
        self._data = data
        self._next = next
        self._prev = prev


class DoublyLinkedList:
    """
    Creates a doubly linked list (DLL)
    """

    def __init__(self):
        """
        Create an empty doubly linked list with default values:
        * head -> None
        * tail -> None
        * size -> 0
        """
        self._head = None
        self._tail = None
        self._size = 0

    def _is_empty(self):
        return self._size == 0

    def prepend(self, data: Any):
        """
        Add an element to start of DLL

        Args:
            data (any): data to be added
        """

        candidate = _Node(data)

        if self._is_empty():
            self._head = self._tail = candidate
        else:
            candidate._next = self._head
            candidate._next._prev = candidate
            candidate._prev = None
            self._head = candidate

        self._size += 1

    def append(self, data: Any):
        """
        Add an element to end of DLL

        Args:
            data (any): data to be added
        """

        candidate = _Node(data)

        if self._is_empty():
            self._head = self._tail = candidate
        else:
            candidate._prev = self._tail
            candidate._prev._next = candidate
            candidate._next = None
            self._tail = candidate

        self._size += 1

    def pop_head(self):
        """
        Pop an element from the start of DLL
        """
        if self._is_empty():
            raise IndexError("Cannot pop element from an empty DLL")

        if self._size == 1:
            answer = self._head._data
            self.clear()
            return answer

        answer = self._head._data
        self._head = self._head._next
        self._head._prev = None

        self._size -= 1

        return answer

    def pop_tail(self):
        """
        Pop an element from the end of the DLL
        """

        if self._is_empty():
            raise IndexError("Cannot pop element from an empty DLL")

        if self._size == 1:
            answer = self._tail._data
            self.clear()
            return answer

        answer = self._tail._data
        self._tail = self._tail._prev
        self._tail._next = None

        self._size -= 1

        return answer

    def peek_head(self):
        """
        Return the first element from the DLL
        """
        if self._is_empty():
            raise IndexError("Cannot peek from an empty DLL")

        return self._head._data

    def peek_tail(self):
        """
        Return the last element from the DLL
        """
        if self._is_empty():
            raise IndexError("Cannot peek from an empty DLL")

        return self._tail._data

    def clear(self):
        """
        Sets the DLL back to its default state:
        * _head = None
        * _tail = None
        * _size = 0
        """

        self._head = self._tail = None
        self._size = 0

    def __len__(self):
        return self._size

    def __iter__(self):
        return _DLLIterator(self._head)

    def __reversed__(self):
        return _DLLReverseIterator(self._tail)

    def __repr__(self) -> str:
        if self._is_empty():
            return "empty"

        representation = "none <=> "
        temp = self._head
        while temp:
            representation += str(temp._data) + " <=> "
            temp = temp._next
        representation += " none"

        return representation


class _DLLIterator:
    def __init__(self, node: _Node):
        self._current: _Node = node

    def __iter__(self):
        return self

    def __next__(self):
        if not self._current:
            raise StopIteration

        data = self._current._data
        self._current = self._current._next
        return data


class _DLLReverseIterator:
    def __init__(self, node: _Node):
        self._current: _Node = node

    def __iter__(self):
        return self

    def __next__(self):
        if not self._current:
            raise StopIteration

        data = self._current._data
        self._current = self._current._prev
        return data


if __name__ == "__main__":
    example = DoublyLinkedList()
    example.prepend(2)
    example.append(10)
    example.prepend(15)
    example.append(18)
    example.prepend(89)
    example.append(7)

    print(example)
    for ele in example.__iter__():
        print(ele)

    example.pop_head()
    # example.pop_tail()
    # example.pop_tail()
    # example.pop_tail()
    # example.pop_tail()
    # example.pop_tail()

    print(example)
    print(len(example))

    print("Reversing iterating the DLL")
    for ele in reversed(example):
        print(ele)
