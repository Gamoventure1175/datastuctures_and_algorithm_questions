# Circular singly linked list
![diagram](
    https://media.geeksforgeeks.org/wp-content/uploads/20240806145414/Node-structure-of-circular-linked-list.webp
)

## Trying to code a ***circular singly linked list***
1. Define *Node* class
    - *data* should be typed **'any | None'**. (*any* can be any other thing like *int* or *str*)
    - *next* should be typed **'Node | None'**. 

```py
class Node:
    def __init__(self, data: int | None = None):
        self.data: int | None = data
        self.next: Node | None = None
```
2. Define a *CircularSinglyLinkedList* class with init having head and tail pointing to None? 

```py
class CircularSinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
```

## Representation of a Circular Singly Linked List

### Implementating logic for representing this circular singly linked list: 
1. Initialize a `__repr__` function
2. Return ***'Linked list is empty'*** when ***self.head*** is **None**.
3. Assign a **current** pointer to ***self.head***
4. Using the current pointer, keep iterating over to the next *Nodes* until:```current.next == self.head```
5. While iterating, use **current.data** to form *string* representation of the data inside the nodes in the list
6. At the end, return the string representation of the *linked_list*

### Expected output
```txt
(head) n1 -> n2 -> n3 -> n4 -> n1 (back to head)
 ```

## Operations on circular singly linked list
1. Insertion
    - Insertion at the empty list
    - Insertion at the beginning
    - Insertion at the end
    - Insertion at the given position

2. Deletion
    - Delete the first node
    - Delete the last node
    - Delete the node from any position

3. Searching

## Assumption about head and tail
All the subsequent implementation ***approaches*** rely on the following assumption:

1. If *head* is **None** then *tail* has to be **None**
2. If *head* is **not None** then *tail* **cannot** be **None**
3. If *head* is **not None** then *tail.next* has to be **head**

An **assertive check** regarding the same is as follows:
```py
def _check_invariants(self):
    if self.head is None:
        assert self.tail is None, "Tail should be None when head is None"
    else:
        assert self.tail is not None, "Tail cannot be None if head is not None"
        assert (
            self.tail.next == self.head
        ), "Tail's next should always be head in a circular linked list"
```


## Insertion
### 1. Insertion in an empty list in the circular linked list

![Inserting in an empty circular linked list](https://media.geeksforgeeks.org/wp-content/uploads/20240806193408/Insertion-in-an-empty-list-in-circular-linked-list.webp)

### 2. Insertion at the beginning in circular linked list
![Insertion in the beginning](
    https://media.geeksforgeeks.org/wp-content/uploads/20240806150314/Insertion-at-the-beginning-of-circular-linked-list.webp
)

#### Trying to code this operation
1. Define a function named ***insert_beginning***
2. It should take one argument: *data*: *int*
3. *data* argument cannot be None
4. Create a new *Node* using this *data* parameter
5. *IF THE CIRCULAR LIST IS EMPTY*:
    1. self.head = new_node
    2. new_node.next = new_node
    3. self.tail = new_node
6. *IF THE CIRCULAR LIST IS NOT EMPTY*:
    1. new_node.next=self.head
    2. self.tail.next = new_node
    3. self.head = new_node
7. Add a check enforcement where if head is not none, then the tail should not be none.

#### Code for this operation
```py
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
```

### 3. Insertion at the end in circular linked list

![Insertion at the end](
    https://media.geeksforgeeks.org/wp-content/uploads/20240806150353/Insertion-at-the-end-of-circular-linked-list.webp
)

#### Trying to code this operation
1. Define a function named *insert_end*
2. It will take one argument, **data: int**
3. Create a *new node* using this data argument
4. *IF THE CIRCULAR LIST IS EMPTY*:
    1. self.head = new_node
    2. new_node.next = new_node
    3. self.tail = new_node
5. *IF THE CIRCULAR LIST IS NOT EMPTY:*
    1. self.tail.next = new_node
    2. new_node.next = self.head
    3. self.tail = new_node

#### Code for this operation
```py
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
```

### 4. Insertion at a specific position in circular linked list

![Insertion at a specific location](
    https://media.geeksforgeeks.org/wp-content/uploads/20240806150431/Insertion-at-specific-position-of-circular-linked-list.webp
)


#### Edge cases for this operation
1. *Empty circular linked list* : This will occur when the list is empty.

2. *Adding the element at the start* : This will occur if the positional index is 0

3. *Adding the element to the end*: This will occur if the positional index is, index == self.length - 1

4. *Out of range position* : This will occur if the positional index is not in the range [0, length), where, '[' -> included and ')' not included