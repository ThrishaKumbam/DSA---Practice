"""
Check if a string is a palindrome using recursion and a single pointer.

Approach:
- Compare characters from the start and end moving toward the center.
- If all mirrored characters match, the string is a palindrome.

Time Complexity: O(n)   → Each character is compared once (up to n/2 comparisons).
Space Complexity: O(n)  → Due to recursion call stack.
"""

def is_palindrome_recursive(s, index=0):
    n = len(s)
    if index >= n // 2:  # base case: reached the middle
        return True
    if s[index] != s[n - index - 1]:  # mismatch
        return False
    return is_palindrome_recursive(s, index + 1)


# Example usage
if __name__ == "__main__":
    test_string = "MOM"
    print(f"Is '{test_string}' a palindrome? : {is_palindrome_recursive(test_string)}")
