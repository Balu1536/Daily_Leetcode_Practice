class Solution:
    def sumAndMultiply(self, s: str, queries: List[List[int]]) -> List[int]:
        MOD = 10**9 + 7
        m = len(s)
        
        # Extract non-zero digits and their original positions
        nz_digits = []
        nz_positions = []
        for i, ch in enumerate(s):
            if ch != '0':
                nz_digits.append(int(ch))
                nz_positions.append(i)
                
        n = len(nz_digits)
        
        # Precompute power of 10 modulo MOD
        pow10 = [1] * (n + 1)
        for i in range(1, n + 1):
            pow10[i] = (pow10[i-1] * 10) % MOD
            
        # Precompute prefix sums and prefix values
        pref_sum = [0] * (n + 1)
        pref_val = [0] * (n + 1)
        for i in range(n):
            pref_sum[i+1] = pref_sum[i] + nz_digits[i]
            pref_val[i+1] = (pref_val[i] * 10 + nz_digits[i]) % MOD
            
        # Precompute next and previous non-zero digit index mapping
        next_nz = [n] * m
        curr = n
        for i in range(m - 1, -1, -1):
            if s[i] != '0':
                curr = bisect_left(nz_positions, i) # or track via pointers
            next_nz[i] = curr
            
        prev_nz = [-1] * m
        curr = -1
        for i in range(m):
            if s[i] != '0':
                curr = bisect_left(nz_positions, i)
            prev_nz[i] = curr

        # Optimizing the mapping lookups without repeated binary search
        # We can build a direct mapping array for O(1) lookups
        next_nz_idx = [n] * (m + 1)
        prev_nz_idx = [-1] * (m + 1)
        
        idx = 0
        for i in range(m):
            while idx < n and nz_positions[idx] < i:
                idx += 1
            next_nz_idx[i] = idx
            
        idx = n - 1
        for i in range(m - 1, -1, -1):
            while idx >= 0 and nz_positions[idx] > i:
                idx -= 1
            prev_nz_idx[i] = idx
            
        ans = []
        for l, r in queries:
            L = next_nz_idx[l]
            R = prev_nz_idx[r]
            
            if L > R:
                ans.append(0)
            else:
                # Calculate digit sum
                digit_sum = pref_sum[R+1] - pref_sum[L]
                
                # Calculate concatenated value x % MOD
                length = R - L + 1
                x = (pref_val[R+1] - pref_val[L] * pow10[length]) % MOD
                
                ans.append((x * digit_sum) % MOD)
                
        return ans