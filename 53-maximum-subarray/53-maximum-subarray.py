class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_ending = nums[0]
        max_sum = nums[0]
        for i in range(1,len(nums)):
            max_ending = max(max_ending+nums[i], nums[i])
            max_sum = max(max_ending, max_sum)
        return max_sum  