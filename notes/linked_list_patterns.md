Most linked-list interview questions are combinations of these.

---

# Pattern 1: Traverse Once

Used when you just need to inspect nodes.

Examples:

* Length of list
* Search value
* Find maximum
* Print list

Template:

```python id="d6i4zv"
curr = head

while curr:
    # do something

    curr = curr.next
```

Complexity:

```text id="1q8n3h"
O(n)
```

---

# Pattern 2: Previous + Current

Used when deleting or inserting.

Examples:

* Remove element
* Delete node by value
* Remove duplicates

Template:

```python id="2s1eqv"
prev = None
curr = head

while curr:
    ...
    prev = curr
    curr = curr.next
```

Key idea:

```text id="6h2flc"
To modify a node's link,
you usually need the previous node.
```

---

# Pattern 3: Dummy Node

Probably the most useful interview pattern.

Examples:

* Remove Nth node
* Remove elements
* Merge lists
* Partition list

Template:

```python id="4t8kmo"
dummy = ListNode(0)
dummy.next = head
```

Key idea:

```text id="44d0s7"
Turn head operations
into normal operations.
```

Without dummy:

```text id="r4r0ot"
Delete head
Special case
```

With dummy:

```text id="5c4sz4"
Delete head
Same as deleting any node
```

---

# Pattern 4: Fast and Slow Pointers

One pointer moves faster.

Examples:

* Find middle
* Detect cycle
* Remove Nth from end

Template:

```python id="6qq9z4"
slow = fast = head

while fast and fast.next:
    slow = slow.next
    fast = fast.next.next
```

Usually:

```text id="o0kx42"
slow -> middle
```

---

# Pattern 5: Reverse List

Extremely important.

Examples:

* Reverse Linked List
* Palindrome List
* Reorder List
* Reverse K Group

Template:

```python id="e2b3ib"
prev = None
curr = head

while curr:
    nxt = curr.next

    curr.next = prev

    prev = curr
    curr = nxt
```

Result:

```text id="n9y4w5"
prev
```

becomes the new head.

---

# Pattern 6: Split + Reverse + Merge

This is the pattern you're currently learning.

Examples:

* Reorder List
* Palindrome Linked List

Workflow:

```text id="6mqo9w"
Find middle

Split

Reverse second half

Merge
```

This pattern appears constantly.

---

# Pattern 7: Two Lists Walking Together

Examples:

* Merge Two Sorted Lists
* Intersection of Lists

Template:

```python id="x3rvvq"
while a and b:
    ...
```

Key idea:

```text id="shtr54"
Compare heads.

Move one pointer.
```

---

# Pattern 8: Weaving / Zipping Lists

Examples:

* Reorder List

Given:

```text id="7e54fo"
1 -> 2 -> 3

6 -> 5 -> 4
```

Produce:

```text id="rq9grz"
1 -> 6 -> 2 -> 5 -> 3 -> 4
```

Template:

```python id="dkz1kg"
first_next = first.next
second_next = second.next

first.next = second
second.next = first_next
```

---

# Pattern 9: Cycle Pattern

Examples:

* Detect cycle
* Find cycle start

Always:

```python id="h6iqmd"
slow
fast
```

If they meet:

```text id="jk9z1i"
cycle exists
```

---

# Pattern 10: Pointer Distance Pattern

Examples:

* Remove Nth from end

Idea:

```text id="gb8r8l"
Keep fast and slow
exactly n apart.
```

Then when:

```text id="x93bnm"
fast reaches end
```

```text id="d32l1z"
slow reaches target
```

---

# The Meta Pattern

Most medium linked-list problems reduce to:

```text
Traverse
Previous/Current
Dummy Node
Fast/Slow
Reverse
Merge
```

For example:

### Reorder List

```text
Fast/Slow
+
Reverse
+
Merge
```

---

### Palindrome Linked List

```text
Fast/Slow
+
Reverse
+
Compare
```

---

### Remove Nth From End

```text
Dummy Node
+
Pointer Distance
```

---

### Merge Two Sorted Lists

```text
Dummy Node
+
Two Lists Walking Together
```

---

