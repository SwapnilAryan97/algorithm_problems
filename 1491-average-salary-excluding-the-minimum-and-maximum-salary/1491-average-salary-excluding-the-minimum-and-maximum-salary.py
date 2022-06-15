class Solution:
    def average(self, nums: List[int]) -> float:
        nums.pop(nums.index(max(nums)))
        nums.pop(nums.index(min(nums)))
        return sum(nums)/len(nums)