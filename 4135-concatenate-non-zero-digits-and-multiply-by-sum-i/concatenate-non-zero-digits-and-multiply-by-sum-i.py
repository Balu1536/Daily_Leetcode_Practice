class Solution:
    def sumAndMultiply(self, n: int) -> int:
        if n == 0:
            return 0
            
        digits = []
        
        while n > 0:
            digit = n % 10
            if digit != 0:
                digits.append(digit)
            n //= 10
            

        if not digits:
            return 0
            
        x = 0
        digit_sum = 0
        for d in reversed(digits):
            x = x * 10 + d
            digit_sum += d
            
        return x * digit_sum