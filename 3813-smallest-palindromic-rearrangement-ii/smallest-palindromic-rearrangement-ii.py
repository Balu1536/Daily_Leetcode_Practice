from collections import Counter
import math

class Solution:
    def smallestPalindrome(self, s: str, k: int) -> str:
        n = len(s)
        half_len = n // 2
        counts = Counter(s[:half_len])
        
        def count_permutations(remaining_counts, total_chars):
            res = 1
            curr_len = total_chars
            for ch in sorted(remaining_counts.keys()):
                cnt = remaining_counts[ch]
                if cnt > 0:
                    res *= math.comb(curr_len, cnt)
                    curr_len -= cnt
                    if res >= k:
                        return k + 1
            return res

        if count_permutations(counts, half_len) < k:
            return ""

        left_half = []
        
        for i in range(half_len):
            remaining_slots = half_len - 1 - i
            
            for char_code in range(26):
                ch = chr(ord('a') + char_code)
                if counts[ch] > 0:
                    counts[ch] -= 1
                    
                    num_ways = count_permutations(counts, remaining_slots)
                    
                    if num_ways >= k:
                        left_half.append(ch)
                        break
                    else:
                        k -= num_ways
                        counts[ch] += 1

        left_str = "".join(left_half)
        mid_char = s[half_len] if n % 2 == 1 else ""
        return left_str + mid_char + left_str[::-1]