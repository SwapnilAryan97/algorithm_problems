class Solution:
    def addDigits(self, num: int) -> int:
        res = num
        temp = str(num)
        
        while len(temp)>1:
            res=0
            for s in temp:
                res+=int(s)
            temp = str(res)
        
        return res
            