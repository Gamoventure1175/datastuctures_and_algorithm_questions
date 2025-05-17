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
#This above algorithm only checks for adjacent pairs and not all the possible pairs

# print(two_sum(arr=example, target=target))
