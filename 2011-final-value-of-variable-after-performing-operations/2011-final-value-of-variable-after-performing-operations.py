class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        res = 0
        for str in operations:
            if str[0]=='X':
                if str[1]=='-':
                    res -=1
                if str[1]=='+':
                    res +=1
            
            elif str[0]=='-':
                res -=1
            else:
                res +=1
        return res