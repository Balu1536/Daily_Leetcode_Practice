class Solution:
    def smallestSubsequence(self, s: str) -> str:

        # Store last occurrence of each character
        last = {}

        for i, ch in enumerate(s):
            last[ch] = i

        # Characters already present in stack
        visited = set()

        # Stack to build answer
        stack = []

        for i, ch in enumerate(s):

            # Skip if already in stack
            if ch in visited:
                continue

            # Remove larger characters if they appear again later
            while (stack and
                   stack[-1] > ch and
                   last[stack[-1]] > i):

                visited.remove(stack.pop())

            stack.append(ch)
            visited.add(ch)

        return "".join(stack)