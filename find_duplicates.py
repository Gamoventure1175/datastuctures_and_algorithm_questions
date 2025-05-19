# Given an array arr[] of n elements that contains elements from 0 to n-1,
# with any of these numbers appearing any number of times. The task is to
# find the repeating numbers.

# Didn't start with the brute force method of using two arrays because that's simple

from typing import Dict, Any

# Using a python dictionary for an O(n) approach as lookups in dictionary can cost
# only o(1) time in python


def duplicates_dictionary(arr: list) -> tuple:
    """
    Takes an array (list) and finds all the duplicates in it
    and returns a tuple with all the duplicate values once
    """

    s: Dict[Any, int] = {}
    duplicates: set[int] = set()

    for elem in arr:
        if elem in s:
            s[elem] += 1
        else:
            s[elem] = 1

    for key in s.keys():
        if s[key] > 1:
            duplicates.add(key)

    return tuple(duplicates)


example = ["a", "b", "a", "c", "d", "b", "e"]
print(duplicates_dictionary(example))
