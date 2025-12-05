"""
Basic CRUD operations
        append(value) → add to end (amortized O(1) in dynamic arrays)

        insert(index, value) → insert at position (O(n) worst case because shifting)

        [i] (retrieval) → get element at index (O(1))

        [i] = value (assignment) → set element at index (O(1))

        len(arr) → get length (O(1))

Removal operations
        pop() → remove last element (O(1))

        pop(i) → remove at index (O(n) worst case because shifting)

        remove(value) → remove first occurrence (O(n) because search + shift)

        Search-related
        search(value) → index of first occurrence (O(n))

        count(value) → count occurrences (O(n))

        contains(value) / value in arr → check membership (O(n) worst case)

Extra functionality you might see in arrays
        clear() → remove all elements (O(1) if you just reset size, O(n) if you explicitly free references)

        extend(iterable) → append all elements from another iterable (O(k) where k is new elements count)

        reverse() → reverse in place (O(n))

        sort() → sort in place (O(n log n) with typical algorithms)

        copy() → shallow copy of array (O(n))

        slice (arr[start:end:step]) → create a new array from part of the old one (O(k) for slice size)
"""

# Trying to implement a dynamic array using a low level array from ctypes that goes directly
# into the memory

import ctypes


class DynamicArray:
    def __init__(self):
        self._n = 0
        self._capacity = 1
        self._A = self._make_array(self._capacity)

    def __len__(self):
        """Returns the count of the elements in the array"""
        return self._n

    # Utilising the checking functionality if the index is valid into a single function
    def _index_checker(self, k):
        """Returns index (positive or negative) by checking if it is in the range of the size
        of the array and raises IndexError if it is not"""
        if k < 0:
            k += self._n
        if not 0 <= k < self._n:
            raise IndexError("Invalid index.")
        return k

    def __getitem__(self, k):
        """Returns the element at the index k in the array"""
        checked_index = self._index_checker(k)
        return self._A[checked_index]

    def __setitem__(self, k, new_obj):
        """Used to assign an element at a specific index k"""
        checked_index = self._index_checker(k)
        self._A[checked_index] = new_obj

    def _resize(self, c: int):
        """
        Resizes the internal array to the size of capacity c
        """
        B = self._make_array(c)
        for k in range(self._n):
            B[k] = self._A[k]
        self._A = B
        self._capacity = c

    def _make_array(self, c: int):
        """
        A function that takes in the capacity c (int) for assigning a continous blog of memory (array) using the ctypes.py_object method
        """
        return (ctypes.py_object * c)()

    def append(self, obj):
        """Add object to the end of the array"""
        if self._n == self._capacity:
            # Whenever the number of elements in the reaches half the size of the array, we double it?
            self._resize(2 * self._capacity)

        self._A[self._n] = obj
        self._n += 1

    def __repr__(self):
        """Representing the array in the form [obj, obj, obj, ...]"""

        readable_form = "["
        for k in range(self._n):
            if k == self._n - 1:
                readable_form += str(self._A[k])
                continue
            readable_form += str(self._A[k]) + ", "
        readable_form += "]"

        return readable_form

    def pop(self, k: int | None = None):
        """Removes the last element from the array
        Optionally, if the index of the element to be removed is provided, it will remove that specific
        element and resize the array if needed"""
        if self._n == 0:
            raise IndexError("Cannot pop from an empty array")

        if k:
            checked_index = self._index_checker(k)
            popped_obj = self._A[checked_index]
            self._A[checked_index] = None
            # Shifting the elements up the deleted element
            for i in range(checked_index + 1, self._n):
                self._A[i - 1] = self._A[i]
            self._A[self._n - 1] = None
            self._n -= 1
        else:
            popped_obj = self._A[self._n - 1]
            self._A[self._n - 1] = None
            self._n -= 1

        if self._n == (self._capacity // 2):
            self._resize(self._capacity // 2)

        return popped_obj

    def insert(self, k, new_object):
        """Insert a new object at a specific index in the array. The elements in
        the array are shifted and the overall time complexity of the function is
        O(n-k+1)"""
        checked_index = self._index_checker(k)
        if self._n == self._capacity:
            self._resize(2 * self._capacity)

        for i in range(self._n, checked_index, -1):
            self._A[i] = self._A[i - 1]

        self._A[checked_index] = new_object
        self._n += 1


def testing_dynamic_array():
    """Tests the resizing and then shrinking of the dynamic array when I use append and pop methods"""
    sequence = DynamicArray()
    for i in range(1, 11):
        print(
            f"Capacity: {sequence._capacity}, Internal size: {ctypes.sizeof(sequence._A)} bytes"
        )
        sequence.append(i)

    for i in range(1, 11):
        print(
            f"Capacity: {sequence._capacity}, Internal size: {ctypes.sizeof(sequence._A)} bytes"
        )
        sequence.pop()


if __name__ == "__main__":
    test_array = DynamicArray()
    for i in range(1, 11):
        test_array.append(i)

    print("The array that was formed: ", test_array)
    print(f"Using negative indexing: {test_array[-1]}")
    print(f"Using positive indexing: {test_array[0]}")
    print(f"The length of the array: {len(test_array)}")

    # Reassigning
    test_array[5] = "it worked"
    print(f"Reassigning using positive indexes: {test_array}")
    test_array[-2] = "miracle"
    print(f"Reassiging using negative indexes: {test_array}")

    for i in range(5):
        test_array.pop()

    print(f"The array after popping elements: {test_array}")
    print(f"The length of the array: {len(test_array)}")

    # print("Testing the array resizing mechanism of the dynamic array: ")
    # testing_dynamic_array()

    # Inserting an element in the array
    test_array.insert(3, ";")
    print(
        f"The array after inserting an element in the array using positive index: {test_array}"
    )

    test_array.insert(-2, "where might this be?")
    print(
        f"The array after inserting an element in the array using negative index: {test_array}"
    )

    # Popping a specific element from the array using index
    popped = test_array.pop(2)
    print(f"Popped element from the array using positive index 2: {popped}")
    print(f"The array after popping: {test_array}")

    popped = test_array.pop(-2)
    print(f"Popped element from the array using negative index -2: {popped}")
    print(f"The array after popping: {test_array}")
