class Solution:
    def minimumSum(self, num: int) -> int:
        x = num//100
        y = num%100
        
        
        res = min(x+y, int(str(x)[::-1]) + y, x + int(str(y)[::-1]), int(str(y)[::-1])+int(str(x)[::-1]))
        
        x = int(str(num)[0]+str(num)[3])
        y = int(str(num)[1:3])
        
        res = min(res, x+y, int(str(x)[::-1]) + y, x + int(str(y)[::-1]), int(str(y)[::-1])+int(str(x)[::-1]))

        
        return res