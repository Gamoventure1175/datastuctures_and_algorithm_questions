"""
Given two integer arrays A and B of size N. There are N gas stations along a circular route, where the amount of gas at station i is A[i].

You have a car with an unlimited gas tank and it costs B[i] of gas to travel from station i to its next station (i+1). You begin the journey with an empty tank at one of the gas stations.

Return the minimum starting gas station's index if you can travel around the circuit once, otherwise return -1.

You can only travel in one direction. i to i+1, i+2, ... n-1, 0, 1, 2.. Completing the circuit means starting at i and ending up at i again.

"""

# Though process for the solution is as follow:
"""
A circular linked list was already learned and built by me in the datastructures folder.

So, for the solution, I am going to use the above mentioned circular singly linked list with the following traversal implementation
    - dial_traversal: It initializes start and end pointers on a particular node of the list and then, like a dial phone, the start pointer traverses the whole list until it reaches the end. 
    We repeat this process for all indexes in the circular linked list, meaning that every time, the start and end pointers keep on shifting to the next node until the next node is the head node again. 
    
Also, the following logic needs to be implemented when trying to solve this problem as it sets the rules of traversal and loop breaking:

1. Car's initial fuel level will be determined by the starting point of the journey:
    current_fuel = A[i]
2. For a journey of 'i' to 'i+1', fuel that is needed is determined by B[i]:
    fuel_needed = B[i]
3. Fuel that will be used up for going from point 'i' to 'i+1' should be calculated using:
    fuel_after = curr_fuel - fuel_needed
5. If this journey (i -> i+1) is possible, repeat the same until the car is back to the same spot.  Report this starting index as the solution
6. If the journey (i -> i+1) is not possible, check if the current position of the start is the same as the ending point. If it is the same, report the index of the starting point or else continue to the next index as the start point.
7. If none of the journies are ever completed, return -1
"""

# Trying to code this

from datastructures.circular_singly_linked_list import CircularSinglyLinkedList
from typing import Any


def gas_station_solution(a: list[Any], b: list[Any]):
    A = CircularSinglyLinkedList()
    for element in a:
        A.insert_end(element)

    for i in range(len())


if __name__ == "__main__":
    gas_station_solution(a=[2, 5, 6, 0], b=[3, 5, 2, 6])
