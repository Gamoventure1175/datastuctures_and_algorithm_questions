class SinglyLinkedList:
    class Node:
        def __init__(self, data: int):
            self.data = data
            self.next = None

    def __init__(self):
        self._head: SinglyLinkedList.Node | None = None
        self._tail: SinglyLinkedList.Node | None = None
        self._length: int = 0

    def _is_empty(self):
        return self._length == 0

    def peek_head(self):
        if self._is_empty():
            raise IndexError("Cannot peek from an empty linked list")
        return self._head.data

    def prepend(self, data):
        new_node = self.Node(data)
        if self._is_empty():
            self._head = new_node
            self._tail = new_node
        else:
            new_node.next = self._head
            self._head = new_node
        self._length += 1

    def append(self, data):
        new_node = self.Node(data)
        if self._is_empty():
            self._head = new_node
            self._tail = new_node
        else:
            self._tail.next = new_node
            self._tail = new_node

        self._length += 1

    def __repr__(self) -> str:
        if self._is_empty():
            return "[]"
        representation = "head => "
        temp = self._head
        while temp:
            representation += str(temp.data) + " => "
            temp = temp.next
        representation += "end"
        return representation

    def pop_head(self):
        if self._is_empty():
            raise IndexError("Cannot pop from an empty linked list")
        temp = self._head.data
        if not self._head.next:
            # Means the list has only one element before popping
            self._head = None
            self._tail = None
        else:
            self._head = self._head.next
        self._length -= 1
        return temp

    def __len__(self):
        return self._length

    def clear(self):
        self._head = None
        self._tail = None
        self._length = 0

    def __iter__(self):
        return _SLLIterator(self._head)


class _SLLIterator:
    def __init__(self, node):
        self._current = node

    def __iter__(self):
        return self

    def __next__(self):
        if self._current is None:
            raise StopIteration
        data = self._current.data
        self._current = self._current.next
        return data


class StackADT:
    def __init__(self):
        self._A = SinglyLinkedList()

    def push(self, ele):
        self._A.prepend(ele)

    def _is_empty(self):
        return len(self._A) == 0

    def pop(self):
        if self._is_empty():
            raise IndexError("Cannot pop from an empty stack")

        return self._A.pop_head()

    def peek(self):
        if self._is_empty():
            raise IndexError("Cannot peek from an empty stack")

        return self._A.peek_head()

    def __len__(self):
        return len(self._A)


if __name__ == "__main__":
    simple = SinglyLinkedList()

    simple.append(5)
    simple.prepend(3)
    simple.prepend(10)
    # print(len(simple))

    # for data in simple:
    #     print(data)

    # Testing the new stack adt using linked list

    stack = StackADT()
    stack.push(10)
    stack.push(11)
    stack.push(12)
    # stack.push(45)
    # stack.push(55)
    # print(stack.peek())
    # print(len(stack))
    stack.pop()
    stack.pop()
    stack.pop()
    print(len(stack))
    print(len(stack))
