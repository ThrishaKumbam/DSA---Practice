def upper_bound(arr, target):
    """
    Find the index of the first element in a sorted array that is greater than the target.
    
    Args:
        arr : A sorted array of comparable elements.
        target: The value to search for.
    
    Returns:
        int: The index of the first element > target.
             If all elements are smaller, returns len(arr).
    
    Example:
        >>> upper_bound([1, 2, 2, 4, 5], 2)
        1
        >>> upper_bound([1, 2, 2, 4, 5], 3)
        3
    """
    low, high = 0, len(arr) - 1
    result = len(arr)  # Default: target is larger than all elements

    while low <= high:
        mid = low + (high - low) // 2

        if arr[mid] > target:
            result = mid      # Potential answer found
            high = mid - 1    # Look for an earlier occurrence
        else:
            low = mid + 1

    return result


if __name__ == "__main__":
    # Example usage
    print(upper_bound([1, 2, 2, 4, 5], 2))  # Expected output: 1
