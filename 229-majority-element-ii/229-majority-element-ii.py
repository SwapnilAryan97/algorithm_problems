class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        mem={}
        n = len(nums)//3
        res = []
        
        for num in nums:
            if num not in mem:
                mem[num] = 1
            else:
                mem[num] +=1

        for key in mem:
            if mem[key]>n:
                res.append(key)
        
        return res
            