class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = []
        res = 0
        for i in range(len(s)):
            if s[i]==")":
                if not stack:  
                    res+=1
                else:
                    stack.pop()
            
            else:
                stack.append(s[i])
            
        
        return res + len(stack)