class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        def digitProduct(num:int):
            prod=1
            for digit in str(num):
                prod*=int(digit)
            return prod
        
        curr=n
        while digitProduct(curr)%t!=0:
            curr+=1
        return curr