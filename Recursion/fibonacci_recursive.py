"""
Find the nth Fibonacci number using recursion.

Approach:
- The Fibonacci sequence is defined as:
  F(0) = 0, F(1) = 1
  F(n) = F(n-1) + F(n-2) for n > 1
- This recursive solution makes multiple calls for each n,
  leading to exponential time complexity.

Time Complexity: O(2^n)  → Each call branches into two more calls.
Space Complexity: O(n)   → Due to recursion call stack depth.
"""

def fibonacci_recursive(n):
    if n <= 1:  # base cases
        return n
    prev = fibonacci_recursive(n - 1)      # F(n-1)
    prev_prev = fibonacci_recursive(n - 2) # F(n-2)
    return prev + prev_prev


if __name__ == "__main__":
    test_n = 5
    print(f"Fibonacci number at position {test_n}: {fibonacci_recursive(test_n)}")
