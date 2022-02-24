class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        n = len(nums)
        m = len(multipliers)
        
        dp = [[0]*(m+1) for _ in range(m+1)]
        
        for i in range(m-1, -1, -1):
            for left in range(i, -1, -1):
                right = n-1-(i-left)
                mul = multipliers[i]
                dp[i][left] = max(nums[left]*mul + dp[i+1][left+1], 
                                  nums[right]*mul + dp[i+1][left])   
        
        return dp[0][0]