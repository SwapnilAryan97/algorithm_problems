class Solution:
    def balancedStringSplit(self, string: str) -> int:
        count = res = 0
        for s in string:
            count += 1 if s=='L' else -1
            if count==0:
                res+=1
        return res