"""
You have a set which contains all positive integers [1, 2, 3, 4, 5, ...].

Implement the SmallestInfiniteSet class:

    SmallestInfiniteSet() Initializes the SmallestInfiniteSet object to contain all positive integers.
    int popSmallest() Removes and returns the smallest integer contained in the infinite set.
    void addBack(int num) Adds a positive integer num back into the infinite set, if it is not already in the infinite set.

 

Example 1:

Input
["SmallestInfiniteSet", "addBack", "popSmallest", "popSmallest", "popSmallest", "addBack", "popSmallest", "popSmallest", "popSmallest"]
[[], [2], [], [], [], [1], [], [], []]
Output
[null, null, 1, 2, 3, null, 1, 4, 5]

Explanation
SmallestInfiniteSet smallestInfiniteSet = new SmallestInfiniteSet();
smallestInfiniteSet.addBack(2);    // 2 is already in the set, so no change is made.
smallestInfiniteSet.popSmallest(); // return 1, since 1 is the smallest number, and remove it from the set.
smallestInfiniteSet.popSmallest(); // return 2, and remove it from the set.
smallestInfiniteSet.popSmallest(); // return 3, and remove it from the set.
smallestInfiniteSet.addBack(1);    // 1 is added back to the set.
smallestInfiniteSet.popSmallest(); // return 1, since 1 was added back to the set and
                                   // is the smallest number, and remove it from the set.
smallestInfiniteSet.popSmallest(); // return 4, and remove it from the set.
smallestInfiniteSet.popSmallest(); // return 5, and remove it from the set.

 

Constraints:

    1 <= num <= 1000
    At most 1000 calls will be made in total to popSmallest and addBack.
"""

# Attempt 1: Using intuition and the problem constraints
# class SmallestInfiniteSet:
#     from heapq import heappush, heappop
#     def __init__(self):
#         self._heap = [n for n in range(1, 1001)]
#         self._set = set(self._heap)
# 
#     def popSmallest(self) -> int:
#         toRemove = heappop(self._heap)
#         self._set.remove(toRemove)
#         return toRemove
# 
#     def addBack(self, num: int) -> None:
#         if num not in self._set:
#             heappush(self._heap, num)
#             self._set.add(num)

# Attempt 2: Better solution
class SmallestInfiniteSet:
    from heapq import heappush, heappop

    def __init__(self):
       self._heap = []
       self._curr = 1
       self._set = set()

    def popSmallest(self) -> int:
        if self._heap and self._heap[0] < self._curr:
            toRemove = heappop(self._heap)
            self._set.remove(toRemove)
            return toRemove
        self._curr += 1
        return self._curr - 1

    def addBack(self, num: int) -> None:
        if num < self._curr and num not in self._set:
            heappush(self._heap, num)
            self._set.add(num)


