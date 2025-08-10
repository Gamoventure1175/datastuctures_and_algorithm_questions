# Understanding operations in a dynamic array
---
The following is a broader category of all the operations on a dynamic array
--- 

* Basic CRUD operations
    1. ***append(value)*** → add to end (amortized O(1) in dynamic arrays)

    2. ***insert(index, value)*** → insert at position (O(n) worst case because shifting)

    3. ***[i] (retrieval)*** → get element at index (O(1))

    4. ***[i]*** = value (assignment) → set element at index (O(1))

    5. ***len(arr)*** → get length (O(1))

* Removal operations
    1. ***pop()*** → remove last element (O(1))

    2. ***pop(i)*** → remove at index (O(n) worst case because shifting)

    3. ***remove(value)*** → remove first occurrence (O(n) because search + shift)

* Search-related
    1. ***search(value)*** → index of first occurrence (O(n))

    2. ***count(value)*** → count occurrences (O(n))

    3. ***contains(value) / value in arr*** → check membership (O(n) worst case)

* Extra functionality you might see in arrays
    1. ***clear()*** → remove all elements (O(1) if you just reset size, O(n) if you explicitly free references)

    2. ***extend(iterable)*** → append all elements from another iterable (O(k) where k is new elements count)

    3. ***reverse()*** → reverse in place (O(n))

    4. ***sort()*** → sort in place (O(n log n) with typical algorithms)

    5. ***copy()*** → shallow copy of array (O(n))

    6. ***slice (arr[start:end:step])*** → create a new array from part of the old one (O(k) for slice size)
"""