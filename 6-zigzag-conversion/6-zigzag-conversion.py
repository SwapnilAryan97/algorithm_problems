class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows==1: return s
        res = ""
        cycle = 2*numRows -2
        for i in range(0,numRows):
            j=i
            #for j in range(i,len(s),j+cycle):
            while j<len(s):
                res = res + s[j]
                next_j = (j-i)+cycle-i
                if i!=0 and i!=numRows-1 and next_j<len(s):
                    res = res + s[next_j]
                j = j+cycle
        return res