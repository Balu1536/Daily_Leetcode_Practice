from typing import List

class Solution:
    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
        # Step 1: Build the graph (adj[u] contains nodes invoked by u)
        adj = [[] for _ in range(n)]
        for a, b in invocations:
            adj[a].append(b)

        # Step 2: Traverse from node k to find all suspicious methods
        suspicious = set()
        stack = [k]
        suspicious.add(k)
        
        while stack:
            curr = stack.pop()
            for neighbor in adj[curr]:
                if neighbor not in suspicious:
                    suspicious.add(neighbor)
                    stack.append(neighbor)

        # Step 3: Check if any non-suspicious method invokes a suspicious method
        for a, b in invocations:
            if a not in suspicious and b in suspicious:
                # Removal invalid: return all methods
                return list(range(n))

        # Step 4: Return only non-suspicious methods
        return [i for i in range(n) if i not in suspicious]