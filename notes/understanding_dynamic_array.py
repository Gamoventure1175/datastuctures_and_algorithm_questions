import sys

a = []
# Let's take a loop wise approach to understand how the python's list is a dynamic array
print(
    f"""
        Size of an array 'a' (container size) when there are {len(a)} elements in the array: {sys.getsizeof(a)}
        """
)
for i in range(10):
    a.append(i)
    print(
        f"""
        Size of an array 'a' (container size) when there are {len(a)} elements in the array: {sys.getsizeof(a)}
        """
    )
