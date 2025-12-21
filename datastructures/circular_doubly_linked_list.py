class _Node:
    __slots__ = "_element", "_next", "_prev"

    def __init__(self, element, next=None, prev=None):
        self._element = element
        self._next = next
        self._prev = prev


class CircularDoublyLinkedList:
    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    def __len__(self):
        return self._size

    def _is_empty(self):
        return self._size == 0

    def _clear(self):
        self._head = self._tail = None
        self._size = 0

    def append(self, element):
        new_node = _Node(element)
        if self._is_empty():
            self._head = self._tail = new_node
            self._head._next = self._head
            self._head._prev = self._head
        else:
            new_node._prev = self._tail
            new_node._next = self._head
            self._tail._next = new_node
            self._head._prev = new_node
            self._tail = new_node

        self._size += 1

    def prepend(self, element):
        new_node = _Node(element)
        if self._is_empty():
            self._head = self._tail = new_node
            self._tail._next = self._tail
            self._tail._prev = self._tail
        else:
            new_node._next = self._head
            new_node._prev = self._tail
            self._head._prev = new_node
            self._tail._next = new_node
            self._head = new_node

        self._size += 1

    def peek_head(self):
        if self._is_empty():
            raise IndexError("Cannot peek from an empty CDLL")
        return self._head._element

    def peek_tail(self):
        if self._is_empty():
            raise IndexError("Cannot peek from an empty CDLL")
        return self._tail._element

    def pop_head(self):
        if self._is_empty():
            raise IndexError("Cannot pop from an empty CDLL")

        if self._size == 1:
            result = self._head._element
            self._clear()
            return result

        else:
            result = self._head._element
            self._head._next._prev = self._tail
            self._tail._next = self._head._next

            self._head = self._head._next

            self._size -= 1
            return result

    def pop_tail(self):
        if self._is_empty():
            raise IndexError("Cannot pop from an empty CDLL")

        if self._size == 1:
            result = self._tail._element
            self._clear()
            return result

        else:
            result = self._tail._element
            self._tail._prev._next = self._head
            self._head._prev = self._tail._prev

            self._tail = self._tail._prev

            self._size -= 1
            return result

    def __repr__(self):
        if self._is_empty():
            return "CircularDoublyLinkedList()"
        elements = []
        current = self._head
        while True:
            elements.append(repr(current._element))
            current = current._next
            if current == self._head:
                break
        return "CircularDoublyLinkedList(" + ", ".join(elements) + ")"

    def __iter__(self):
        return _CDLLIterator(self._head, self._size)

    def __reversed__(self):
        return _CDLLReverseIterator(self._tail, self._size)


class _CDLLIterator:
    def __init__(self, node: _Node, size):
        self._current: _Node = node
        self._size = size

    def __iter__(self):
        return self

    def __next__(self):
        if self._size == 0:
            raise StopIteration

        current = self._current._element
        self._current = self._current._next
        self._size -= 1
        return current


class _CDLLReverseIterator:
    def __init__(self, node: _Node, size):
        self._current: _Node = node
        self._size = size

    def __iter__(self):
        return self

    def __next__(self):
        if self._size == 0:
            raise StopIteration

        current = self._current._element
        self._current = self._current._prev
        self._size -= 1
        return current


if __name__ == "__main__":
    cdll = CircularDoublyLinkedList()
    cdll.append(10)
    cdll.append(20)
    cdll.append(30)
    print(cdll)

    print("Forward iterator: ")
    for element in cdll:
        print(element)

    print("Reverse iterator: ")
    for element in reversed(cdll):
        print(element)
