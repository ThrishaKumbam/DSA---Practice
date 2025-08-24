def binary_search_recursive(sorted_array, target, left, right):
    """Recursive binary search implementation.
    
    Args:
        sorted_array (list): A sorted list of integers.
        target (int): The integer to search for.
        left (int): Starting index of the search range.
        right (int): Ending index of the search range.
        
    Returns:
        int: The index of the target if found, otherwise -1.
    """
    if left > right:
        return -1  # base case: target not found
    
    mid = (left + right) // 2
    
    if target < sorted_array[mid]:
        return binary_search_recursive(sorted_array, target, left, mid - 1)
    elif target > sorted_array[mid]:
        return binary_search_recursive(sorted_array, target, mid + 1, right)
    else:
        return mid


if __name__ == "__main__":
    numbers = [1, 3, 5, 7, 9]
    target_value = 7
    
    result = binary_search_recursive(numbers, target_value, 0, len(numbers) - 1)
    
    if result != -1:
        print(f"Target {target_value} found at index {result}")
    else:
        print(f"Target {target_value} not found in the list")
