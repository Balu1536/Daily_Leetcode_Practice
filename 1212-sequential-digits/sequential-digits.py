class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        digits = "123456789"
        result = []
        
        low_len = len(str(low))
        high_len = len(str(high))
        
        for length in range(low_len, high_len + 1):
            for i in range(10 - length):
                num = int(digits[i:i + length])
                if low <= num <= high:
                    result.append(num)
                    
        return result