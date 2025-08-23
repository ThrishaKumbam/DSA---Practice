def binary_search(sorted_array, target):
    """Perform binary search on a sorted array.
    
    Args:
        sorted_array (list): A sorted list of integers.
        target (int): The integer to search for.
        
    Returns:
        int: The index of the target if found, otherwise -1.
    """
    left, right = 0, len(sorted_array) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if target < sorted_array[mid]:
            right = mid - 1
        elif target > sorted_array[mid]:
            left = mid + 1
        else:
            return mid  # return index of the target
            
    return -1


if __name__ == "__main__":
    numbers = [1, 3, 5, 7, 9]
    target_value = 9
    
    result = binary_search(numbers, target_value)
    
    if result != -1:
        print(f"Target {target_value} found at index {result}")
    else:
        print(f"Target {target_value} not found in the list")
