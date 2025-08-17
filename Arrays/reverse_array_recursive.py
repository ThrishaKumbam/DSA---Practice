"""
Reverse an array using recursion and a single pointer (index).
Approach: Swap elements from start and end until the middle is reached.
Exact Swaps: n/2
Time Complexity: O(n)   → Linear, since constants are ignored.
Space Complexity: O(n)  → Due to recursion call stack.
"""

def reverse_array_recursive(arr, index=0):
    n = len(arr)
    if index >= n // 2:  # base case
        return arr
    arr[index], arr[n - index - 1] = arr[n - index - 1], arr[index]  # swap
    return reverse_array_recursive(arr, index + 1)

# Example usage
arr = [7, 14, 21, 28, 35, 42, 49]
print("Original array:", arr)
print("Reversed array:", reverse_array_recursive(arr))
