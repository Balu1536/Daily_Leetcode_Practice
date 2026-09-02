class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        diff=[0]*(len(s)+1)
        for start, end, direction in shifts:

            value = 1 if direction == 1 else -1

            diff[start] += value
            diff[end + 1] -= value

        curr=0
        ans=[]
        for i in range(len(s)):
            curr+=diff[i]
            curr%=26
            c=s[i]
            new_char=chr(ord('a')+(ord(c)-ord('a')+curr)%26)
            ans.append(new_char)
        return "".join(ans)