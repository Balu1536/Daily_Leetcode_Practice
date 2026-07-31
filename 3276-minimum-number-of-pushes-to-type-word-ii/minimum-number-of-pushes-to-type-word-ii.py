class Solution:
    def minimumPushes(self, word: str) -> int:
        freq = Counter(word)
        sorted_counts = sorted(freq.values(), reverse=True)
        
        total_pushes = 0
        for i, count in enumerate(sorted_counts):
            multiplier = (i // 8) + 1
            total_pushes += count * multiplier
            
        return total_pushes