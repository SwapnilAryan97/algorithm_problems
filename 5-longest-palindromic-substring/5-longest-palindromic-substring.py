class Solution:
    def longestPalindrome(self, s: str) -> str:
        ans =""
        for i in range(len(s)):
            '''odd case like aba'''
            temp = self.helper(s,i,i)
            ans = max(temp,ans,key=len)
            '''even case like abba'''
            temp = self.helper(s,i,i+1)
            ans = max(temp,ans,key=len)
            
        return ans
    
    def helper(self, s, left,right):
        while left>=0 and right<len(s) and s[left]==s[right]:
            left-=1
            right+=1
        return s[left+1:right]