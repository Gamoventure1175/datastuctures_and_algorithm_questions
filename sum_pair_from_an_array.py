# Given an array arr[] of n integers and a target value, the task is to find whether there is a pair of elements in the array whose sum is equal to target.


def two_sum(arr: list, target: int) -> bool:
    """
    Takes an array and a target value and returns true if it finds a pair of elements from the array whose sum is equal to target
    """

    for i in range(1, len(arr)):
        if (arr[i - 1] + arr[i]) == target:
            return True
    return False


example = [0, -1, 2, -3, 1]
target = -2
# This above algorithm only checks for adjacent pairs and not all the possible pairs

# print(two_sum(arr=example, target=target))


# the o(n^2) approach
def two_sum_o2(arr: list, target: int) -> bool:
    """
    Takes a list (array) and searches for all possible pairs such that a + b = target and returns True if it finds it
    """

    for i in range(0, len(arr)):
        for j in range(0, len(arr)):
            if (arr[i] + arr[j]) == target:
                print((arr[i], arr[j]))
                return True

    return False


# This function takes o(n^2) time

# print(two_sum_o2(example, target))


def two_sum_another_approach(arr: list, target: int) -> bool:
    i = 0
    while i < len(arr):
        for j in range(i + 1, len(arr)):
            if (arr[i] + arr[j]) == target:
                print((i, j))
                return True
        i += 1
    return False


# This approach though better than previous in not checking duplicates and self pairs, it still uses O(n^2) time

# print(two_sum_another_approach(example, target))


# Using binary search and the fact that if target - arr[i] = complement is found in the array, the pair exists
def binary_search(arr, left, right, target):
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            return True
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return False


def two_sum_using_binary_search(arr: list, target):
    arr.sort()
    for i in range(0, len(arr)):
        complement = target - arr[i]

        if binary_search(arr, i + 1, len(arr) - 1, complement):
            return True
    return False

#the binary search takes o(log n) time and the we check the complement for all the elements in the loop, o(n) time
#so, it takes o(n*log n) time


example = [0, -1, 2, -3, 1, -3, 1, 2]
target = 3

# print(two_sum_using_binary_search(example, target))


#Using a set
def two_sum_using_set(arr, target):
    s = set()
    
    for num in arr:
        complement = target - num
        if complement in s:
            return True
        s.add(num)
    return False
#the look up of complement in the set is o(1) time and the loop takes o(n) time, so the function is o(n) time

print(two_sum_using_set(example, target))