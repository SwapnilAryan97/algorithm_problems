class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        mem = {}
        for num in nums:
            if num not in mem:
                mem[num] = True
            else:
                return True