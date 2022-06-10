class Solution:
    def addBinary(self, a: str, b: str) -> str:
#         a = list(a)
#         b = list(b)
#         carry=0
#         res=""
        
#         while a or b or carry:
#             if a:
#                 carry+= int(a.pop())
#             if b:
#                 carry+= int(b.pop())
            
#             res += str(carry%2)
#             carry //= 2
#         return res[::-1]

        "Leetcode best solution wrt time"
        a1 = int(a)
        b1 = int(b)
        total = 0
        
        sum = int(a, 2) + int(b, 2)
        return bin(sum)[2:]
            