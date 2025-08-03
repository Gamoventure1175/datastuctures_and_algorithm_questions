"""
The size difference between a referential sequence (python's list) and a compact sequence (python's string)
"""

from sys import getsizeof
from pympler import asizeof

reference_seq = [
    str(bytearray(b"a")) for _ in range(10000)
]  # This does defeat the default string interning that happens in python
print(f"The length of the reference based sequence is: {len(reference_seq)}")
print(
    f"The container size of the reference based sequence is: {getsizeof(reference_seq)}"
)
# getsizeof() is misleading because it only gives the size of the array/list container and not the actual size of that sequence
# by also taking into account the size consumed by the content.
"""
That is why, getsizeof will show the size of the string as higher than compared to the array despite having the same length
and the same element inside them. So this is not a good test measure this.
"""
print(
    f"The actual full size of the reference based sequence is: {asizeof.asizeof(reference_seq)}"
)

compact_seq = "a" * 10000

print(f"The length of the compact sequence is: {len(compact_seq)}")
print(f"The size of the compact sequence is: {getsizeof(compact_seq)}")

print(
    f"""
All 'a' inside the reference sequence do point to the same a.
For prove you can check the following:
Id of the first element in the list: {id(reference_seq[0])}
Id of the second element in the list: {id(reference_seq[8])}
"""
)

# How many unique 'a' strings exist in the list?
unique_ids = len(set(id(x) for x in reference_seq))
print(
    f"Number of unique string objects: {unique_ids}"
)  # This will return just 1 because:
"""
In the newer versions of python (>3.10), for strings that are smaller in that 20 characters (ascii ones), 
they will be interned in the list and all the references would be to the same string instead of creating new ones.

"""
