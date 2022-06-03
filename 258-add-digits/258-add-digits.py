class Solution:
    def addDigits(self, num: int) -> int:
        return 1 + (num - 1) % 9 if num else 0
        
#         res = num
#         temp = str(num)
        
#         while len(temp)>1:
#             res=0
#             for s in temp:
#                 res+=int(s)
#             temp = str(res)
        
#         return res
        