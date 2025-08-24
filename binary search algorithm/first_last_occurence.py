def first_occurrence(arr, target):
    """
    Find the index of the first occurrence of target in a sorted array.

    Args:
        arr (list): A sorted list of comparable elements.
        target: The value to search for.

    Returns:
        int: The index of the first occurrence of target.
             Returns -1 if target is not found.

    Example:
        >>> first_occurrence([1, 2, 2, 2, 3, 4, 5], 2)
        1
    """
    low, high = 0, len(arr) - 1
    result = -1

    while low <= high:
        mid = low + (high - low) // 2
        if arr[mid] == target:
            result = mid
            high = mid - 1  # Look further left
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return result


def last_occurrence(arr, target):
    """
    Find the index of the last occurrence of target in a sorted array.

    Args:
        arr (list): A sorted list of comparable elements.
        target: The value to search for.

    Returns:
        int: The index of the last occurrence of target.
             Returns -1 if target is not found.

    Example:
        >>> last_occurrence([1, 2, 2, 2, 3, 4, 5], 2)
        3
    """
    low, high = 0, len(arr) - 1
    result = -1

    while low <= high:
        mid = low + (high - low) // 2
        if arr[mid] == target:
            result = mid
            low = mid + 1  # Look further right
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return result


def count_occurrences(arr, target):
    """
    Count how many times target appears in a sorted array.

    Args:
        arr (list): A sorted list of comparable elements.
        target: The value to count.

    Returns:
        int: Number of times target appears in arr.

    Example:
        >>> count_occurrences([1, 2, 2, 2, 3, 4, 5], 2)
        3
    """
    first = first_occurrence(arr, target)
    last = last_occurrence(arr, target)

    if first == -1:
        return 0
    return last - first + 1


if __name__ == "__main__":
    # Example usage
    print(count_occurrences([1, 2, 2, 2, 3, 4, 5], 2))  # Expected output: 3
