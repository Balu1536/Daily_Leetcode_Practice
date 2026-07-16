import math

class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        prefixGcd = []
        mx = 0
        
        for num in nums:
            if num > mx:
                mx = num
            prefixGcd.append(math.gcd(num, mx))
            
        prefixGcd.sort()
        
        total_sum = 0
        left, right = 0, len(nums) - 1
        
        while left < right:
            total_sum += math.gcd(prefixGcd[left], prefixGcd[right])
            left += 1
            right -= 1
            
        return total_sum