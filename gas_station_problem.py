# Trying to implement a circular singly linked list
from datastructures.linked_list.circular_singly_linked_list import (
    CircularSinglyLinkedList,
)


class Node:
    """
    # Definition of a base node used by the circular singly linked list

    ## Arguments include:
    - data = the data that the node carries
    - next = pointer to the next node in the linked list
    """

    def __init__(self, data):
        self.data = data
        self.next: Node | None = None

    # def __str__(self):
    #     return f"[{self.data}, {self.next}]"


# example of creating a circular linked list
first = Node(1)
second = Node(2)
third = Node(3)

first.next = second
second.next = third
third.next = first  # Closing the list to form a circle


print(first.next)
print(second.next)
print(third.next)
