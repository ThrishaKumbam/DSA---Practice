"""
binary_search_algorithm/lower_bound.py

Implementation of the Lower Bound algorithm using binary search.
"""


def lower_bound(arr, target):
    """
    Find the index of the first element in a sorted array that is greater than or equal to target.
    
    Args:
        arr (list): A sorted list of comparable elements.
        target: The value to search for.
    
    Returns:
        int: The index of the first element >= target.
             If all elements are smaller, returns len(arr).
    
    Example:
        >>> lower_bound([1, 2, 2, 4, 5], 2)
        1
        >>> lower_bound([1, 2, 2, 4, 5], 3)
        3
    """
    low, high = 0, len(arr) - 1
    result = len(arr)  # Default: target is larger than all elements

    while low <= high:
        mid = low + (high - low) // 2

        if arr[mid] >= target:
            result = mid      # Potential answer found
            high = mid - 1    # Look for an earlier occurrence
        else:
            low = mid + 1

    return result


if __name__ == "__main__":
    # Example usage
    print(lower_bound([1, 2, 2, 4, 5], 2))  # Expected output: 1
