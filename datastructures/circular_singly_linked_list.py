from typing import Any


class Node:
    """
    # Definition of a base node used by the circular singly linked list

    ## Arguments include:
    - data = the data that the node carries
    - next = pointer to the next node in the linked list
    """

    def __init__(self, data: Any | None = None):
        self.data: Any | None = data
        self.next: Node | None = None


class CircularSinglyLinkedList:
    def __init__(self):
        """
        Initialize the following for every new instance of the clas:
        * head
        * tail
        * length (the length of the circular linked list)
        """
        self.head = None
        self.tail = None
        self.length = 0

    def _insert_empty(self, data: Any):
        """
        #### Inserts an element to a circular linked list when the list is empty

        *Noted: Use this function only when the circular list is completely (self.head is None)*
        """
        if self.head is not None:
            raise Exception(
                "The list must be completely empty for this operation to occur"
            )

        new_node = Node(data=data)

        self.head = new_node
        new_node.next = new_node
        self.tail = new_node
        self.length += 1

        self._check_invariants()

    def insert_beginning(self, data: Any) -> None:
        """
        #### A function that inserts a node at the beginning of the circular singly linked list

        ##### Arguments:
        - data = *int* value
        """

        if self.head is None:  # check for if the linked list is empty
            self._insert_empty(data=data)

        else:
            if self.tail is None:
                raise Exception("Tail cannot be None if the head is not None")
            else:
                new_node = Node(data=data)
                new_node.next = self.head
                self.tail.next = new_node
                self.head = new_node
                self.length += 1

        self._check_invariants()

    def insert_end(self, data: Any) -> None:
        """
        #### A function that inserts a node at the ending of the circular singly linked list

        ##### Arguments:
        - data = *int* value
        """

        if self.head is None:
            self._insert_empty(data=data)
        else:
            if self.tail is None:
                raise Exception(
                    "Tail must be assigned to something if the head is not None"
                )
            else:
                new_node = Node(data=data)
                self.tail.next = new_node
                new_node.next = self.head
                self.tail = new_node
                self.length += 1

        self._check_invariants()

    def insert_at_any_position(self, position_index: int, data: Any) -> None:
        """
        *Note: position, index -> starts with 0*
        """
        if self.is_valid_insert_index(position_index):
            if self.head is None:
                self._insert_empty(data=data)
                return
            elif position_index == 0:
                self.insert_beginning(data)
                return
            elif position_index == self.length:
                self.insert_end(data)
                return
            else:
                new_node = Node(data)
                insert_after = self.head
                for i in range(1, position_index):
                    insert_after = insert_after.next  # type:ignore
                insert_before = insert_after.next  # type:ignore
                insert_after.next = new_node  # type: ignore
                new_node.next = insert_before
                self.length += 1

                self._check_invariants()

                return
        else:
            raise IndexError("Incorrect index provided")

    def is_valid_insert_index(self, index: int):
        """
        A checking function that returns a boolean value
        based on if the index is within the range of [0, self.length]

        ***'[' -> included***
        """
        return index in range(0, self.length + 1)

    def _check_invariants(self):
        """
        #### This function checks for the following
        conditions and asserts that they are true:
        * If *head* is **None** then *tail* has to be **None**
        * If *head* is **not None** then *tail* **cannot** be **None**
        * If *head* is **not None** then *tail.next* has to be **head**
        * If *head* is **not None** then *length* cannot be **0**
        """
        if self.head is None:
            assert self.tail is None, "Tail should be None when head is None"
        else:
            assert self.tail is not None, "Tail cannot be None if head is not None"
            assert (
                self.tail.next == self.head
            ), "Tail's next should always be head in a circular linked list"
            assert self.length > 0, "Length should not be 0 if head is not None"

    def __repr__(self) -> str:
        """
        #### A function to represent the circular singly linked list
        Outputs the list in the following format:

        > (head) n1 -> n2 -> n3 -> n4 -> n1 (back to head)
        """

        if self.head is None:
            return "List is empty."

        linked_list_repr = "(head) "
        current = self.head

        while True:
            linked_list_repr += str(current.data) + " -> "  # type: ignore
            current = current.next  # type: ignore
            if current == self.head:
                break
        linked_list_repr += "(back to head)"
        return linked_list_repr

    def __len__(self):
        """
        A function that returns the length of the circular linked list.
        """
        return self.length


list1 = CircularSinglyLinkedList()
list1.insert_beginning(7)
list1.insert_beginning(8)
list1.insert_beginning(9)
list1.insert_end(10)
list1.insert_end(11)
list1.insert_end(12)
list1.insert_beginning(32)
list1.insert_end(2)
print(list1)
print(len(list1))

list1.insert_at_any_position(6, 6)
print(list1)

print(len(list1))
list1.insert_at_any_position(0, 10)
print(list1)

print(len(list1))
list1.insert_at_any_position(10, 10)
print(list1)
print(len(list1))
