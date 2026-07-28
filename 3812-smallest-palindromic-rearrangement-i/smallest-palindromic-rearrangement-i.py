class Solution:

  def smallestPalindrome(self, s: str) -> str:
    n = len(s)
    half_len = n // 2

    # Extract the first half characters and sort them
    half = sorted(s[:half_len])

    # Join the sorted half
    left = "".join(half)

    # Determine middle character if n is odd
    mid = s[half_len] if n % 2 != 0 else ""

    # Combine left + mid + right (reversed left)
    return left + mid + left[::-1]