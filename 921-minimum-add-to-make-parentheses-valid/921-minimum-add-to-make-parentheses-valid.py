class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        res = 0
        temp = 0
        for i in range(len(s)):
            if s[i]==")":
                if res==0: temp+=1
                else: res-=1 
            else: res+=1
            
        return res + temp