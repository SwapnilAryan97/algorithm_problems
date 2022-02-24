class Solution:
    def reverse(self, x: int) -> int:
        if x==0: return 0
        if x<0:
            res = -int(str(-x)[::-1])
            if res<-2147483648:
                return 0
            return res
        
        res = int(str(x)[::-1])
        if res>2147483647:
            return 0
        return res