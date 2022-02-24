class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}
        for i in range(len(nums)):
            if nums[i] not in dict:
                dict[nums[i]] = i
            temp = target-nums[i]
            if temp in dict and dict[temp]!=i:
                return [i, dict[target-nums[i]]]