class Node:
    """
    # Definition of a base node used by the circular singly linked list

    ## Arguments include:
    - data = the data that the node carries
    - next = pointer to the next node in the linked list
    """

    def __init__(self, data: int | None = None):
        self.data: int | None = data
        self.next: Node | None = None


class CircularSinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_beginning(self, data: int) -> None:
        """
        #### A function that inserts a node at the beginning of the circular singly linked list

        ##### Arguments:
        - data = *int* value
        """
        new_node = Node(data=data)

        if self.head is None:  # check for if the linked list is empty
            self.head = new_node
            new_node.next = new_node
            self.tail = new_node

        else:
            if self.tail is None:
                raise Exception(
                    "Tail must be assigned to something if the head is not None"
                )
            else:
                new_node.next = self.head
                self.tail.next = new_node
                self.head = new_node

        self._check_invariants()

    def insert_end(self, data: int) -> None:
        """
        #### A function that inserts a node at the ending of the circular singly linked list

        ##### Arguments:
        - data = *int* value
        """

        new_node = Node(data=data)

        if self.head is None:
            self.head = new_node
            new_node.next = new_node
            self.tail = new_node
        else:
            if self.tail is None:
                raise Exception(
                    "Tail must be assigned to something if the head is not None"
                )
            else:
                self.tail.next = new_node
                new_node.next = self.head
                self.tail = new_node

        self._check_invariants()

    def _check_invariants(self):
        if self.head is None:
            assert self.tail is None, "Tail should be None when head is None"
        else:
            assert self.tail is not None, "Tail cannot be None if head is not None"
            assert (
                self.tail.next == self.head
            ), "Tail's next should always be head in a circular linked list"

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
