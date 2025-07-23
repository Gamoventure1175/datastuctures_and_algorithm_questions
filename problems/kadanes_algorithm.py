# ✅ Kadane's Algorithm - Essentials
# Efficiently compute the maximum sum of any contiguous subarray in a 1D array of numbers.

# 🔢 Core Logic

# Iterate through an array A of size n, maintaining two variables:
#       current_sum: Maximum sum ending at the current position
#       max_sum: Global maximum sum found so far


def kadanes_algorithm(A: list):
    current_sum = max_sum = A[0]
    n = len(A)

    for i in range(1, n):
        current_sum = max(A[i], current_sum + A[i])
        max_sum = max(max_sum, current_sum)
