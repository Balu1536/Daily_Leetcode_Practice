class Solution:
    def findGCD(self, nums: List[int]) -> int:
        mn=min(nums)
        mx=max(nums)

        while mn:
            mx,mn=mn,mx%mn
        return mx