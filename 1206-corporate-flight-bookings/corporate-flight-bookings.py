class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        diff=[0]*(n+2)
        for i in bookings:
            seats=i[2]
            first=i[0]
            last=i[1]
            diff[first]+=seats
            diff[last+1]-=seats
        cur=0
        for i in range(len(diff)):
            diff[i]+=cur
            cur=diff[i]
        return diff[1:n+1]