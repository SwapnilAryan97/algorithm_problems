class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        res = 0
        i=3
        while i<=len(s):
            temp = s[i-3:i]
            if temp[0]!=temp[1] and temp[1]!=temp[2] and temp[0]!=temp[2]:
                res+=1
            i+=1
        return res