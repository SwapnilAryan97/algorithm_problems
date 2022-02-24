class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height)-1
        res = 0
        while left!=right:
            if height[left]<height[right]:
                val = (height[left])*(right-left)
                res = max(res,val)
                left+=1
            else:
                val = (height[right])*(right-left)
                res = max(res,val)
                right-=1
        return res