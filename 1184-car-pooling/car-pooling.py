class Solution(object):
    def carPooling(self, trips, capacity):
        """
        :type trips: List[List[int]]
        :type capacity: int
        :rtype: bool
        """
        diff=[0]*(1001)
        for i in trips:
            passengers=i[0]
            f=i[1]
            t=i[2]
            diff[f]+=passengers
            diff[t]-=passengers
        
        cur=0
        for i in diff:
            cur+=i
            if cur>capacity:
                return False
        return True