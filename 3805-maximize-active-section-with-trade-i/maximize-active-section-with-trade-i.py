class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        total_ones = s.count('1')
        t = '1' + s + '1'
        
        # Filter out 0-length blocks caused by consecutive '1's
        zero_blocks = [len(b) for b in t.split('1') if len(b) > 0]
        
        if len(zero_blocks) < 2:
            return total_ones
        
        # Find maximum sum of any two adjacent 0-blocks
        max_delta = max(zero_blocks[i] + zero_blocks[i+1] for i in range(len(zero_blocks) - 1))
        
        return total_ones + max_delta