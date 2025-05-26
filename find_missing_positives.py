# Given an unsorted integer array nums. Return the smallest positive integer that is not present in nums.


# I start with a brute force method that first separates the positives from the array and then works from there
# When I separate the array and get a array of positives, it's possible that the array could be:
#       1. empty (no positive) -> smallest positive = 1
#       2. only have one number (only one positive) -> if it is 1: smallest positive = 2
#                                                   -> if it is >1: smallest positive = 1
#       3. have more than 1 positive number ->
#               find the smalles and the largest inside the array: sm, lg
#               if sm is not 1 -> obviously then smallest positive integer is 1
#               else -> loop from sm <-> lg and see if there are any missing
#               elements in between -> the first missing element is the smallest positive integer
def find_missing_positives(nums: list[int]) -> int:
    """
    A function that takes an array of randomnly distributed integers and returns the smallest positive integer that is not in the array
    """
    positives = set()
    smallest = 1
    for num in nums: #o(n)
        if num > 0:
            positives.add(num)

    number_of_positives = len(positives)

    if number_of_positives == 0:
        return 1
    elif number_of_positives == 1:
        if 1 in positives:
            return 2
        else:
            return 1

    sm = min(positives)
    lg = max(positives)

    if sm != 1:
        return 1

    for i in range(sm, lg + 1): #o(n)
        if i not in positives:
            smallest = i
            return smallest
    smallest = lg + 1

    return smallest


print(find_missing_positives([7,8,9,11,12]))
